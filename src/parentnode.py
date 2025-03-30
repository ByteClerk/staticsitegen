
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError()
        if self.children == None:
            raise ValueError()
        
        childsHtml = "".join( f"{child.to_html()}" for child in self.children)

        return f"<{self.tag}>{childsHtml}</{self.tag}>"