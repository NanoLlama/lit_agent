#!/usr/bin/env python3
"""Offline tests for scripts/fetch.py parsing and merge logic.

No network: every test runs against an inline fixture, so this is the check
that still works when the environment's network policy blocks the source APIs.

Run: python3 -I tests/test_fetch.py
"""

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import fetch  # noqa: E402

PUBMED_XML = b"""<?xml version="1.0"?>
<PubmedArticleSet>
 <PubmedArticle>
  <MedlineCitation>
   <PMID Version="1">40123456</PMID>
   <Article>
    <Journal>
     <ISOAbbreviation>Nat Biotechnol</ISOAbbreviation>
     <Title>Nature biotechnology</Title>
     <PubDate><Year>2026</Year><Month>Oct</Month></PubDate>
    </Journal>
    <ArticleTitle>Branched linkers raise nanobody DAR to 8 without
      altering clearance</ArticleTitle>
    <Abstract>
     <AbstractText Label="BACKGROUND">Cargo per nanobody is limited.</AbstractText>
     <AbstractText Label="RESULTS">DAR 8 gave 3.2-fold uptake over control.</AbstractText>
    </Abstract>
    <AuthorList>
     <Author><LastName>Smith</LastName><Initials>J</Initials></Author>
     <Author><LastName>Doe</LastName><Initials>A</Initials></Author>
     <Author><LastName>Roe</LastName><Initials>B</Initials></Author>
     <Author><LastName>Poe</LastName><Initials>C</Initials></Author>
    </AuthorList>
    <ArticleDate DateType="Electronic">
     <Year>2026</Year><Month>10</Month><Day>14</Day>
    </ArticleDate>
   </Article>
   <PublicationTypeList>
    <PublicationType>Journal Article</PublicationType>
   </PublicationTypeList>
  </MedlineCitation>
  <PubmedData>
   <ArticleIdList>
    <ArticleId IdType="pubmed">40123456</ArticleId>
    <ArticleId IdType="doi">10.1038/s41587-026-0001-2</ArticleId>
   </ArticleIdList>
  </PubmedData>
 </PubmedArticle>
 <PubmedArticle>
  <MedlineCitation>
   <PMID Version="1">40123457</PMID>
   <Article>
    <Journal><ISOAbbreviation>Pharm Rev</ISOAbbreviation>
     <PubDate><Year>2026</Year><Month>09</Month><Day>30</Day></PubDate>
    </Journal>
    <ArticleTitle>Antibody-drug conjugates in oncology: a review</ArticleTitle>
    <Abstract><AbstractText>We review the clinical landscape.</AbstractText></Abstract>
    <AuthorList>
     <Author><CollectiveName>ADC Working Group</CollectiveName></Author>
    </AuthorList>
   </Article>
   <PublicationTypeList>
    <PublicationType>Review</PublicationType>
   </PublicationTypeList>
  </MedlineCitation>
 </PubmedArticle>
</PubmedArticleSet>
"""

BIORXIV_RAW = [
    {  # matches: platform (nanobody) + delivery (transcytosis)
        "doi": "10.1101/2026.10.14.123456",
        "title": "A bivalent nanobody shuttle increases transcytosis per receptor",
        "authors": "Lee, K.; Park, S.; Kim, J.; Cho, H.",
        "date": "2026-10-14",
        "abstract": "We measure transcytosis of a nanobody shuttle.",
        "published": "NA",
    },
    {  # platform only ("antibody"), no delivery term -> dropped
        "doi": "10.1101/2026.10.14.999999",
        "title": "A new antibody against a kinase",
        "authors": "Ng, P.",
        "date": "2026-10-14",
        "abstract": "Affinity maturation of a kinase binder.",
        "published": "NA",
    },
    {  # delivery only, no platform term -> dropped
        "doi": "10.1101/2026.10.13.111111",
        "title": "Lipid nanoparticle cargo loading",
        "authors": "Ali, R.",
        "date": "2026-10-13",
        "abstract": "We improve encapsulation and delivery of siRNA.",
        "published": "NA",
    },
    {  # preprint that has since been published
        "doi": "10.1101/2026.09.01.222222",
        "title": "Valency controls antibody uptake",
        "authors": "Mori, T.",
        "date": "2026-09-01",
        "abstract": "Multivalent antibody uptake is measured.",
        "published": "10.1038/s41587-026-0009-9",
    },
]

KW = {
    "platform": ["nanobody", "VHH", "antibody"],
    "delivery": ["transcytosis", "delivery", "uptake", "encapsulation"],
}


