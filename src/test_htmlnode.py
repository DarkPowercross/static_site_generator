import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
