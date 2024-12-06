import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.SemiCircleProgress(
      fillDirection="left-to-right",
      orientation="up",
      filledSegmentColor="blue",
      size=350,
      thickness=12,
      value=40,
      label="Label"
)


configurator = Configurator(target)

configurator.add_segmented_control("fillDirection", ["left-to-right", "right-to-left"], "left-to-right")
configurator.add_segmented_control("orientation", ["up", "down"], "up")
configurator.add_colorpicker("filledSegmentColor", "red")

configurator.add_number_slider("size", 300, **{"min": 120, "max": 450} )
configurator.add_number_slider("thickness", 20,  **{"min": 1, "max": 20})
configurator.add_number_input("value", 69, **{"min": 0, "max": 100})

component = configurator.panel
