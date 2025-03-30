import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        is_exception = False
        try:
            parent_node = ParentNode("div")
        except Exception as e:
            is_exception = True

        self.assertTrue(is_exception, "no excpetion on missing childs")

    
    def test_to_html_with_none_children(self):
        is_exception = False
        try:
            parent_node = ParentNode("div", None)
            parent_node.to_html()
        except Exception as e:
            is_exception = True

        self.assertTrue(is_exception, "no excpetion None missing childs")
