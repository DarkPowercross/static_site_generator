from textnode import TextNode, TextType
from regex import extract_markdown_images, extract_markdown_links, split_images, split_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if delimiter not in node.text:
            new_nodes.append(node)
            continue
      
        parts = node.text.split(delimiter)
    
        if len(parts) % 2 == 0:
            raise Exception(f"unmatched delimiter '{delimiter}' in '{node.text}'")

        for i , part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                    new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        original_data = node.text
        matches = extract_markdown_images(original_data)
        if not matches:
            new_nodes.append(node)
            continue
        
        parts = split_images(original_data)

        #this feels like it could be done better
        i = 0
        while i < len(parts):
            if i + 2 < len(parts):
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                alt_text = parts[i + 1]
                image_url = parts[i + 2]
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
                i += 3
            else:
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                i += 1

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.append(node)
            continue
        
        parts = split_links(node.text)
        
        #this feels like it could be done better
        i = 0
        while i < len(parts):
            if i + 2 < len(parts):
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                link_text = parts[i + 1]
                link_url = parts[i + 2]
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                i += 3
            else:

                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                i += 1

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

