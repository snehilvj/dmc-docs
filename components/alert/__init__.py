from lib.blocks import (
    Text,
    Heading,
    CodeBlock,
    DocsBlock,
)
from lib.blueprints import DmcDash

app = DmcDash(__name__, "alert")

app.layout = DocsBlock(
    component_name="Alert",
    children=[
        Text("Attract user attention with important static message."),
        Heading("Simple Example"),
        Text(
            "Create an alert with the main message (`children`), the `title`, and the `color`."
        ),
        CodeBlock(__file__, "simple.py", app),
        Heading("Different colors"),
        Text("Set the color using `color` argument."),
        CodeBlock(__file__, "colors.py", app),
        Heading("Dismissible Alerts"),
        Text(
            "The alerts can be closed either programmatically by toggling the `hide` property or by clicking on the "
            "close button on the alert if enabled with `withCloseButton=True`."
        ),
        CodeBlock(__file__, "dismissible.py", app),
        Heading("Automatic Dismissal"),
        Text(
            "The alerts can also be timed out using the `duration` prop which accepts time in milliseconds."
        ),
        CodeBlock(__file__, "auto_dismissible.py", app),
    ],
)
