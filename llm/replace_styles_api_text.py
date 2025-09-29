

text = """
This component supports Styles API. With Styles API, you can customize styles of any inner element. See the Styling and Theming sections of these docs for more information.
"""

def replace_styles_api_text(md: str) -> str:
    return md.replace(".. styles_api_text::", text)

