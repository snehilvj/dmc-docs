import dash_mantine_components as dmc

component = dmc.Autocomplete(
    label="Your country",
    placeholder="Pick value or enter anything",
    data=[
        "Great Britain",
        "Canada",
        "United States",
    ],
    filter={"function": "filterCountries"},
)
