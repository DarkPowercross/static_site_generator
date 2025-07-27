import unittest
from blocktype import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_code_single_line(self):
        self.assertEqual(block_to_block_type("```print('hi')```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- List item"), BlockType.UNORDERED_LIST)

    def test_ordered_list_single_digit(self):
        self.assertEqual(block_to_block_type("1. First item"), BlockType.ORDERED_LIST)


    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is just a regular paragraph."), BlockType.PARAGRAPH)

    def test_whitespace_heading(self):
        self.assertEqual(block_to_block_type("    # Heading"), BlockType.PARAGRAPH)

    def test_edge_case_number_like(self):
        self.assertEqual(block_to_block_type("1a. Not an ordered list"), BlockType.PARAGRAPH)

class Test_Paragraphs(unittest.TestCase):
    def test_paragraphs(self):
        md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """```
This is text that _should_ remain
the **same** even with inline stuff
```"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == '__main__':
    unittest.main()
