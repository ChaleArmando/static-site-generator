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

test_node = TextNode("hello world **test** **later** and **then**", TextType.TEXT)
test_node2 = TextNode("**Second Test** try to understand **how it works**", TextType.CODE)
test_node3 = TextNode("Third Test **Exercise** to check **Different Types**", TextType.ITALIC)
split_nodes_delimiter([test_node, test_node2, test_node3], "**", TextType.BOLD)