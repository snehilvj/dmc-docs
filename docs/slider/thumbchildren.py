import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = [
    dmc.Slider(
        thumbChildren=DashIconify(icon="mdi:heart", width=16),
        color="red",
        label=None,
        value=40,
        thumbSize=26,
        styles={"thumb": {"borderWidth": 2, "padding": 3}},
    ),
    dmc.RangeSlider(
        mt="xl",
        styles={"thumb": {"borderWidth": 2, "padding": 3}},
        color="red",
        label=None,
        value=[20, 60],
        thumbSize=26,
        thumbChildren=[
            DashIconify(icon="mdi:heart", width=16),
            DashIconify(icon="mdi:heart-broken", width=16),
        ],
    ),
]
