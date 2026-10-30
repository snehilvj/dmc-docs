import dash_mantine_components as dmc

component = dmc.Stack([
    dmc.Group([
        dmc.Pagination(total=45, size="sm"),
        dmc.Button("sm button", size="sm"),
        dmc.TextInput(size="sm", placeholder="sm input"),
    ]),
    dmc.Group([
        dmc.Pagination(total=45, size="input-sm"),
        dmc.Button("sm button", size="sm"),
        dmc.TextInput(size="sm", placeholder="sm input"),
    ], mt="md"),
])
