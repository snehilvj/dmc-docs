import uuid

import dash_mantine_components as dmc
from dash import html, Output, Input, clientside_callback

DEFAULT_PROPS = {
    "SegmentedControl": {"fullWidth": True},
    "Select": {"clearable": False, "searchable": False},
    "ColorPicker": {
        "withPicker": False,
        "swatches": [color[5] for color in dmc.theme.DEFAULT_COLORS.values()],
        "swatchesPerRow": 7,
    },
}

color_picker_callback_func = """function(color) {
    const colorMap = {
        "#2c2e33": "dark",
        "#aeb5bd": "gray",
        "#ff6b6b": "red",
        "#f06595": "pink",
        "#cc5de8": "grape",
        "#845ef7": "violet",
        "#5c7cfa": "indigo",
        "#329af0": "blue",
        "#21b7cf": "cyan",
        "#20c997": "teal",
        "#51cf66": "green",
        "#94d92e": "lime",
        "#fcc419": "yellow",
        "#ff922b": "orange",
    };
    return colorMap[color];
}"""


def create_configurator(demo, controls, center=True):
    # callback setup
    dmc_controls = []  # right pane
    callback_outputs = []
    callback_inputs = []

    demo.id = str(uuid.uuid4())

    # create control components
    for i, conf in enumerate(controls):
        prop, component_type = conf.pop("property"), conf.pop("component")
        cid = str(uuid.uuid4())

        # set some default props
        if component_type in DEFAULT_PROPS:
            conf.update(DEFAULT_PROPS[component_type])

        # get component type
        component_class = getattr(dmc, component_type)

        # create component
        component = component_class(id=cid, **conf)

        # wrap in InputWrapper if needed
        if component_type in ["SegmentedControl", "Slider"]:
            component = dmc.InputWrapper(html.Div(component), label=prop)

        # set the label
        component.label = prop[0].upper() + prop[1:]

        # add style
        component.style = {"marginTop": 0 if i == 0 else 15}

        # add component to right pane
        dmc_controls.append(component)

        if component_type == "ColorPicker":
            clientside_callback(
                color_picker_callback_func,
                Output(demo.id, prop),
                Input(cid, "value"),
            )
        else:
            # add Output
            callback_outputs.append(Output(demo.id, prop))

            # add Input
            callback_inputs.append(
                Input(cid, "checked" if component_type == "Switch" else "value")
            )

    if callback_outputs:
        # create callback
        clientside_callback(
            """
            function(...kwargs) {
                return Object.values(kwargs)
            }
            """,
            callback_outputs,
            callback_inputs,
        )

    # create panel
    return html.Div(
        className="demo-container",
        children=[
            html.Div(
                html.Div(demo),
                className="demo-preview",
                style=({"alignItems": "center"} if center else {}),
            ),
            html.Div(className="demo-controls", children=dmc_controls),
        ],
    )
