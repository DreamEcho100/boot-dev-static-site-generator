from enum import Enum
from typing_extensions import Any

from leafnode import LeafNode

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    url: str | None
    def __init__(self, text: str, text_type: TextType = TextType.TEXT, url: str | None = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: Any, /) -> bool:
        return (
            isinstance(value, TextNode) and
            self.text == value.text and
            self.text_type == value.text_type and
            self.url == value.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: "TextNode") -> LeafNode:
    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={ "href": text_node.url })
        case TextType.IMAGE:
            return LeafNode(tag="img", value=text_node.text, props={ "src": text_node.url, "alt": "" })
