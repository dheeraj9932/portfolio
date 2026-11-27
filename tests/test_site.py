from html.parser import HTMLParser
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.images = []
        self.articles = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a":
            self.links.append(attrs)
        elif tag == "img":
            self.images.append(attrs)
        elif tag == "article":
            self.articles.append(attrs)


class PortfolioSiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = SiteParser()
        cls.parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
        cls.hrefs = [link.get("href", "") for link in cls.parser.links]

    def test_public_contact_and_current_project_links_are_real(self):
        required = {
            "mailto:dheeraj.tippani2@gmail.com",
            "https://github.com/dheeraj9932",
            "https://www.linkedin.com/in/dheeraj-tippani/",
            "https://dheeraj9932.github.io/schufi_uni_rostock_imaging/",
        }
        self.assertTrue(required.issubset(set(self.hrefs)))
        self.assertFalse(any("example.com" in href for href in self.hrefs))

    def test_primary_navigation_reaches_all_portfolio_sections(self):
        required_sections = {"work", "direction", "lab", "about", "contact"}
        self.assertTrue(required_sections.issubset(self.parser.ids))
        for section in required_sections:
            self.assertIn(f"#{section}", self.hrefs)

    def test_every_internal_fragment_link_has_a_target(self):
        missing = [
            href for href in self.hrefs
            if href.startswith("#") and len(href) > 1 and href[1:] not in self.parser.ids
        ]
        self.assertEqual([], missing)

    def test_future_repositories_are_explicitly_marked_as_planned(self):
        statuses = [article.get("data-status") for article in self.parser.articles]
        self.assertGreaterEqual(statuses.count("planned"), 3)
        self.assertIn("current", statuses)
        self.assertIn("prototype", statuses)
        self.assertIn("built", statuses)

    def test_project_media_is_local_and_has_alternative_text(self):
        self.assertGreaterEqual(len(self.parser.images), 3)
        for image in self.parser.images:
            src = image.get("src", "")
            self.assertTrue(src, "Every project image needs a source")
            self.assertTrue(image.get("alt", "").strip(), f"Missing alt text for {src}")
            self.assertFalse(src.startswith(("http://", "https://", "//")), src)
            self.assertTrue((ROOT / src).is_file(), f"Missing local image: {src}")


if __name__ == "__main__":
    unittest.main()
