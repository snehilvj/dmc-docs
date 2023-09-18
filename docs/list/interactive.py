import dash_mantine_components as dmc

from components.configurator import Configurator

target = dmc.List(
    [
        dmc.ListItem("Join our Discord Community."),
        dmc.ListItem("Install python virtual environment."),
        dmc.ListItem(
            dmc.Text(["Install npm dependencies with ", dmc.Code("npm install")])
        ),
        dmc.ListItem(
            dmc.Text(["Add your new component in ", dmc.Code("src/lib/components.")])
        ),
        dmc.ListItem(
            "Raise a PR, including an example to reproduce the changes contributed by the PR."
        ),
    ],
    type="unordered",
)

configurator = Configurator(target)
configurator.add_segmented_control("type", ["unordered", "ordered"], "unordered")
configurator.add_slider("size", "md")
configurator.add_switch("withPadding", False)

component = configurator.panel
