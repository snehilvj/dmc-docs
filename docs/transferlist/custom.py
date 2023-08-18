import dash_mantine_components as dmc

from docs.transferlist.simple import initial_values

component = dmc.TransferList(
    value=initial_values,
    searchPlaceholder=["Search item to add...", "Search item to remove..."],
    nothingFound=["Cannot find item to add", "Cannot find item to remove"],
    placeholder=["No item left to add", "No item left ro remove"],
)
