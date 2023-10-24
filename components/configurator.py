import uuid
from typing import List, Optional

import dash_mantine_components as dmc
from dash import Input, Output, clientside_callback, ClientsideFunction
from dash.development.base_component import Component


def create_label(label: str) -> str:
    return label[0].upper() + label[1:]


class Configurator:
    def __init__(self, target_component: Component, target_id: Optional[str] = None):
        self.target = target_component
        self.target_id = target_id or self.new_id
        if not target_id:
            self.target.id = self.target_id
        self.outputs = []
        self.inputs = []
        self.controls = []

    @property
    def new_id(self):
        return str(uuid.uuid4())[:5]

    def add_colorpicker(self, target_prop: str, value: str):
        mapping = {
            "dark": "#2C2E33",
            "gray": "#adb5bd",
            "red": "#ff6b6b",
            "pink": "#f06595",
            "grape": "#cc5de8",
            "violet": "#845ef7",
            "indigo": "#5c7cfa",
            "blue": "#329af0",
            "cyan": "#22b8cf",
            "teal": "#20c997",
            "green": "#51cf66",
            "lime": "#94d82d",
            "yellow": "#fcc419",
            "orange": "#ff922b",
        }
        cid = self.new_id
        clientside_callback(
            ClientsideFunction(namespace="clientside", function_name="colorCallback"),
            Output(self.target_id, target_prop),
            Input(cid, "value"),
        )
        setattr(self.target, target_prop, mapping[value])
        self.controls.append(
            dmc.ColorPicker(
                id=cid,
                withPicker=False,
                swatches=[color[5] for color in dmc.theme.DEFAULT_COLORS.values()],
                swatchesPerRow=7,
                value=mapping[value],
            )
        )

    def add_switch(self, target_prop: str, checked: bool):
        cid = self.new_id
        self.outputs.append(Output(self.target_id, target_prop))
        self.inputs.append((Input(cid, "checked")))
        setattr(self.target, target_prop, checked)
        self.controls.append(
            dmc.Switch(id=cid, checked=checked, label=create_label(target_prop))
        )

    def add_slider(self, target_prop: str, value: str):
        mapping = {"xs": 1, "sm": 2, "md": 3, "lg": 4, "xl": 5}
        cid = self.new_id
        clientside_callback(
            ClientsideFunction(namespace="clientside", function_name="sliderCallback"),
            Output(self.target_id, target_prop),
            Input(cid, "value"),
        )
        setattr(self.target, target_prop, mapping[value])
        self.controls.append(
            dmc.InputWrapper(
                dmc.Slider(
                    min=1,
                    max=5,
                    value=mapping[value],
                    id=cid,
                    label=None,
                    updatemode="drag",
                    styles={"markLabel": {"display": "none"}},
                    marks=[
                        {"value": 1, "label": "xs"},
                        {"value": 2, "label": "sm"},
                        {"value": 3, "label": "md"},
                        {"value": 4, "label": "lg"},
                        {"value": 5, "label": "xl"},
                    ],
                ),
                label=create_label(target_prop),
            )
        )

    def add_segmented_control(self, target_prop: str, data: List[str], value: str):
        cid = self.new_id
        self.outputs.append(Output(self.target_id, target_prop))
        self.inputs.append((Input(cid, "value")))
        setattr(self.target, target_prop, value)
        self.controls.append(
            dmc.InputWrapper(
                dmc.SegmentedControl(id=cid, data=data, value=value, fullWidth=True),
                label=create_label(target_prop),
            )
        )

    def add_select(self, target_prop: str, data: List[str], value: str):
        cid = self.new_id
        self.outputs.append(Output(self.target_id, target_prop))
        self.inputs.append((Input(cid, "value")))
        setattr(self.target, target_prop, value)
        self.controls.append(
            dmc.Select(id=cid, data=data, label=create_label(target_prop), value=value)
        )

    def add_number_input(self, target_prop: str, value: int, **kwargs):
        cid = self.new_id
        self.outputs.append(Output(self.target_id, target_prop))
        self.inputs.append((Input(cid, "value")))
        setattr(self.target, target_prop, value)
        self.controls.append(
            dmc.NumberInput(
                id=cid, value=value, label=create_label(target_prop), **kwargs
            )
        )

    def add_text_input(self, target_prop: str, value: str, **kwargs):
        kwargs.setdefault("debounce", 100)
        cid = self.new_id
        self.outputs.append(Output(self.target_id, target_prop))
        self.inputs.append((Input(cid, "value")))
        setattr(self.target, target_prop, value)
        self.controls.append(
            dmc.TextInput(
                id=cid, value=value, label=create_label(target_prop), **kwargs
            )
        )

    @property
    def panel(self):
        if self.outputs and self.inputs:
            clientside_callback(
                ClientsideFunction(
                    namespace="clientside", function_name="generalCallback"
                ),
                self.outputs,
                self.inputs,
            )

        return dmc.Grid(
            [
                dmc.Col(self.target, span="auto", p=20, miw=400),
                dmc.Col(
                    dmc.Stack(self.controls, spacing="md", maw="100%", w=250, p=20),
                    span="content",
                ),
            ],
            align="center",
        )
