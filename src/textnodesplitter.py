import re
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

def split_nodes_image(old_nodes):
    result_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        current_text = node.text
        images = extract_markdown_images(current_text)

        if len(images) == 0:
            result_nodes.append(node)
            continue

        for image_alt, image_link in images:
            splitted = current_text.split(f"![{image_alt}]({image_link})", 1)
            result_nodes.append(TextNode(splitted[0], TextType.TEXT))
            result_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            current_text = splitted[1]

    return result_nodes

def split_nodes_link(old_nodes):
    result_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue

        current_text = node.text
        links = extract_markdown_links(current_text)

        if len(links) == 0:
            result_nodes.append(node)
            continue

        for link_text, link_url in links:
            splitted = current_text.split(f"[{link_text}]({link_url})", 1)
            result_nodes.append(TextNode(splitted[0], TextType.TEXT))
            result_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            current_text = splitted[1]

    return result_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((http.*?)\)", text)
    return matches