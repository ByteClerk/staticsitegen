import unittest
from textnode import TextNode, TextType
from textnodesplitter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestNodeSplitter(unittest.TestCase):

    def test_code_without_in_text(self):
        node = TextNode("This is a text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertTrue(len(new_nodes) == 1)
        self.assertEqual(new_nodes[0].text, "This is a text")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)


    def test_code_in_text(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertTrue(len(new_nodes) == 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)


    def test_multi_bold_in_text(self):
        node = TextNode("This is *bold text* with 2 *bold block* in a text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertTrue(len(new_nodes) == 5)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "bold text")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " with 2 ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "bold block")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[4].text, " in a text")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)