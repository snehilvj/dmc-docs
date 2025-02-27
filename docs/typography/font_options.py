# font_options.py
import dash_mantine_components as dmc
from dash import Dash, Input, Output, clientside_callback, callback
from dash_iconify import DashIconify
from lib.configurator import Configurator


# Sample paragraph text for demonstration
sample_text = """Typography is the art and technique of arranging type to make written language legible, readable, and appealing when displayed. The arrangement of type involves selecting typefaces, point sizes, line lengths, line-spacing, and letter-spacing, and adjusting the space between pairs of letters. Typography also includes the study of the design of letterforms.

ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
!@#$%^&*()_+-=[]{}|;':",./<>?"""

# Sample code for the CodeHighlight component
sample_code = """import dash_mantine_components as dmc

def create_text(text, font_family):
    return dmc.Text(
        text,
        ff=font_family,
        size="md",
        style={"marginBottom": 20}
    )

dmc.CodeHighlight(
    language="python",
    code="print('Hello, world!')",
    style={"fontFamily": font_family}
)
"""

# List of fonts to showcase
fonts = [
    "Default",
    "Arial, sans-serif",
    "Helvetica, sans-serif",
    "Verdana, sans-serif",
    "Tahoma, sans-serif",
    "Calibri, sans-serif",
    "Futura, sans-serif",
    "Absolut Vodka, sans-serif",
    "Times New Roman, serif",
    "Georgia, serif",
    "Garamond, serif",
    "Palatino, serif",
    "Merriweather, serif",
    "Courier New, monospace",
    "Consolas, monospace",
    "Monaco, monospace",
    "Menlo, monospace",
    "Brush Script MT, cursive",
    "Impact, fantasy",
    "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif"
]



# Build the app layout
component = dmc.MantineProvider(
    theme={
        "fontFamilyMonospace": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace",
        "components": {
            "Select": {
                "styles": {"dropdown": {"maxHeight": "300px"}}
            }
        }
    },
    children=[
        dmc.Container([
            dmc.Paper(
                children=[
                    dmc.Group(
                        [
                            dmc.Title("Font Explorer", order=1),
                        ],

                        mb="xl",
                    ),
                    dmc.Text(
                        "Select a font from the dropdown to preview it in text and code:",
                        mb="md",
                    ),
                    dmc.Select(
                        id="font-select",
                        data=[{"value": font, "label": font} for font in fonts],
                        value="Default",
                        searchable=True,
                        style={"marginBottom": 20},
                        placeholder="Select a font",
                        clearable=True,
                    ),
                    dmc.Divider(mb="md"),

                    dmc.Title("Text Preview", order=3, mb="sm"),
                    dmc.Text(
                        sample_text,
                        id="sample-text",
                        style={"marginBottom": 20}
                    ),

                    dmc.Title("Code Preview", order=3, mb="sm"),
                    dmc.Text(
                        "The code below demonstrates how the selected font looks in a code block:",
                        mb="md",
                    ),
                    dmc.Box(id="code-highlight-container"),
                ],
                p="lg",
                shadow="sm",
                withBorder=True,
                radius="md",
                style={"marginTop": 20}
            )
        ], size="lg")
    ]
)


# Callback to update the text font
@callback(
    Output("sample-text", "style"),
    Input("font-select", "value")
)
def update_text_font(font):
    if font is None or font == "Default":
        return {"marginBottom": 20}
    return {"fontFamily": font, "marginBottom": 20}


# Callback to update the code highlight
@callback(
    Output("code-highlight-container", "children"),
    Input("font-select", "value")
)
def update_code_highlight(font):
    style = {}
    if font is not None and font != "Default":
        # For monospace fonts, apply to pre/code elements inside CodeHighlight
        style = {
            "pre": {"fontFamily": font},
            "code": {"fontFamily": font}
        }

    return dmc.CodeHighlight(
        language="python",
        code=sample_code,
        styles=style if (font is not None and font != "Default") else {},
        copyLabel="Copy code",
        copiedLabel="Copied!",
    )

