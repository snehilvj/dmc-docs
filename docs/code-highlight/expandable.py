import dash_mantine_components as dmc
from dash_iconify import DashIconify

styles_css = """
.dmc-api-demo-root {
  border: 1px solid light-dark(var(--mantine-color-gray-3), var(--mantine-color-dark-4));
  padding: var(--mantine-spacing-xs) var(--mantine-spacing-sm);
  border-radius: var(--mantine-radius-md);
  font-weight: 500;
  cursor: pointer;

  &[data-checked] {
    background-color: var(--mantine-color-blue-filled);
    border-color: var(--mantine-color-blue-filled);
    color: var(--mantine-color-white);
  }
}"""

demo_py = """
import dash_mantine_components as dmc

 dmc.Checkbox(
    classNames={"root": "dmc-api-demo-root"},
    label="Checkbox button",
    w=180
)"""


code = [
    {
        "fileName": "demo.py",
        "code": demo_py,
        "language": "python",
        "icon": DashIconify(icon="vscode-icons:file-type-reactts", width=20),
    },
    {
        "fileName": "styles.css",
        "code":styles_css,
        "language": "css",
        "icon": DashIconify(icon="vscode-icons:file-type-css", width=20),
    },
]

component = dmc.CodeHighlightTabs(
    code=code,
    withExpandButton=True,
    expandCodeLabel="Show full code",
    collapseCodeLabel="Show less",
)
