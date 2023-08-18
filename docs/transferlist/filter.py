import dash_mantine_components as dmc

from docs.transferlist.simple import initial_values

component = dmc.TransferList(value=initial_values, transferAllMatchingFilter=True)
