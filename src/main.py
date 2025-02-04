from textnode import TextNode, TextType, text_node_to_html_node

from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    test = TextNode("This a text node", TextType.BOLD, "https://www.boot.dev")
    test2 = TextNode("Second Test", TextType.ITALIC)
    test3 = TextNode("Third test", TextType.CODE, "print('Hello World')")

    print(test)
    print(test2)
    print(test3)

    test_html = HTMLNode("p", "Paragraph Text", ["a", "img"], {"href": "http://google.com", "target": "_blank"})
    test_html2 = HTMLNode("h1", "Title Text", None, {"color": "red"})
    test_html3 = HTMLNode("h2", "Title 2 Text")
    print(test_html)
    print(test_html2)
    print(test_html3)
    print(test_html.props_to_html())
    print(test_html2.props_to_html())
    print(test_html3.props_to_html())

    test_leaf = LeafNode("p", "Paragrapg Text Test")
    test_leaf2 = LeafNode("a", "Click me!", {"href":"https://boot.dev"})
    print(test_leaf.to_html())
    print(test_leaf2.to_html())

    test_parent = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal Text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal Text Again"),
            LeafNode("strong", "Important text")
        ]
    )

    test_parent2 = ParentNode(
        "p",
        [
            
        ]
    )
    node = ParentNode("div",[ParentNode("span",[LeafNode("i","Italic Text"),LeafNode("b", "Bold Text")]), LeafNode("strong", "Important Text")])

    print(test_parent.to_html())
    print(test_parent2.to_html())
    print(node.to_html())

    test_transf = TextNode("Alternate Image Text", TextType.IMAGE, "https://yahoo.com")
    test_transf2 = TextNode("Click Me!", TextType.LINK, "https://yahoo.com")
    print(text_node_to_html_node(test_transf).to_html())
    print(text_node_to_html_node(test_transf2).to_html())

main()