import unittest

from inline_markdown import split_nodes_delimiter

from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("hello world **test** **later** and **then**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes, 
            [
                TextNode("hello world ", TextType.TEXT),
                TextNode("test", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("later", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("then", TextType.BOLD)
            ]
        )

    def test_delim_code(self):
        node = TextNode("1 Test `print('Exercise')` to check `def Code Types()`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes, 
            [
                TextNode("1 Test ", TextType.TEXT),
                TextNode("print('Exercise')", TextType.CODE),
                TextNode(" to check ", TextType.TEXT),
                TextNode("def Code Types()", TextType.CODE)
            ]
        )

    def test_delim_italic(self):
        node = TextNode("*Second Test* try to understand *how it works*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            new_nodes, 
            [
                TextNode("Second Test", TextType.ITALIC),
                TextNode(" try to understand ", TextType.TEXT),
                TextNode("how it works", TextType.ITALIC)
            ]
        )
        
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()