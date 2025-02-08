import unittest

from block_markdown import markdown_to_blocks, block_to_block_type

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """
        # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
        """
        blocks = markdown_to_blocks(text)
        self.assertListEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )

    def test_markdown_to_blocks_newlines(self):
        text = """
        # This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.




* This is the first list item in a list block
* This is a list item
* This is another list item
        """
        blocks = markdown_to_blocks(text)
        self.assertListEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )

    def test_markdown_to_blocks_trim(self):
        text = """
                   # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.             

     * This is the first list item in a list block
* This is a list item
* This is another list item
        """
        blocks = markdown_to_blocks(text)
        self.assertListEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ]
        )
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "heading")
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "quote")
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), "unordered_list")
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "ordered_list")
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), "paragraph")

if __name__ == "__main__":
    unittest.main()
