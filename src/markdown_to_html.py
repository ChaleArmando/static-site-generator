import re

from block_markdown import markdown_to_blocks, block_to_block_type

from inline_markdown import text_to_textnodes

from textnode import text_node_to_html_node

from htmlnode import HTMLNode, LeafNode, ParentNode

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    #print(text_nodes)
    html_nodes = []
    for t_node in text_nodes:
        html_node = text_node_to_html_node(t_node)
        html_nodes.append(html_node)
    #print(html_nodes)
    return html_nodes

def heading_blocks(text):
    new_text = text[0:6].lstrip("#").lstrip()+text[6:]
    tag = f"h{len(re.findall('#',text[0:6]))}"
    child_nodes = text_to_children(new_text)
    node = ParentNode(tag, child_nodes)
    #print(node.to_html())
    return node

def code_blocks(text):
    new_text = text[3:-3]
    new_text = new_text.strip("\n")
    child_nodes = text_to_children(new_text)
    node_code = ParentNode("code", child_nodes)
    node = ParentNode("pre", [node_code])
    #print(node.to_html())
    return node

def quote_blocks(text):
    text_lines = text.split("\n")
    new_text = text_lines[0][2:]
    count = 0
    for line in text_lines:
        if count > 0: new_text += "\n" + line[2:]
        count =+ 1
    child_nodes = text_to_children(new_text)
    node = ParentNode("blockquote", child_nodes)
    #print([node.to_html()])
    return node

def unordered_list_block(text):
    text_lines = text.split("\n")
    child_nodes = [ParentNode("li", text_to_children(text_lines[0][2:]))]
    count = 0
    for line in text_lines:
        if count > 0: child_nodes.append(ParentNode("li", text_to_children(line[2:])))
        count =+ 1
    node = ParentNode("ul", child_nodes)
    #print([node.to_html()])
    return node

def ordered_list_block(text):
    text_lines = text.split("\n")
    child_nodes = [ParentNode("li", text_to_children(re.sub("[0-9]+\. ", "", text_lines[0])))]
    count = 0
    for line in text_lines:
        if count > 0: child_nodes.append(ParentNode("li", text_to_children(re.sub("[0-9]+\. ", "", line))))
        count =+ 1
    node = ParentNode("ol", child_nodes)
    #print([node.to_html()])
    return node

def paragraph_blocks(text):
    child_nodes = text_to_children(text)
    node = ParentNode("p", child_nodes)
    #print(node)
    return node
    

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == "heading":
            nodes.append(heading_blocks(block))
        elif type == "code":
            nodes.append(code_blocks(block))
        elif type == "quote":
            nodes.append(quote_blocks(block))
        elif type == "unordered_list":
            nodes.append(unordered_list_block(block))
        elif type == "ordered_list":
            nodes.append(ordered_list_block(block))
        else:
            nodes.append(paragraph_blocks(block))
    html = ParentNode("div", nodes)
    #print([html.to_html()])
    return html

text = """
1. quote *1* try
2. more quote **2 example**
3. even more `try code` and

paragraph text example

and an ![image](https://i.imgur.com/zjjcJKZ.png)
""" 

text2 = """
This is **bolded** paragraph
text in a p
tag here

"""

#markdown_to_html_node(text2)