"""
Note - this isn't working quite right.  arrowPosition and arrowOffset doesn't work.
       might have something to do with how the type is defined?
"""

import dash_mantine_components as dmc

from lib.configurator import Configurator

TARGET_ID = "interactive-popover-arrow"

target = dmc.Center(
    dmc.Popover(
        [
            dmc.PopoverTarget(dmc.Button("Toggle Popover")),
            dmc.PopoverDropdown(dmc.Text("Arrow position can be changed for *-start and *-end positions")),
        ],
        width=200,
        position="bottom",
        withArrow=True,
        shadow="md",
        opened=True,
        id=TARGET_ID
    )
)

configurator = Configurator(target, TARGET_ID)
configurator.add_segmented_control("arrowPosition", ["center", "side"], "side")
configurator.add_number_slider("arrowOffset", value=6, max=50)
configurator.add_number_slider("arrowSize", value=12, max=12)
configurator.add_number_slider("arrowRadius", value=0, max=10)
configurator.add_switch("opened", checked=True)

component = configurator.panel
