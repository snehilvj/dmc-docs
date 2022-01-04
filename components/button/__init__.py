from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "button")

app.layout = DocsBlock(
    component_name="Button",
    children=[
        Text("Render button or link with button styles from mantine theme."),
        Heading("Interactive Demo"),
        Text(
            "You can customize your Button and then just copy the auto generated code."
        ),
        CodeBlock(__file__, "interactive.py", app, prism=False),
        Heading("With Gradient"),
        Text("You can also customize the gradient fill of the button."),
        CodeBlock(__file__, "gradient.py", app),
        Heading("Full width button"),
        Text("Pass `fullWidth=True` for a full width button."),
        CodeBlock(__file__, "button.py", app),
    ],
)
