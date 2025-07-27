
from generate_page import *
from copy_directory_contents import *
import sys

def main():
    basepath = "/"
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    
    copy_source_destination()
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()