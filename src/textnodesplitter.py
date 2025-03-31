
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    result_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        splitted = node.text.split(delimiter)
        
        if len(splitted) == 1:
            result_nodes.append(node)
            continue

        if len(splitted) % 2 != 1:
            raise Exception("unsupported")
        
        for i in range(len(splitted)):
            if i % 2 == 0:
                result_nodes.append(TextNode(splitted[i], TextType.TEXT))
            else:
                result_nodes.append(TextNode(splitted[i], text_type))

    return result_nodes


