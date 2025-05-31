import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="Your favorite Python library",
    placeholder="Pick value or enter anything",
    data=[
        "4 – NumPy",
        "1 – Pandas",
        "3 – Scikit-learn",
        "2 – Plotly",
    ],
    filter={"function": "filterPythonLibs"},
)
