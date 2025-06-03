import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-timegrid"

target = dmc.TimeGrid(
        timeRangeData={ "startTime": "10:00", "endTime": "21:00", "interval": "01:00" },
        withSeconds=False,
        simpleGridProps={
            "type": "container",
            "cols": { "base": 1, "180px": 2, "320px": 3 },
            "spacing": "xs",
        },
        value="10:00:00",
    )

configurator = Configurator(target, center_component=True)
configurator.add_segmented_control("format", ["12h", "24h"], "12h")
configurator.add_switch("withSeconds", True)
configurator.add_slider("size", "sm")
configurator.add_slider("radius", "sm")
component = configurator.panel


