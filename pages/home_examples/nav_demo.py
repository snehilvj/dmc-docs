import dash_mantine_components as dmc
from docs.stepper.loading import component as stepper_demo
from docs.pagination.interactive import target as pagination_demo
from docs.tabs.icons import component as tabs_demo
from docs.menu.submenus import menu as menu_demo

component =  dmc.Card([


    dmc.SimpleGrid([
        dmc.Stack([
            dmc.Text("Menu with submenus", my="md"),
            menu_demo
        ]),
        dmc.Stack([
            dmc.Text("Pagination", my="md"),
            pagination_demo
        ]),
    ], cols=2),
    dmc.Text("Stepper", my="md"),
    stepper_demo,
    dmc.Text("Tabs", my="md"),
    dmc.Box(tabs_demo, mb="lg"),
], withBorder=True)