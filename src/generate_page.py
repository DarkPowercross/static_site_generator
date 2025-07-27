import os
from blocktype import *
from copy_directory_contents import *
from extract_content import *

def generate_page(from_path, template_path, output_path, basepath):
    print(f"{from_path} to {output_path} using {template_path}")
    
    with open(from_path) as file:
        from_content = file.read()

    with open(template_path) as file:
        template_content = file.read()

    content = markdown_to_html_node(from_content)
    html_content = content.to_html()
    title = extract_title(from_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_content)

    template_content = template_content.replace('href="/', f'href="{basepath}')
    template_content = template_content.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as file:
        file.write(template_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path, exist_ok=True)
    for content in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, content)

        if os.path.isdir(src_path):
            dst_path = os.path.join(dest_dir_path, content)
            generate_pages_recursive(src_path, template_path, dst_path, basepath)

        elif os.path.isfile(src_path) and src_path.endswith(".md"):
            name, _ = os.path.splitext(content)
            dst_path = os.path.join(dest_dir_path, f"{name}.html")
            generate_page(src_path, template_path, dst_path, basepath)
