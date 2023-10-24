import dash_mantine_components as dmc

from components.configurator import Configurator

TARGET_ID = "interactive-ringprogress"

target = dmc.RingProgress(
    size=120,
    thickness=12,
    sections=[
        {"value": 40, "color": "red"},
        {"value": 15, "color": "yellow"},
        {"value": 15, "color": "violet"},
    ],
    id=TARGET_ID,
)

configurator = Configurator(target, TARGET_ID)

configurator.add_number_input("size", 120, **{"min": 60, "max": 400, "step": 10})
configurator.add_number_input("thickness", 12, **{"min": 0})
configurator.add_switch("roundCaps", False)

component = configurator.panel
