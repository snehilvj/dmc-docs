import dash_mantine_components as dmc

component = dmc.Box(
    dmc.Pagination(total=20, layout="responsive"),
    style={
        "resize": "horizontal",
        "overflow": "auto",
        "minWidth": 200,
        "maxWidth": "100%",
        "border": "1px solid var(--mantine-color-gray-5)",
        "padding": "16px",
    },
)