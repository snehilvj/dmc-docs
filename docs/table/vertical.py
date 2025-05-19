import dash_mantine_components as dmc

component = dmc.Table(
    withTableBorder=True,
    layout="fixed",
    variant="vertical",
    children=[
        dmc.TableTbody([
            dmc.TableTr([
                dmc.TableTh("Epic name", w=160),
                dmc.TableTd("7.x migration"),
            ]),
            dmc.TableTr([
                dmc.TableTh("Status"),
                dmc.TableTd("Open"),
            ]),
            dmc.TableTr([
                dmc.TableTh("Total issues"),
                dmc.TableTd("135"),
            ]),
            dmc.TableTr([
                dmc.TableTh("Total story points"),
                dmc.TableTd("874"),
            ]),
            dmc.TableTr([
                dmc.TableTh("Last updated at"),
                dmc.TableTd("September 26, 2024 17:41:26"),
            ]),
        ])
    ]
)
