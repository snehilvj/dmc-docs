

text = """
Note: This example uses custom JavaScript defined in the assets folder. Learn more in the "Functions As Props" section of this document.
"""

def replace_functions_as_props(md: str) -> str:
    return md.replace(".. functions_as_props::", text)

