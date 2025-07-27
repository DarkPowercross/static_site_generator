import os
import shutil

def copy_source_destination(source="static", destination="docs"):
    if os.path.isdir(destination):
        shutil.rmtree(destination)
    copy_files(source, destination)
   

def copy_files(source="static", destination="docs"):
    os.makedirs(destination, exist_ok=True)
    for content in os.listdir(source):
        src_path = os.path.join(source, content)
        dst_path = os.path.join(destination, content)

        if os.path.isdir(src_path):
            copy_files(src_path, dst_path)
        elif os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
