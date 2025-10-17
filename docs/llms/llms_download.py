from collections import defaultdict

import dash
import dash_mantine_components as dmc
from dash import  dcc, callback, Input, Output, State

from lib.constants import DMC_VERSION, LLMS

category_order = [
    "General",
    "Theming",
    "Styling",
    "Layout",
    "Inputs",
    "Combobox",
    "Buttons",
    "Navigation",
    "Feedback",
    "Overlay",
    "Data Display",
    "Typography",
    "Miscellaneous",
    "Date Pickers",
    "Charts",
    "Dash",
    "Releases"
]

def make_tree_component():
    grouped = defaultdict(list)
    for item in LLMS:
        category = item.get('category', 'General')
        grouped[category].append(item['name'])

    # Build tree data in the order specified
    tree_data = [
        {
            "value": category,
            "label": category,
            "children": [{"value": f"{category}-{name}", "label": name} for name in grouped[category]]
        }
        for category in category_order
        if category in grouped
    ]
    return dmc.ScrollArea(
        dmc.Tree(
            data=tree_data,
            checkboxes=True,
            id="llms-custom-select"
        ),
        h=425,
        w=400
    )


llms_intro = f"""
> Dash Mantine Components v{DMC_VERSION} Documentation
> All relative links in this file should be resolved against https://www.dash-mantine-components.com
"""


component  = dmc.Box([
        dmc.Title("Select pages to include in custom llms.txt", order=5),
         make_tree_component(),

        dmc.Title("Additional instructions to include in llms.txt", order=5, mt="lg"),
        dmc.Textarea(
            llms_intro,
            autosize=True,
            minRows=2,
            maxRows=8,
            id="llms-custom-intro",
            w="100%"
        ),
        dmc.Title("Filename for download", order=5, mt="lg"),
        dmc.TextInput(value="llms.txt", id="llms-custom-filename"),
        dmc.Button("Download", id="llms-custom-download-btn", n_clicks=0, mt="lg"),
        dcc.Download(id="llms-custom-download", data={"content": "", "filename": "llms.txt"})
    ])


@callback(
    Output("llms-custom-download", "data"),
    Input("llms-custom-download-btn", "n_clicks"),
    State("llms-custom-select", "checked"),
    State("llms-custom-intro", "value"),
    State("llms-custom-filename", "value")
)
def download_custom_llm_txt(n, checked, intro, filename):
    if not checked:
        return dash.no_update

    checked_pages = [item.split("-", 1)[1] for item in checked]

    llm_content = [intro or ""]
    for p in LLMS:
        if p["name"] in checked_pages:
            llm_content.append(p["content"])
    llm_content= "\n".join(llm_content)

    return  {"content": llm_content, "filename": filename or "llms.txt"}

