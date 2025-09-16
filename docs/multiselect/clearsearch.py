import dash_mantine_components as dmc

component = dmc.MultiSelect(
    data=["aa", "ab", "ac", "ba", "bb", "bc"],
    value=["aa"],
    searchable=True,
    clearSearchOnChange=False
)

