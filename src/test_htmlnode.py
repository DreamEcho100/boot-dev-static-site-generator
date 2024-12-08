import unittest

from htmlnode import HTMLNODE

class TestHTMLNODE(unittest.TestCase):
    def test_eq(self):
        node = HTMLNODE("div", "This is a div", None, {"class": "container"})
        node2 = HTMLNODE("div", "This is a div", None, {"class": "container"})
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)
        self.assertIs(node.children, None)
        self.assertIs(node2.children, None)
        self.assertIsNot(node.props, None)
        self.assertIsNot(node2.props, None)
        self.assertDictEqual(node.props, node2.props)

    def test_empty_props(self):
        node = HTMLNODE("div", "This is a div")
        self.assertIsNone(node.props)

    def test_not_eq_html(self):
        node = HTMLNODE("div", "This is a div", None, {"class": "container"})
        node2 = HTMLNODE("div", "This is a div", None, {"class": "container-fluid"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

if __name__ == "__main__":
    unittest.main()
