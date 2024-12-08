import unittest
from markdown_blocks import BlockType, block_to_block_type, markdown_to_blocks, markdown_to_html_node

# text_node_to_html_node
class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_markdown_to_blocks_normal(self):
        markdown = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        """* This is the first list item in a list block
        * This is a list item
        * This is another list item"""
        ]

        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_extra_newlines(self):
        markdown = "\n\n# Heading\n\n\nParagraph text\n\n* List item 1\n* List item 2\n\n"
        expected = [
            "# Heading",
            "Paragraph text",
            "* List item 1\n* List item 2"
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_empty(self):
        markdown = "\n\n\n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_markdown_to_blocks_single(self):
        markdown = "# Single heading"
        expected = ["# Single heading"]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

        block = "### This is a subheading"
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```python\nprint('Hello World')\n```"
        self.assertEqual(block_to_block_type(block),BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block),BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "* This is an unordered list item"
        self.assertEqual(block_to_block_type(block),BlockType.UNORDERED_LIST)

        block = "- This is another unordered list item"
        self.assertEqual(block_to_block_type(block),BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        block = "1. This is an ordered list item"
        self.assertEqual(block_to_block_type(block),BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "This is just a normal paragraph of text."
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

    def test_block_to_block_type_edge_cases(self):
        block = "   "
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

        # Edge case for code block with triple backticks and content
        block = "```java\npublic class Main {}\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )




if __name__ == '__main__':
    unittest.main()
