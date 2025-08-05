

def markdown_to_blocks(markdown):

    result_blocks = []

    splits = markdown.split('\n\n')

    for split in splits:
        strip = split.strip()
        if strip == '':
            continue
        result_blocks.append(strip)

    return result_blocks