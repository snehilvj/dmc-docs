import dash_mantine_components as dmc

component = dmc.Box([

    dmc.Text(
        "Click the theme switch in the header to see how the background changes in different modes"
    ),
    dmc.Text(
        "CSS class defined for light and dark scheme",
        className="light-dark-demo",
        p="lg",
        m="md"
    ),
])