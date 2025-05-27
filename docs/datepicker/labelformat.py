import dash_mantine_components as dmc

component = dmc.Center(
    dmc.DatePicker(
        decadeLabelFormat="YY",
        yearLabelFormat="YYYY [year]",
        monthLabelFormat="MM/YY",
    )
)

