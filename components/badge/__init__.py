from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "badge")

app.layout = DocsBlock(
    component_name="Badge",
    children=[
        ComponentDescription("Display badge, pill or tag."),
        Heading("Simple Example", id="simple-example"),
        Text(
            "You can create badges with different variants by setting the `variant` prop."
        ),
        CodeBlock(__file__, "variant.py", app),
        Heading("Colors", id="colors"),
        Text("Change the color of the badge by choosing from one of the theme colors."),
        CodeBlock(__file__, "colors.py", app),
        Heading("Radius", id="radius"),
        Text("You can set the radius of the badge using the `radius` prop."),
        CodeBlock(__file__, "radius.py", app),
        Heading("Size", id="size"),
        Text("You can set the size of the badge using the `size` prop."),
        CodeBlock(__file__, "size.py", app),
        Heading("With Gradient", id="gradient"),
        Text("You can also customize the gradient fill of the badge."),
        CodeBlock(__file__, "gradient.py", app),
        Heading("Badge within a Button", id="in-button"),
        Text("You can put badge in a button's `children`."),
        CodeBlock(__file__, "button.py", app),
    ],
)
