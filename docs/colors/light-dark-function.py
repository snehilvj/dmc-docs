import dash_mantine_components as dmc

component = dmc.Box([

    dmc.Text(
        "Click the theme switch in the header to see how the background changes in different modes:"
    ),
    # Using CSS color names
    dmc.Text(
        "light-dark(whitesmoke, gray)",
        style={"backgroundColor": "light-dark(whitesmoke, gray)"},
        p="lg",
        m="md"
    ),
    # Using Mantine CSS variables
    dmc.Text(
        "light-dark(var(--mantine-color-blue-1), var(--mantine-color-blue-9))",
        style={"backgroundColor": "light-dark(var(--mantine-color-blue-1), var(--mantine-color-blue-9))"},
        p="lg",
        m="md"
    )
])