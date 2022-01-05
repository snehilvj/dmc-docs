from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
    ComponentDescription,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "drawer")

app.layout = DocsBlock(
    component_name="Drawer",
    children=[
        ComponentDescription("Display overlay area at any side of the screen."),
        Heading("Simple Example", id="simple-example"),
        Text(
            """This is a basic example of dmc.Drawer. Set the `opened` property to open the drawer. The drawer 
                can be closed in the following ways: 
                
* programmatically (using callbacks)
* by clicking on the cross button (if not disabled using `hideCloseButton` prop)
* by clicking outside the drawer area (if not disabled using `noCloseOnClickOutside` prop)
* by pressing the ESC key (if not disabled using `noCloseOnEscape` prop)"""
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("Different Sizes", id="sizes"),
        Text("Set the size of the drawer using the `size` prop."),
        CodeBlock(__file__, "sizes.py", app),
        Heading("Placement", id="placement"),
        Text(
            "By default, Drawer will start to appear from the left, but this position can be customized by setting "
            "the `position` prop. "
        ),
        CodeBlock(__file__, "placement.py", app),
    ],
)
