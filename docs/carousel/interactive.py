import dash_mantine_components as dmc

from lib.configurator import Configurator

target = dmc.Carousel(
    [
        dmc.CarouselSlide(dmc.Text("Slide 1", ta="center", bg="blue", c="white", p=30)),
        dmc.CarouselSlide(dmc.Text("Slide 2", ta="center", bg="blue", c="white", p=30)),
        dmc.CarouselSlide(dmc.Text("Slide 3", ta="center", bg="blue", c="white", p=30)),
        dmc.CarouselSlide(dmc.Text("Slide 4", ta="center", bg="blue", c="white", p=30)),
    ],
    id="carousel",
)

configurator = Configurator(target)

configurator.add_segmented_control("align", ["start", "center", "end"], "center")
configurator.add_segmented_control(
    "orientation", ["horizontal", "vertical"], "horizontal"
)
configurator.add_slider("slideGap", "xs")
configurator.add_slider("controlsOffset", "sm")
configurator.add_number_slider("controlSize", 26, min=14, max=60)
configurator.add_switch("loop", True)
configurator.add_switch("dragFree", False)
configurator.add_switch("draggable", True)
configurator.add_switch("withControls", True)
configurator.add_switch("withIndicators", True)

component = configurator.panel
