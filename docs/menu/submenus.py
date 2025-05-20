
import dash_mantine_components as dmc


menu = dmc.Menu(
    width=200,
    position="bottom-start",
    children=[
        dmc.MenuTarget(
            dmc.Button("Toggle Menu")
        ),
        dmc.MenuDropdown([
            dmc.MenuItem("Dashboard"),

            dmc.MenuSub([
                dmc.MenuSubTarget(
                    dmc.MenuSubItem("Products")
                ),
                dmc.MenuSubDropdown([
                    dmc.MenuItem("All products"),
                    dmc.MenuItem("Categories"),
                    dmc.MenuItem("Tags"),
                    dmc.MenuItem("Attributes"),
                    dmc.MenuItem("Shipping classes"),
                ])
            ]),

            dmc.MenuSub([
                dmc.MenuSubTarget(
                    dmc.MenuSubItem("Orders")
                ),
                dmc.MenuSubDropdown([
                    dmc.MenuItem("Open"),
                    dmc.MenuItem("Completed"),
                    dmc.MenuItem("Cancelled"),
                ])
            ]),

            dmc.MenuSub([
                dmc.MenuSubTarget(
                    dmc.MenuSubItem("Settings")
                ),
                dmc.MenuSubDropdown([
                    dmc.MenuItem("Profile"),
                    dmc.MenuItem("Security"),
                    dmc.MenuItem("Notifications"),
                ])
            ]),
        ])
    ]
)

component=dmc.Center(menu)
