import dash_mantine_components as dmc

component = dmc.Select(
    label="Your country",
    placeholder="Pick value",
    searchable=True,
    data=[
        "Great Britain",
        "Canada",
        "United States",
    ],
    filter={"function": "filterCountries"},
)
