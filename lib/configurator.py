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
        colors = dmc.DEFAULT_THEME["colors"]
        mapping = {color: codes[5] for color, codes in colors.items()}
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
                size="sm",
                withPicker=False,
                swatches=list(mapping.values()),
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
            [Output(self.target_id, target_prop), Output(cid, "label")],
            Input(cid, "value"),
        )
        setattr(self.target, target_prop, mapping[value])
        control = dmc.Stack(
            [
                dmc.Text(create_label(target_prop), size="sm", fw=500),
                dmc.Slider(
                    min=1,
                    max=5,
                    value=mapping[value],
                    id=cid,
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
            ],
            gap=0,
        )
        self.controls.append(control)

    def add_number_slider(self, target_prop: str, value: int, **kwargs):
        cid = self.new_id
        self.outputs.append(Output(self.target_id, target_prop))
        self.inputs.append((Input(cid, "value")))
        setattr(self.target, target_prop, value)
        control = dmc.Stack(
            [
                dmc.Text(create_label(target_prop), size="sm", fw=500),
                dmc.Slider(value=value, id=cid, updatemode="drag", **kwargs),
            ],
            gap=0,
        )
        self.controls.append(control)

    def add_segmented_control(self, target_prop: str, data: List[str], value: str):
        cid = self.new_id
        self.outputs.append(Output(self.target_id, target_prop))
        self.inputs.append((Input(cid, "value")))
        setattr(self.target, target_prop, value)
        control = dmc.Stack(
            [
                dmc.Text(create_label(target_prop), size="sm", fw=500),
                dmc.SegmentedControl(id=cid, data=data, value=value, fullWidth=True),
            ],
            gap=1,
        )
        self.controls.append(control)

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
                dmc.GridCol(self.target, span={"sm": 12, "md": "auto"}, p=20),
                dmc.GridCol(
                    dmc.Stack(self.controls, gap="md", maw="100%", w=240, p=20),
                    span="content",
                ),
            ],
            align="center",
        )
