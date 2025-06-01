import dash_mantine_components as dmc

component = dmc.MultiSelect(
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
