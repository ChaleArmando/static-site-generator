import os
import shutil
import re

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_to_html import markdown_to_html_node
from block_markdown import markdown_to_blocks

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

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    h1 = ""
    for block in blocks:
        if re.search(r'^#{1} .+', block):
            h1 = block[2:]
            break
    if h1 == "": raise Exception("Title not found")
    return h1

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file_mark:
        markdown = file_mark.read()
    with open(template_path) as file_temp:
        template = file_temp.read()
    html_nodes = markdown_to_html_node(markdown)
    html = html_nodes.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    path = os.path.join(dest_path,from_path.split("/")[-1].split(".")[0]+".html")
    with open(path, "x") as file_dest:
        file_dest.write(template)


def main():
    copy_static()
    generate_page("content/index.md", "template.html", "public/")

main()