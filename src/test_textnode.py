import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        text_node = TextNode(text_type=TextType.TEXT, text="Hello, world!")
        result = text_node_to_html_node(text_node)
        self.assertEqual(result, LeafNode(value=result.value))

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode(text_type=TextType.BOLD, text="Hello, world!")
        result = text_node_to_html_node(text_node)
        self.assertEqual(result, LeafNode(tag="b", value="Hello, world!"))

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode(text_type=TextType.ITALIC, text="Hello, world!")
        result = text_node_to_html_node(text_node)
        self.assertEqual(result, LeafNode(tag="i", value="Hello, world!"))


if __name__ == "__main__":
    unittest.main()
