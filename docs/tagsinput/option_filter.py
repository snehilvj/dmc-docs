import dash_mantine_components as dmc

component = dmc.TagsInput(
    label="What countries have you visited?",
    placeholder="Pick value or enter anything",
    data=[
        "Great Britain",
        "Canada",
        "United States",
    ],
    filter={"function": "filterCountries"},
)
