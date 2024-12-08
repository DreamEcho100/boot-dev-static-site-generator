import re
from textnode import TextNode, TextType

def text_to_textnodes(text: str) -> list["TextNode"]:
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)  # For bold text
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)  # For italic text
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)  # For code blocks

    return nodes


    return nodes



def split_text(text: str, delimiter: str, text_type: TextType):
    new_nodes = []
    delimiter_len = len(delimiter)

    while delimiter in text:
        start = text.find(delimiter)
        end = text.find(delimiter, start + delimiter_len)

        # If there's no matching closing delimiter, raise an error
        if end == -1:
            raise ValueError("Unmatched delimiter found in text")

        # Add the text before the delimiter as a separate node
        if start > 0:
            new_nodes.append(TextNode(text[:start], TextType.TEXT))

        # Add the text within the delimiters as the specified text type
        new_nodes.append(TextNode(text[start + delimiter_len:end], text_type))

        # Continue parsing after the closing delimiter
        text = text[end + delimiter_len:]

    # Add any remaining text after the last delimiter as a plain text node
    if text:
        new_nodes.append(TextNode(text, TextType.TEXT))


    return new_nodes

def split_nodes_delimiter(
    old_nodes: list["TextNode"],
    delimiter: str,
    text_type: TextType,
):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            new_nodes.extend(split_text(node.text, delimiter, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes: list["TextNode"]) -> list["TextNode"]:
    new_nodes = []

    for node in old_nodes:
        if not (node.text_type == TextType.TEXT):
            new_nodes.append(node)
            continue

        text = node.text

        matches = extract_markdown_images(text)
        matchexIndex = 0


        # if len(matches) == 0:
        #     return old_nodes

        while matchexIndex < len(matches):
            match = matches[matchexIndex]
            matchexIndex += 1
            before, _, after = text.partition(f"![{match[0]}]({match[1]})")

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes: list["TextNode"]) -> list["TextNode"]:
    new_nodes = []

    for node in old_nodes:
        if not (node.text_type == TextType.TEXT):
            new_nodes.append(node)
            continue

        text = node.text

        matches = extract_markdown_links(text)
        matchexIndex = 0

        # if len(matches) == 0:
        #     return old_nodes

        while matchexIndex < len(matches):
            match = matches[matchexIndex]
            matchexIndex += 1
            before, _, after = text.partition(f"[{match[0]}]({match[1]})")

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))

            text = after

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text: str):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches
