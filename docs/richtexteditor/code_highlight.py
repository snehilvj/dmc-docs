
import dash_mantine_components as dmc

code_example = """import dash_mantine_components as dmc
from dash import Dash

app = Dash()

app.layout = dmc.MantineProvider(
    dmc.Alert(
       "Welcome to Dash Mantine Components",
       title="Hello!",
       color="violet",
    )
)

if __name__ == "__main__":
    app.run(debug=True)"""

# Replace special HTML characters manually
escaped_code = (code_example
    .replace("&", "&amp;")
    .replace("<", "&lt;")
    .replace(">", "&gt;")
    .replace('"', "&quot;"))


component= dmc.RichTextEditor(
    html=f"<p>Regular paragraph</p><pre><code>{escaped_code}</code></pre>",
    extensions=[
        {"StarterKit": { "codeBlock": False }},
        "CodeBlockLowlight"
    ],
    toolbar={
        "controlsGroups": [
            [
                "Bold",
                "Italic",
                "Underline",
                "Strikethrough",
                "CodeBlock"
            ],
        ],
    },
)
