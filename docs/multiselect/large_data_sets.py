import dash_mantine_components as dmc

component = dmc.MultiSelect(
    label="100,000 options",
    data=[f"Option {i}" for i in range(100000)],
    placeholder="use limit to optimize performance",
    limit=10,
    searchable=True,
    w=400,
)
