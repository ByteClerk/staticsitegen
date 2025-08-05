import unittest
from textblock import BlockType, block_to_block_type

class TestTextBlock(unittest.TestCase):

    def test_block_to_block_type_headline(self):
        blockType = block_to_block_type("# Heading 1")
        self.assertEqual(BlockType.HEADING, blockType)

        blockType = block_to_block_type("## Heading 2")
        self.assertEqual(BlockType.HEADING, blockType)
    
        blockType = block_to_block_type("###### Heading 6")
        self.assertEqual(BlockType.HEADING, blockType)

    def test_block_to_block_type_code(self):
        blockType = block_to_block_type("``` code ```")
        self.assertEqual(BlockType.CODE, blockType)

        blockType = block_to_block_type("```code```")
        self.assertEqual(BlockType.CODE, blockType)

        blockType = block_to_block_type("""```
multiline code
with multilines
    and tabs
```
""")
        self.assertEqual(BlockType.CODE, blockType)


    def test_block_to_block_type_quote(self):
        blockType = block_to_block_type(">quote")
        self.assertEqual(BlockType.QUOTE, blockType)

        blockType = block_to_block_type(""">quote
> test quote
>   with tabs
""")
        self.assertEqual(BlockType.QUOTE, blockType)

    def test_block_to_block_type_ul(self):
        blockType = block_to_block_type("- unordered list")
        self.assertEqual(BlockType.UNORDERED_LIST, blockType)

        blockType = block_to_block_type("""- unordered list
- test list
- a item
""")
        self.assertEqual(BlockType.UNORDERED_LIST, blockType)

    def test_block_to_block_type_ol(self):
        blockType = block_to_block_type("1. unordered list")
        self.assertEqual(BlockType.ORDERED_LIST, blockType)

        blockType = block_to_block_type("""1. unordered list
2. test list
3. a item
""")
        self.assertEqual(BlockType.ORDERED_LIST, blockType)

        blockType = block_to_block_type("""1. unordered list
 no list item
3. a item
""")
        self.assertEqual(BlockType.PARAGRAPH, blockType)