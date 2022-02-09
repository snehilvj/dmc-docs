import dash_mantine_components as dmc

component = dmc.Alert(
    "Make sure you are passing these extra components in a list, otherwise you will get an error from dash.",
    title="Passing components other than children",
    style={"marginBottom": 10},
    color="orange",
)
