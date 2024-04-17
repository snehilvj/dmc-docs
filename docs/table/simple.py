import dash_mantine_components as dmc

elements = [
    {"position": 6, "mass": 12.011, "symbol": "C", "name": "Carbon"},
    {"position": 7, "mass": 14.007, "symbol": "N", "name": "Nitrogen"},
    {"position": 39, "mass": 88.906, "symbol": "Y", "name": "Yttrium"},
    {"position": 56, "mass": 137.33, "symbol": "Ba", "name": "Barium"},
    {"position": 58, "mass": 140.12, "symbol": "Ce", "name": "Cerium"},
]

rows = [
    dmc.TableTr(
        [
            dmc.TableTd(element["position"]),
            dmc.TableTd(element["name"]),
            dmc.TableTd(element["symbol"]),
            dmc.TableTd(element["mass"]),
        ]
    )
    for element in elements
]

head = dmc.TableThead(
    dmc.TableTr(
        [
            dmc.TableTh("Element Position"),
            dmc.TableTh("Element Name"),
            dmc.TableTh("Symbol"),
            dmc.TableTh("Atomic Mass"),
        ]
    )
)
body = dmc.TableTbody(rows)
caption = dmc.TableCaption("Some elements from periodic table")

component = dmc.Table([head, body, caption])