class TestPubmedParsing(unittest.TestCase):
    def setUp(self):
        import xml.etree.ElementTree as ET
        root = ET.fromstring(PUBMED_XML)
        self.arts = [fetch._parse_pubmed_article(a)
                     for a in root.findall(".//PubmedArticle")]

    def test_core_fields(self):
        a = self.arts[0]
        self.assertEqual(a["id"], "PMID:40123456")
        self.assertEqual(a["journal"], "Nat Biotechnol")
        self.assertEqual(a["doi"], "10.1038/s41587-026-0001-2")
        self.assertEqual(a["alt_ids"], ["DOI:10.1038/s41587-026-0001-2"])
        self.assertEqual(a["url"], "https://pubmed.ncbi.nlm.nih.gov/40123456/")

    def test_title_whitespace_is_collapsed(self):
        self.assertEqual(
            self.arts[0]["title"],
            "Branched linkers raise nanobody DAR to 8 without altering clearance")

    def test_labelled_abstract_sections_are_joined_in_order(self):
        self.assertEqual(
            self.arts[0]["abstract"],
            "BACKGROUND: Cargo per nanobody is limited. "
            "RESULTS: DAR 8 gave 3.2-fold uptake over control.")

    def test_authors_truncated_after_three(self):
        self.assertEqual(self.arts[0]["authors"], "Smith J, Doe A, Roe B, et al.")

    def test_collective_name_used_when_no_personal_authors(self):
        self.assertEqual(self.arts[1]["authors"], "ADC Working Group")

    def test_article_date_preferred_over_issue_date(self):
        self.assertEqual(self.arts[0]["date"], "2026-10-14")

    def test_month_name_converted(self):
        self.assertEqual(self.arts[1]["date"], "2026-09-30")

    def test_review_flagged(self):
        self.assertFalse(self.arts[0]["is_review"])
        self.assertTrue(self.arts[1]["is_review"])

    def test_missing_doi_gives_no_alt_ids(self):
        self.assertEqual(self.arts[1]["alt_ids"], [])


class TestBiorxivFilter(unittest.TestCase):
    def setUp(self):
        self.out = fetch.biorxiv_filter(BIORXIV_RAW, "biorxiv", KW)

    def test_requires_both_platform_and_delivery_terms(self):
        titles = [r["title"] for r in self.out]
        self.assertEqual(len(self.out), 2, titles)
        self.assertIn("A bivalent nanobody shuttle increases transcytosis per receptor",
                      titles)
        self.assertNotIn("A new antibody against a kinase", titles)
        self.assertNotIn("Lipid nanoparticle cargo loading", titles)

    def test_preprint_fields(self):
        r = self.out[0]
        self.assertTrue(r["is_preprint"])
        self.assertEqual(r["id"], "DOI:10.1101/2026.10.14.123456")
        self.assertEqual(r["url"], "https://doi.org/10.1101/2026.10.14.123456")
        self.assertIsNone(r["published_doi"])

    def test_na_published_normalized_to_none_but_real_doi_kept(self):
        published = [r for r in self.out if r["published_doi"]]
        self.assertEqual(len(published), 1)
        self.assertEqual(published[0]["published_doi"], "10.1038/s41587-026-0009-9")


class TestMerge(unittest.TestCase):
    def test_same_doi_across_sources_collapses_and_keeps_both_query_hits(self):
        pm = {"id": "PMID:1", "alt_ids": ["DOI:10.1/x"], "title": "Alpha",
              "doi": "10.1/x", "date": "2026-10-14", "is_preprint": False}
        ep = {"id": "DOI:10.1/x", "alt_ids": [], "title": "Alpha",
              "doi": "10.1/x", "date": "2026-10-14", "is_preprint": False}
        merged = fetch.merge([("q_a", [pm]), ("q_b", [ep])], cap=10)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["id"], "PMID:1")
        self.assertEqual(sorted(merged[0]["query_hits"]), ["q_a", "q_b"])

    def test_title_match_collapses_when_ids_differ(self):
        a = {"id": "DOI:10.1101/pre", "alt_ids": [], "doi": "10.1101/pre",
             "title": "Valency Controls Antibody Uptake!", "date": "2026-09-01",
             "is_preprint": True}
        b = {"id": "PMID:9", "alt_ids": [], "doi": "10.1038/pub",
             "title": "valency controls antibody uptake", "date": "2026-10-14",
             "is_preprint": False}
        merged = fetch.merge([("q_a", [a]), ("q_b", [b])], cap=10)
        self.assertEqual(len(merged), 1, [r["title"] for r in merged])

    def test_published_version_supersedes_preprint_and_sets_flag(self):
        pre = {"id": "DOI:10.1101/pre", "alt_ids": [], "doi": "10.1101/pre",
               "title": "Same Paper", "date": "2026-09-01", "is_preprint": True}
        pub = {"id": "PMID:9", "alt_ids": [], "doi": "10.1038/pub",
               "title": "Same paper", "date": "2026-10-14", "is_preprint": False}
        merged = fetch.merge([("q_a", [pre]), ("q_b", [pub])], cap=10)
        self.assertFalse(merged[0]["is_preprint"])
        self.assertTrue(merged[0]["preprint_published"])

    def test_distinct_articles_are_kept_and_sorted_newest_first(self):
        recs = [
            {"id": "PMID:1", "alt_ids": [], "doi": "", "title": "Older",
             "date": "2026-10-01", "is_preprint": False},
            {"id": "PMID:2", "alt_ids": [], "doi": "", "title": "Newer",
             "date": "2026-10-14", "is_preprint": False},
        ]
        merged = fetch.merge([("q", recs)], cap=10)
        self.assertEqual([r["title"] for r in merged], ["Newer", "Older"])

    def test_cap_is_applied(self):
        recs = [{"id": f"PMID:{i}", "alt_ids": [], "doi": "", "title": f"T{i}",
                 "date": "2026-10-14", "is_preprint": False} for i in range(10)]
        self.assertEqual(len(fetch.merge([("q", recs)], cap=3)), 3)


