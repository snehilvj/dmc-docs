import dash_mantine_components as dmc


colors = {
    "Pandas": "grape",
    "NumPy": "blue",
    "Matplotlib": "teal",
    "Plotly": "violet",
}

component = dmc.Select(
    label="Choose a library",
    placeholder="Pick one",
    data=list(colors.keys()),
    renderOption={
        "function": "renderBadge",
        "options": {"colors": colors},
    },
)