import dash_mantine_components as dmc

data = [
    {"item": "TaxRate", "Effective tax rate in %": 21, "color": "blue"},
    {"item": "Foreign inc.", "Effective tax rate in %": -15.5, "color": "teal"},
    {"item": "Perm. diff.", "Effective tax rate in %": -3, "color": "teal"},
    {"item": "Credits", "Effective tax rate in %": -3, "color": "teal"},
    {"item": "Loss carryf.", "Effective tax rate in %": -2, "color": "teal"},
    {"item": "Law changes", "Effective tax rate in %": 2, "color": "red"},
    {"item": "Reven. adj.", "Effective tax rate in %": 4, "color": "red"},
    {
        "item": "ETR",
        "Effective tax rate in %": 3.5,
        "color": "blue",
        "standalone": True,
    },
]

component = dmc.BarChart(
    h=300,
    data=data,
    dataKey="item",
    type="waterfall",
    series=[{"name": "Effective tax rate in %", "color": "blue"}],
    withLegend=True,
)
