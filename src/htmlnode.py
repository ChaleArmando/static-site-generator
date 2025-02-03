class HTMLNode():
    def __init__(self, tag = None, value= None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is not None:
            attr = ""
            for key, value in self.props.items():
                attr += f" {key}=\"{value}\""
            return attr
        return ""
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("Invalid HTML: no value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"  

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("Invalid HTML: no tag")
        if self.children is None or self.children == "":
            raise ValueError("Invalid HTML: no children")
        child_to_html = ""
        for child in self.children:
            child_to_html += child.to_html()
        html = f"<{self.tag}{self.props_to_html()}>{child_to_html}</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
