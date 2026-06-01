import dash_mantine_components as dmc

component = dmc.FunnelChart(
    data=[
        { 'name': 'USA', 'value': 400, 'color': 'blue' },
        { 'name': 'Other', 'value': 200, 'color': 'gray.6' },
      ]
)