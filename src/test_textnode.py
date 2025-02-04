import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")
        self.assertEqual(node, node2)
        node3 = TextNode("Test", TextType.IMAGE, "www.google.com")
        node4 = TextNode("Test", TextType.IMAGE, "www.yahoo.com")
        self.assertNotEqual(node3, node4)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a code node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text_to_html_img_node(self):
        node = TextNode("Alternate Image Text", TextType.IMAGE, "https://yahoo.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), '<img src="https://yahoo.com" alt="Alternate Image Text"></img>')

    def test_text_to_html_link_node(self):
        node = TextNode("Click Me!", TextType.LINK, "https://yahoo.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), '<a href="https://yahoo.com">Click Me!</a>')

if __name__ == "__main__":
    unittest.main()