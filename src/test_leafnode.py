import unittest

from leafnode import LeafNode

class TestHtmlNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_with_tag(self):
        leafnode = LeafNode("test", "Hallo Welt")
        html = leafnode.to_html()
        self.assertEqual(html, "<test>Hallo Welt</test>")

    def test_with_tag2(self):
        leafnode = LeafNode("p", "Hallo Welt")
        html = leafnode.to_html()
        self.assertEqual(html, "<p>Hallo Welt</p>")

if __name__ == "__main__":
    unittest.main()