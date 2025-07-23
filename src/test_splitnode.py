import unittest

from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, extract_markdown_images

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_split(self):
        node = TextNode("Hello `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("First `block`.", TextType.TEXT),
            TextNode("Second `bit` too.", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected = [
            TextNode("First ", TextType.TEXT),
            TextNode("block", TextType.CODE),
            TextNode(".", TextType.TEXT),
            TextNode("Second ", TextType.TEXT),
            TextNode("bit", TextType.CODE),
            TextNode(" too.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("Nothing to split here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_unmatched_delimiter_raises(self):
        node = TextNode("Oops this `is broken", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("unmatched delimiter", str(context.exception))

    def test_empty_delimited_segment(self):
        node = TextNode("Look at `` this", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Look at ", TextType.TEXT),
            TextNode("", TextType.CODE),
            TextNode(" this", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()