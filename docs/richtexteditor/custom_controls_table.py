import dash_mantine_components as dmc
from dash_iconify import DashIconify

toolbar = {
    "sticky": True,
    "controlsGroups": [
        [

            {
                "CustomControl": {
                    "ariaLabel": "Insert Table",
                    "title": "Insert Table",
                    "children": [DashIconify(icon="mdi:table-plus", width=20, height=20)],
                    "function": "insertTable",
                },
            },
            {
                "CustomControl": {
                    "ariaLabel": "Add Column Before",
                    "title": "Add Column Before",
                    "children": [DashIconify(icon="mdi:table-column-plus-before", width=20, height=20)],
                    "function": "addColumnBefore",
                },
            },
            {
                "CustomControl": {
                    "ariaLabel": "Delete Column",
                    "title": "Delete Column",
                    "children": [DashIconify(icon="mdi:table-column-remove", width=20, height=20)],
                    "function": "deleteColumn",
                },
            },
        ],
        [
            "Bold",
            "Italic",
            "Underline",
        ],
    ],
}

component = dmc.RichTextEditor(
    html= '<div>Click controls to insert table, add column before, or delete column</div>',
    toolbar = toolbar,
    className="rte"  # applies custom table styles to this component only
)