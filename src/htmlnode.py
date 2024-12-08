
from typing_extensions import Sequence


class HTMLNODE:
    def __init__(
        self, tag: str | None = None,
        value: str | None = None,
        children: Sequence["HTMLNODE"] | None = None,
        props: dict | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # raise NotImplementedError("Method to_html not implemented")
        if self.props is None:
            return ""

        return " ".join([
            f'{key}="{value}"' for key, value in self.props.items()
        ])

    def props_to_html(self):
        if self.props == None:
            return ""

        return " ".join([
            f'{key}="{value}"' for key, value in self.props.items()
        ])

    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"



class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
