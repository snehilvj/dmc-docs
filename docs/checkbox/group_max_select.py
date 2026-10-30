import dash_mantine_components as dmc
from dash import html, Output, Input, callback

component = html.Div(
    [
        dmc.CheckboxGroup(
            id="checkbox-group-max",
            label="Select your favorite library",
            description="This is anonymous",
            withAsterisk=True,
            mb=10,
            children=dmc.Group(
                [
                    dmc.Checkbox(label="Pandas", value="pandas"),
                    dmc.Checkbox(label="Polars", value="polars"),
                    dmc.Checkbox(label="Vaex", value="vaex"),
                    dmc.Checkbox(label="Dask", value="dask"),
                ],
                mt=10,
            ),
            value=["pandas", "polars"],
            maxSelectedValues=2
        ),
        dmc.Text(id="checkbox-group-max-output"),
    ]
)


@callback(Output("checkbox-group--max-output", "children"), Input("checkbox-group-max", "value"))
def checkbox(value):
    return ", ".join(value) if value else None
