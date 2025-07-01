import dash_mantine_components as dmc
from dash import  Output, Input, callback, ctx, no_update


component = dmc.Center([
    dmc.DrawerStack(
        id="drawer-stack",
        children=[
            dmc.ManagedDrawer(
                id="drawer-delete-page",
                title="Delete this page?",
                children=[
                    dmc.Text("Are you sure you want to delete this page? This action cannot be undone."),
                    dmc.Group(
                        mt="lg",
                        justify="flex-end",
                        children=[
                            dmc.Button("Cancel", id="drawer-cancel-1", variant="default"),
                            dmc.Button("Delete", id="drawer-delete", color="red"),
                        ],
                    ),
                ],
            ),
            dmc.ManagedDrawer(
                id="drawer-confirm-action",
                title="Confirm action",
                children=[
                    dmc.Text("Are you sure you want to perform this action? This action cannot be undone. If you are sure, press confirm button below."),
                    dmc.Group(
                        mt="lg",
                        justify="flex-end",
                        children=[
                            dmc.Button("Cancel", id="drawer-cancel-2", variant="default"),
                            dmc.Button("Confirm", id="drawer-confirm", color="red"),
                        ],
                    ),
                ],
            ),
            dmc.ManagedDrawer(
                id="drawer-really-confirm-action",
                title="Really confirm action",
                children=[
                    dmc.Text("Jokes aside. You have confirmed this action. This is your last chance to cancel it. After you press confirm button below, action will be performed and cannot be undone. For real this time. Are you sure you want to proceed?"),
                    dmc.Group(
                        mt="lg",
                        justify="flex-end",
                        children=[
                            dmc.Button("Cancel", id="drawer-cancel-3", variant="default"),
                            dmc.Button("Confirm", id="drawer-final-confirm", color="red"),
                        ],
                    ),
                ],
            ),
        ]
    ),
    dmc.Button("Open drawer", id="drawer-stack-open")
])


@callback(
    Output("drawer-stack", "open"),
    Output("drawer-stack", "closeAll"),
    Input("drawer-stack-open", "n_clicks"),
    Input("drawer-cancel-1", "n_clicks"),
    Input("drawer-cancel-2", "n_clicks"),
    Input("drawer-cancel-3", "n_clicks"),
    Input("drawer-delete", "n_clicks"),
    Input("drawer-confirm", "n_clicks"),
    Input("drawer-final-confirm", "n_clicks"),
    prevent_initial_call=True,
)
def control_modals(*_):
    trigger = ctx.triggered_id
    if trigger == "drawer-stack-open":
        return "drawer-delete-page", False
    if trigger in ("drawer-cancel-1", "drawer-cancel-2", "drawer-cancel-3", "drawer-final-confirm"):
        return None, True
    if trigger == "drawer-delete":
        return "drawer-confirm-action", False
    if trigger == "drawer-confirm":
        return "drawer-really-confirm-action", False
    return no_update, no_update
