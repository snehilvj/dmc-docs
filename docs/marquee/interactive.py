import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Marquee(
    children=[
        dmc.Badge("Python", color="red", variant="light", w=80),
        dmc.Badge("Plotly", color="blue", variant="light", w=80),
        dmc.Badge("Dash", color="violet", variant="light", w=80),
        dmc.Badge("Mantine", color="yellow", variant="light", w=80),
        dmc.Badge("React", color="teal", variant="light", w=80),
    ],
    maw=400,
    mah=400
)

configurator = Configurator(target, center_component=True)

configurator.add_switch("reverse", False)
configurator.add_switch("pauseOnHover", False)
configurator.add_segmented_control("orientation", ["vertical", "horizontal"], "horizontal")
configurator.add_number_slider("repeat", min=1, max=10, value=4)
configurator.add_number_slider("duration", min=5000, max=100000, value=40000)
configurator.add_slider("gap", "md")
configurator.add_switch("fadeEdges", True)

component = configurator.panel
