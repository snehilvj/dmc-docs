import dash_mantine_components as dmc

component = dmc.Table(
    withTableBorder=True,
    withColumnBorders=True,

    children=[
        dmc.TableThead(
            dmc.TableTr([
                dmc.TableTh("Day"),
                dmc.TableTh("Time"),
                dmc.TableTh("Topic"),
                dmc.TableTh("Action"),
            ])
        ),
        dmc.TableTbody([
            dmc.TableTr([
                dmc.TableTd("Monday", tableProps={"rowSpan": 2}),
                dmc.TableTd("9:00 - 10:00"),
                dmc.TableTd("Building Interactive Dashboards with Dash"),
                dmc.TableTd(dmc.Button("Details", size="xs", variant="light")),
            ]),
            dmc.TableTr([
                dmc.TableTd("10:15 - 11:00"),
                dmc.TableTd("Advanced Callbacks and App Structure"),
                dmc.TableTd(dmc.Button("Details", size="xs", variant="light")),
            ]),
            dmc.TableTr([
                dmc.TableTd("Tuesday", tableProps={"rowSpan": 2}),
                dmc.TableTd("9:00 - 10:00"),
                dmc.TableTd("Data Visualization with Plotly Express"),
                dmc.TableTd(dmc.Button("Details", size="xs", variant="light")),
            ]),
            dmc.TableTr([
                dmc.TableTd("10:15 - 11:00"),
                dmc.TableTd("Deploying Dash Apps to the Web"),
                dmc.TableTd(dmc.Button("Details", size="xs", variant="light")),
            ]),
        ])
    ]
)
