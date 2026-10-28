import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Splitter(
    h=200,
    classNames={"pane": "splitter-examples"},
    bd="1px solid var(--mantine-color-default-border)",
    children=[
        dmc.SplitterPane(
            "First pane",
            defaultSize=50,
            min=20,
        ),
        dmc.SplitterPane(
            "Second pane",
            defaultSize=50,
            min=20,
        ),
    ],
)

configurator = Configurator(target)
configurator.add_number_slider("lineSize", 4, min=1, max=10)
configurator.add_colorpicker("handleColor", "indigo")
configurator.add_switch("withHandle", True)


component = configurator.panel
