

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        return "".join(f' {x[0]}="{x[1]}"' for x in self.props.items())
        
    def __repr__(self):

        children = None
        if(self.children != None):
            children = "\n".join(self.children)

        return f"HTMLNode: {self.tag} value: {self.value} props:{self.props_to_html()} children: {children}"

