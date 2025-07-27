import unittest

from textnode import TextNode, TextType
from split_nodes import *

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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestSplitNodesimages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

class TestSplitNodesLink(unittest.TestCase):
        def test_single_link(self):
            node = TextNode("Click [here](https://example.com)", TextType.TEXT)
            result = split_nodes_link([node])

            self.assertEqual(result, [
                TextNode("Click ", TextType.TEXT),
                TextNode("here", TextType.LINK, "https://example.com")
            ])

        def test_multiple_links(self):
            node = TextNode(
                "Visit [Google](https://google.com) or [Bing](https://bing.com)",
                TextType.TEXT
            )
            result = split_nodes_link([node])

            self.assertEqual(result, [
                TextNode("Visit ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://google.com"),
                TextNode(" or ", TextType.TEXT),
                TextNode("Bing", TextType.LINK, "https://bing.com")
            ])

        def test_link_at_start(self):
            node = TextNode("[Home](https://example.com) is where the heart is", TextType.TEXT)
            result = split_nodes_link([node])

            self.assertEqual(result, [
                TextNode("Home", TextType.LINK, "https://example.com"),
                TextNode(" is where the heart is", TextType.TEXT)
            ])

        def test_link_at_end(self):
            node = TextNode("Go to [Docs](https://docs.example.com)", TextType.TEXT)
            result = split_nodes_link([node])

            self.assertEqual(result, [
                TextNode("Go to ", TextType.TEXT),
                TextNode("Docs", TextType.LINK, "https://docs.example.com")
            ])

        def test_non_text_node(self):
            node = TextNode("Not a text node", TextType.BOLD)
            result = split_nodes_link([node])
            self.assertEqual(result, [node])

        def test_no_links(self):
            node = TextNode("Just some plain text with no links.", TextType.TEXT)
            result = split_nodes_link([node])
            self.assertEqual(result, [node])

class TestTextToTextNodes(unittest.TestCase):
    def test_all_elements(self):
        input_text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(input_text)
        self.assertEqual(result, expected)

    def test_plain_text(self):
        input_text = "Just plain text with no formatting"
        expected = [TextNode("Just plain text with no formatting", TextType.TEXT)]
        result = text_to_textnodes(input_text)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()