import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_different_tags(self):
        node1 = HTMLNode(tag="p")
        node2 = HTMLNode(tag="div")
        self.assertNotEqual(node1, node2)

    def test_different_values(self):
        node1 = HTMLNode(value="Hello")
        node2 = HTMLNode(value="World")
        self.assertNotEqual(node1, node2)


    def test_children_equality(self):
        child1 = HTMLNode(tag="span", value="Child 1")
        child2 = HTMLNode(tag="span", value="Child 2")
        node1 = HTMLNode(tag="div", children=[child1])
        node2 = HTMLNode(tag="div", children=[child2])
        self.assertNotEqual(node1, node2)

    def test_props_equality(self):
        node1 = HTMLNode(tag="a", props={"href": "https://example.com"})
        node2 = HTMLNode(tag="a", props={"href": "https://example.org"})
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="img", props={"src": "image.png", "alt": "A picture"})
        self.assertEqual(node.props_to_html(), ' src="image.png" alt="A picture"')

if __name__ == "__main__":
    unittest.main()
