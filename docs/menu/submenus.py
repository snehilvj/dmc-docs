
import dash_mantine_components as dmc


menu = dmc.Menu(
    width=200,
    position="bottom-start",
    keepMounted=True, # required when using SubMenu
    children=[
        dmc.MenuTarget(
            dmc.Button("Toggle Menu")
        ),
        dmc.MenuDropdown([
            dmc.MenuItem("Dashboard"),

            dmc.SubMenu([
                dmc.SubMenuTarget(
                    dmc.SubMenuItem("Products")
                ),
                dmc.SubMenuDropdown([
                    dmc.MenuItem("All products"),
                    dmc.MenuItem("Categories"),
                    dmc.MenuItem("Tags"),
                    dmc.MenuItem("Attributes"),
                    dmc.MenuItem("Shipping classes"),
                ])
            ]),

            dmc.SubMenu([
                dmc.SubMenuTarget(
                    dmc.SubMenuItem("Orders")
                ),
                dmc.SubMenuDropdown([
                    dmc.MenuItem("Open"),
                    dmc.MenuItem("Completed"),
                    dmc.MenuItem("Cancelled"),
                ])
            ]),

            dmc.SubMenu([
                dmc.SubMenuTarget(
                    dmc.SubMenuItem("Settings")
                ),
                dmc.SubMenuDropdown([
                    dmc.MenuItem("Profile"),
                    dmc.MenuItem("Security"),
                    dmc.MenuItem("Notifications"),
                ])
            ]),
        ])
    ]
)

component=dmc.Center(menu)
