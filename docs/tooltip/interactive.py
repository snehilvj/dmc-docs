import dash_mantine_components as dmc

from lib.configurator import create_configurator

controls = [
    {"property": "color", "component": "ColorPicker"},
    {"property": "radius", "component": "DemoSlider", "value": "sm"},
    {
        "property": "position",
        "component": "Select",
        "data": ["top", "left", "right", "bottom"],
        "value": "top",
    },
    {
        "property": "placement",
        "component": "SegmentedControl",
        "data": ["start", "center", "end"],
        "value": "center",
    },
      {
        "property": "withArrow",
        "component": "Switch",
        "checked": True,
    },

]

demo = dmc.Tooltip(
    label="Tooltip",
    opened=True,
    withArrow=True,
    children=[
        dmc.Button(
            "Tooltip",
            variant="outline",
            size="xl",
        )
    ],
)

component = create_configurator(demo, controls)
