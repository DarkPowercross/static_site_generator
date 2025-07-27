from textnode import *
from blocktype import *
from copy_directory_contents import *
from extract_content import *
from generate_page import *
from copy_directory_contents import *

def main():
    copy_source_destination()
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()