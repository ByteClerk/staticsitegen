import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

    def test_repr(self):
        htmlNode = HTMLNode(tag="<test>", props={ "href": "https://www.google.com","target": "_blank",})
        self.assertEqual(repr(htmlNode), 'HTMLNode: <test> value: None props: href="https://www.google.com" target="_blank" children: None')

    def test_props_to_html_1(self):
        htmlNode = HTMLNode(tag="<test>", props={ "href": "https://www.google.com","target": "_blank",})
        html = htmlNode.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_none(self):
        htmlNode = HTMLNode(tag="<test>")
        html = htmlNode.props_to_html()
        self.assertEqual(html, '')

if __name__ == "__main__":
    unittest.main()