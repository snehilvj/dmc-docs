import dash_mantine_components as dmc
from dash import Input, Output, callback

users = [
    {
        "value": "Emily Johnson",
        "label": "Emily Johnson",
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-7.png",
    },
    {
        "value": "Ava Rodriguez",
        "label": "Ava Rodriguez",
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-8.png",
    },
    {
        "value": "Olivia Chen",
        "label": "Olivia Chen",
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-4.png",
    },
    {
        "value": "Ethan Barnes",
        "label": "Ethan Barnes",
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-1.png",
    },
    {
        "value": "Mason Taylor",
        "label": "Mason Taylor",
        "image": "https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/avatars/avatar-2.png",
    },
]

component = dmc.Box([
    dmc.MultiSelect(
        id="multi-select-render-pill",
        data=users,
        label="Candidates",
        placeholder="Select candidates",
        value=["Emily Johnson", "Ava Rodriguez"],
        renderPill={ "function": "renderUserPill", "options": {"users": users}},
    ),
    dmc.Text(id="multi-select-render-pill-val")
])

@callback(
    Output("multi-select-render-pill-val", "children"),
    Input("multi-select-render-pill", "value"),
)
def update(value):
    return f"You selected {value}"
