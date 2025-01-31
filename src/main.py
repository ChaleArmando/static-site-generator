from textnode import TextNode, TextType

print('hello world')

def main():
    test = TextNode("This a text node", TextType.BOLD, "https://www.boot.dev")
    test2 = TextNode("Second Test", TextType.ITALIC)
    test3 = TextNode("Third test", TextType.CODE, "print('Hello World')")

    print(test)
    print(test2)
    print(test3)

main()