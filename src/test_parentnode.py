import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_simple_parent_node(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_nested_parent_nodes(self):
        nested_node = ParentNode(
            tag="div",
            children=[
                ParentNode(
                    tag="p",
                    children=[
                        LeafNode("b", "Bold in paragraph"),
                        LeafNode(None, " and normal text"),
                    ]
                ),
                LeafNode(None, "Separate text")
            ]
        )
        self.assertEqual(
            nested_node.to_html(),
            "<div><p><b>Bold in paragraph</b> and normal text</p>Separate text</div>"
        )

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[LeafNode("i", "italic text")])

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p", children=[])

    def test_props_attribute(self):
        node_with_props = ParentNode(
            tag="div",
            children=[LeafNode(None, "Content with class")],
            props={"class": "content", "id": "main"}
        )
        self.assertEqual(
            node_with_props.to_html(),
            '<div class="content" id="main">Content with class</div>'
        )

if __name__ == "__main__":
    unittest.main()
