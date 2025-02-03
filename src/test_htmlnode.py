import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_none(self):
        node = HTMLNode("h2", "Title 2 Text")
        node2 = HTMLNode("h2", "Title 2 Text", None, None)
        self.assertEqual(node.props_to_html(), node2.props_to_html())
    
    def test_props_to_html(self):
        node = HTMLNode("p", "Paragraph Text", ["a", "img"], {"href": "http://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), " href=\"http://google.com\" target=\"_blank\"")

    def test_values(self):
        node = HTMLNode("h1", "Title Text", None, {"color": "red"})
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.value, "Title Text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"color": "red"})

    def test_repr(self):
        node = HTMLNode("h1", "Title Text", None, {"color": "red"})
        self.assertEqual(node.__repr__(), "HTMLNode(h1, Title Text, children: None, {'color': 'red'})")

    def test_leaf_values(self):
        node = LeafNode("a", "Click me!", {"href":"https://boot.dev"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click me!")
        self.assertEqual(node.props, {"href":"https://boot.dev"})

    def test_leaf_to_html(self):
        node = LeafNode("a", "Click me!", {"href":"https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://boot.dev" target="_blank">Click me!</a>')
    
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Click me!", {"href":"https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html(), "Click me!")

    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"), LeafNode(None, "Normal Text"), LeafNode("i", "Italic text"), 
                LeafNode(None, "Normal Text Again"), LeafNode("strong", "Important text")
            ]
        )
        self.assertEqual(
            node.to_html()
            , "<p><b>Bold text</b>Normal Text<i>Italic text</i>Normal Text Again<strong>Important text</strong></p>"
            )
        
    def test_parent_no_children(self):
        node = ParentNode("p", [])
        self.assertEqual(node.to_html(), "<p></p>")

    def test_parent_mult_levels(self):
        node = ParentNode("div",[ParentNode("span",[LeafNode("i","Italic Text"),LeafNode("b", "Bold Text")]), LeafNode("strong", "Important Text")])
        self.assertEqual(node.to_html(), "<div><span><i>Italic Text</i><b>Bold Text</b></span><strong>Important Text</strong></div>")

    def test_parent_total(self):
        node = ParentNode("div",[ParentNode("span",[LeafNode("i","Italic Text"),LeafNode("b", "Bold Text")]), LeafNode("strong", "Important Text")]
                          , {"href":"https://boot.dev", "target": "_blank"})
        self.assertEqual(node.to_html()
                         , '<div href="https://boot.dev" target="_blank"><span><i>Italic Text</i><b>Bold Text</b></span><strong>Important Text</strong></div>')
if __name__ == "__main__":
    unittest.main()