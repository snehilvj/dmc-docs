import dash_mantine_components as dmc
from dash_iconify import DashIconify

component = dmc.Header(
    height=70,
    # Set fixed to True in your app.
    # fixed=True,
    padding="md",
    children=[
        dmc.Group(
            position="apart",
            children=[
                dmc.Text("Company Name", color="dark", size="xl"),
                dmc.Group(
                    position="right",
                    children=[
                        dmc.Button(
                            dmc.Text(
                                "Discord",
                                color="dark",
                                weight="lighter",
                                size="sm",
                            ),
                            radius="xl",
                            variant="light",
                            color="gray",
                            rightIcon=[
                                DashIconify(
                                    icon="fa-brands:discord",
                                    width=20,
                                    color="#7289da",
                                )
                            ],
                        ),
                        dmc.Select(
                            style={"width": 300},
                            placeholder="Search",
                            searchable=True,
                            icon=[DashIconify(icon="radix-icons:magnifying-glass")],
                            data=["DatePicker", "Notification", "Drawer"],
                        ),
                    ],
                ),
            ],
        )
    ],
)
