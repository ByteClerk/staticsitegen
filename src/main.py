from textnode import TextNode, TextType

def main():
    textNode = TextNode("This is some anchor text", TextType.Link, "https://www.boot.dev")
    print(textNode)


main()