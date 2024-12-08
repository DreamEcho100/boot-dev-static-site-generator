import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        ln = LeafNode("p", "Hello, World!")
        self.assertEqual(ln.to_html(), "<p>Hello, World!</p>")

    def test_leafnode_no_tag(self):
        ln = LeafNode(None, "Hello, World!")
        self.assertEqual(ln.to_html(), "Hello, World!")

    def test_leafnode_no_value(self):
        ln = LeafNode("p", None)
        with self.assertRaises(ValueError):
            ln.to_html()

    def test_leafnode_no_props(self):
        ln = LeafNode("p", "Hello, World!")
        self.assertEqual(ln.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
