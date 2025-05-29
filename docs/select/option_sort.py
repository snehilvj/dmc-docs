import dash_mantine_components as dmc

component = dmc.Select(
    label="Your favorite Python library",
    placeholder="Pick value",
    searchable=True,
    nothingFoundMessage="Nothing found...",
    data=[
        "4 – NumPy",
        "1 – Pandas",
        "3 – Scikit-learn",
        "2 – Plotly",
    ],
    filter={"function": "filterPythonLibs"},
)
