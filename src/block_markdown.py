import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        block = block.strip()
        if len(block) > 0:
            new_blocks.append(block)
    return new_blocks

def block_to_block_type(block):
    type = "paragraph"
    if re.search(r'^#{1,6} .+', block): type = "heading"
    if re.search(r'^(`{3})(\n*.*)+(`{3})$', block): type = "code"
    if re.search(r'^((\n{0,1}\>.*)+)$',block): type = "quote"
    if re.search(r'^((\n{0,1}[\*\-] .*)+)$', block): type = "unordered_list"
    if re.search(r'^((\n{0,1}[0-9]+\. .*)+)$', block):
        lines = block.split("\n")
        for line in lines:
            if line == "": lines.remove("")
        count = 1
        ordered_list = True
        for line in lines:
            order = re.search(r'^([0-9]+)', line)
            if int(order.group()) != count: ordered_list = False
            count += 1
        if ordered_list: type = "ordered_list"
    return type