import os
import shutil 

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def copy_dir(src_path, target_path):
    src_files = os.listdir(src_path)
    for file in src_files:
        full_path = os.path.join(src_path,file)
        if os.path.isdir(full_path):
            new_path = os.path.join(target_path,file)
            os.mkdir(new_path)
            copy_dir(full_path, new_path)
        else:
            src = os.path.join(src_path,file)
            tgt = os.path.join(target_path,file)
            shutil.copy(src, tgt)

def copy_static():
    target_path = "public/"
    src_path = "static/"
    if os.path.exists(src_path) != True: os.mkdir(src_path)
    if os.path.exists(target_path)!= True: os.mkdir(target_path)
    if len(os.listdir(target_path)) > 0:
        shutil.rmtree(target_path)
        os.mkdir(target_path)
    copy_dir(src_path, target_path)

def main():
    copy_static()

main()