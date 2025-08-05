from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    
    if re.match(r"^#{1,6}", block) is not None:
        return BlockType.HEADING
    
    if re.match(r"^```.+?```", block, flags=re.DOTALL) is not None:
        return BlockType.CODE
    
    if block.startswith(">"):
        validBlock = True
        for part in block.splitlines():
            if part.startswith(">"):
                continue
            validBlock = False
            break
        if validBlock:
            return BlockType.QUOTE

    if block.startswith("- "):
        validBlock = True
        for part in block.splitlines():
            if part.startswith("- "):
                continue
            validBlock = False
            break
        if validBlock:
            return BlockType.UNORDERED_LIST
        
    if block.startswith("1."):
        validBlock = True
        for idx, part in enumerate(block.splitlines()):
            if part.startswith(f"{idx+1}."):
                continue
            validBlock = False
            break
        if validBlock:
            return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH