from htmlnode import HTMLNODE


class ParentNode(HTMLNODE):
    def __init__(
        self,
        children: list["HTMLNODE"],
        tag: str | None = None,
        props: dict | None = None
    ):
        if not tag:
                raise ValueError("ParentNode must have a tag")
        if ((not children) or (len(children) == 0)):
            raise ValueError("ParentNode must have at least one child")
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if ((not self.children) or (len(self.children) == 0)):
            raise ValueError("ParentNode must have at least one child")

        # Generate the HTML for properties
        html_attrs = self.props_to_html()

        # Recursively convert children to HTML
        children_html = ''.join(child.to_html() for child in self.children)

        return f"<{self.tag}{f' {html_attrs}' if html_attrs else ''}>{children_html}</{self.tag}>"
