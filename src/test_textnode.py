import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is not a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_URL(self):
        node = TextNode("This is a an alphanumeric text node with a URL", TextType.TEXT, "https://google.com")
        node2 = TextNode("This is a an alphanumeric text node with a URL", TextType.TEXT, "https://google.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()