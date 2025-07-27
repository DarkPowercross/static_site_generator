import re

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^()\s]+)\)"
    return re.split(pattern, text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_links(text):
    pattern = r"(?<!!)\[([^\[\]]+)\]\(([^()\s]+)\)"
    return re.split(pattern, text)
