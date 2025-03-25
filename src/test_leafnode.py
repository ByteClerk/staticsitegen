import unittest

from leafnode import LeafNode

class TestHtmlNode(unittest.TestCase):

    def test_no_tag(self):
        leafnode = LeafNode(value="Hallo Welt")
        html = leafnode.to_html()
        self.assertEqual(html, "Hallo Welt")

    def test_with_tag(self):
        leafnode = LeafNode(value="Hallo Welt", tag="test")
        html = leafnode.to_html()
        self.assertEqual(html, "<test>Hallo Welt</test>")

    def test_with_tag2(self):
        leafnode = LeafNode(value="Hallo Welt", tag="p")
        html = leafnode.to_html()
        self.assertEqual(html, "<p>Hallo Welt</p>")

if __name__ == "__main__":
    unittest.main()