import dash_mantine_components as dmc

component = dmc.Slider(
    domain=[0, 100],
      min=10,
      max=90,
      value=25,
      marks=[
        { "value": 10, "label": 'min' },
        { "value": 90, "label": 'max' },
      ]
)
