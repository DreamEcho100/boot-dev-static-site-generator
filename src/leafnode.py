from htmlnode import HTMLNODE

class LeafNode(HTMLNODE):
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props=None
    ):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if (not self.value):
            raise ValueError("LeafNode must have a value")
        if (not self.tag):
            return self.value

        hml_attrs = self.props_to_html()
        return f"<{self.tag}{f" {hml_attrs}" if hml_attrs else ""}>{self.value}</{self.tag}>"

    def __eq__(self, other):
        return (
            isinstance(other, LeafNode) and
            self.tag == other.tag and
            self.value == other.value and
            self.props == other.props
        )
