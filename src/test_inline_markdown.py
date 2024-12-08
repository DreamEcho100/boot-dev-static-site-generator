import unittest
from textnode import TextNode, TextType
from inline_markdown import  extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

# text_node_to_html_node
class TestInlineMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(images, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_extract_markdown_links(self):
        text = "This is text with a [link to google](https://www.google.com) and [link to duckduckgo](https://www.dukduckgo.com)"
        links = extract_markdown_links(text)
        self.assertEqual(links, [("link to google", "https://www.google.com"), ("link to duckduckgo", "https://www.dukduckgo.com")])

    def test_split_nodes_delimiter_1(self):
        node = TextNode("This is a text node", TextType.TEXT)
        nodes = [node]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_split_nodes_delimiter_3(self):
        node = TextNode("This is a **text node", TextType.TEXT)
        nodes = [node]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "**", TextType.BOLD)

    def test_split_nodes_image(self):
        node = TextNode(
            "google: ![google logo light color](https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png) and youtube: ![youtube logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/YouTube_Logo_%282013-2017%29.svg/1280px-YouTube_Logo_%282013-2017%29.svg.png)",
            TextType.TEXT,
        )
        nodes = [node]
        new_nodes = split_nodes_image(nodes)

        self.assertEqual(
            new_nodes,
            [
                TextNode("google: ", TextType.TEXT, None),
                TextNode("google logo light color", TextType.IMAGE, "https://www.google.com/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png"),
                TextNode(" and youtube: ", TextType.TEXT, None),
                TextNode("youtube logo", TextType.IMAGE, "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/YouTube_Logo_%282013-2017%29.svg/1280px-YouTube_Logo_%282013-2017%29.svg.png"),
            ]
        )

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ]
        )

    def test_text_to_textnodes(self):
        # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            nodes,
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

if __name__ == '__main__':
    unittest.main()
