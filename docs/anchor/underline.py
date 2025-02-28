import dash_mantine_components as dmc

component = dmc.Group([
    dmc.Anchor(
        "Underline always",
        href="https://www.dash-mantine-components.com/",
        target="_blank",
        underline = "always",
    ),
    dmc.Anchor(
        "Underline on hover",
        href="https://www.dash-mantine-components.com/",
        target="_blank",
        underline = "hover",
    ),
    dmc.Anchor(
        "Underline never",
        href="https://www.dash-mantine-components.com/",
        target="_blank",
        underline = "never",
    ),
    dmc.Anchor(
        "Underline not hover",
        href="https://www.dash-mantine-components.com/",
        target="_blank",
        underline = "not-hover",
    ),

])
