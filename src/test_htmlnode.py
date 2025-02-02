import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()