class TestConfig(unittest.TestCase):
    def setUp(self):
        import yaml
        self.cfg = yaml.safe_load(
            (Path(__file__).resolve().parent.parent / "config" / "queries.yaml")
            .read_text(encoding="utf-8"))

    def test_shipped_config_parses_into_queries(self):
        qs = fetch.flatten_queries(self.cfg)
        self.assertGreaterEqual(len(qs), 10)
        for q in qs:
            self.assertIn("/", q["name"])
            self.assertTrue(q["q"].strip())
            self.assertNotIn("\n", q["q"])

    def test_exclusion_clause_built_from_filters(self):
        clause = fetch.exclusion_clause(self.cfg)
        self.assertIn("NOT case reports[pt]", clause)
        self.assertTrue(clause.startswith(" NOT "))

    def test_increasing_cargo_group_is_weighted_above_baseline(self):
        weights = {q["group"]: q["weight"] for q in fetch.flatten_queries(self.cfg)}
        self.assertGreater(weights["increasing_cargo"], weights["core_platform"])

    def test_preprint_keywords_present_for_local_filter(self):
        kw = self.cfg["preprint_keywords"]
        self.assertTrue(kw["platform"] and kw["delivery"])


class TestEpmcQueryTransform(unittest.TestCase):
    """Europe PMC searches full text by default; queries must be TITLE_ABS-scoped."""

    def test_each_top_level_group_is_scoped(self):
        self.assertEqual(
            fetch.to_epmc_query("(valency OR multivalent) AND (nanobody OR antibody)"),
            "TITLE_ABS:(valency OR multivalent) AND TITLE_ABS:(nanobody OR antibody)")

    def test_bare_term_gets_parenthesized(self):
        self.assertEqual(
            fetch.to_epmc_query("(shuttle OR nanobody) AND brain"),
            "TITLE_ABS:(shuttle OR nanobody) AND TITLE_ABS:(brain)")

    def test_quoted_phrases_survive_untouched(self):
        self.assertEqual(
            fetch.to_epmc_query('(nanobody OR "single-domain antibody")'),
            'TITLE_ABS:(nanobody OR "single-domain antibody")')

    def test_inner_and_inside_a_group_is_not_split(self):
        # Splitting here would produce an unbalanced clause and a 0-hit query.
        self.assertEqual(
            fetch.to_epmc_query('(a AND b) AND (c)'),
            "TITLE_ABS:(a AND b) AND TITLE_ABS:(c)")

    def test_already_scoped_clause_left_alone(self):
        self.assertEqual(
            fetch.to_epmc_query("(nanobody) AND FIRST_IDATE:[2026-01-01 TO 2026-01-02]"),
            "TITLE_ABS:(nanobody) AND FIRST_IDATE:[2026-01-01 TO 2026-01-02]")

    def test_every_shipped_query_stays_balanced_and_fully_scoped(self):
        import yaml
        cfg = yaml.safe_load(
            (Path(__file__).resolve().parent.parent / "config" / "queries.yaml")
            .read_text(encoding="utf-8"))
        for q in fetch.flatten_queries(cfg):
            got = fetch.to_epmc_query(q["q"])
            with self.subTest(query=q["name"]):
                self.assertEqual(got.count("("), got.count(")"), got)
                for clause in got.split(" AND TITLE_ABS:"):
                    self.assertTrue(clause.strip(), got)
                self.assertTrue(got.startswith("TITLE_ABS:"), got)
                # No clause may escape scoping, or it silently matches full text.
                self.assertNotIn(" AND (", got.replace(" AND TITLE_ABS:(", " "))


class TestHelpers(unittest.TestCase):
    def test_norm_title_strips_case_and_punctuation(self):
        self.assertEqual(fetch.norm_title("Valency: Controls Uptake!"),
                         fetch.norm_title("valency controls uptake"))

    def test_iso_date_handles_missing_parts(self):
        self.assertEqual(fetch._iso_date("2026", "", ""), "2026-01-01")
        self.assertEqual(fetch._iso_date("", "", ""), "")
        self.assertEqual(fetch._iso_date("2026", "Mar", "5"), "2026-03-05")

    def test_ssl_context_verifies(self):
        ctx = fetch._ssl_context()
        import ssl as _ssl
        self.assertEqual(ctx.verify_mode, _ssl.CERT_REQUIRED)
        self.assertTrue(ctx.check_hostname)


if __name__ == "__main__":
    unittest.main(verbosity=2)
