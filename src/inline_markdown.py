import re

from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for node in old_nodes:
        node_text = node.text
        node_orig_type = node.text_type
        inline_text = node_text.split(delimiter)
        if len(inline_text) > 1 and len(inline_text) % 2 == 0:
            raise Exception("Invalid Syntax: Markdown Syntax not followed")
        new_nodes = []
        count = 0
        for text in inline_text:
            if count % 2 != 0:
                new_nodes.append(TextNode(text, text_type))
            elif len(text) > 0:
                new_nodes.append(TextNode(text, node_orig_type))
            count += 1
        nodes.extend(new_nodes)
    return nodes

def extract_markdown_images(text):
    list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return list

def extract_markdown_links(text):
    list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return list

def split_nodes_ref(old_nodes, type_search):
    nodes = []
    for node in old_nodes:
        node_text = node.text
        node_orig_type = node.text_type
        refs = []
        if type_search == TextType.IMAGE:
            refs = extract_markdown_images(node_text)
        elif type_search == TextType.LINK:
            refs = extract_markdown_links(node_text)
        if len(refs) == 0:
            nodes.append(node)
            continue
        count = 0
        for ref in refs:
            if type_search == TextType.IMAGE:
                sections = node_text.split(f"![{ref[0]}]({ref[1]})", 1)
            if type_search == TextType.LINK:
                sections = node_text.split(f"[{ref[0]}]({ref[1]})", 1)
            node_text = sections[-1]
            if sections[0] != "":
                nodes.append(TextNode(sections[0], node_orig_type))
            nodes.append(TextNode(ref[0], type_search, ref[1]))
            count += 1
            if count == len(refs) and sections[-1] != "":
                nodes.append(TextNode(sections[-1], node_orig_type))
    return nodes

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        node_text = node.text
        node_orig_type = node.text_type
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            nodes.append(node)
            continue
        count = 0
        for image in images:
            sections = node_text.split(f"![{image[0]}]({image[1]})", 1)
            node_text = sections[-1]
            print(sections)
            if sections[0] != "":
                nodes.append(TextNode(sections[0], node_orig_type))
            nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            count += 1
            if count == len(images) and sections[-1] != "":
                nodes.append(TextNode(sections[-1], node_orig_type))
    return nodes
text = "aaa ![to boot dev](https://www.boot.dev) and finish"
#print(split_nodes_image([TextNode(text, TextType.CODE)]))

#print(split_nodes_ref([TextNode(text, TextType.CODE)], TextType.IMAGE))
