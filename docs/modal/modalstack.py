import dash_mantine_components as dmc
from dash import html, Output, Input, callback, ctx, no_update


component = dmc.Center([
    dmc.ModalStack(
        id="modal-stack",
        children=[
            dmc.ManagedModal(
                id="delete-page",
                title="Delete this page?",
                children=[
                    dmc.Text("Are you sure you want to delete this page? This action cannot be undone."),
                    dmc.Group(
                        mt="lg",
                        justify="flex-end",
                        children=[
                            dmc.Button("Cancel", id="cancel-1", variant="default"),
                            dmc.Button("Delete", id="delete", color="red"),
                        ],
                    ),
                ],
            ),
            dmc.ManagedModal(
                id="confirm-action",
                title="Confirm action",
                children=[
                    dmc.Text("Are you sure you want to perform this action? This action cannot be undone. If you are sure, press confirm button below."),
                    dmc.Group(
                        mt="lg",
                        justify="flex-end",
                        children=[
                            dmc.Button("Cancel", id="cancel-2", variant="default"),
                            dmc.Button("Confirm", id="confirm", color="red"),
                        ],
                    ),
                ],
            ),
            dmc.ManagedModal(
                id="really-confirm-action",
                title="Really confirm action",
                children=[
                    dmc.Text("Jokes aside. You have confirmed this action. This is your last chance to cancel it. After you press confirm button below, action will be performed and cannot be undone. For real this time. Are you sure you want to proceed?"),
                    dmc.Group(
                        mt="lg",
                        justify="flex-end",
                        children=[
                            dmc.Button("Cancel", id="cancel-3", variant="default"),
                            dmc.Button("Confirm", id="final-confirm", color="red"),
                        ],
                    ),
                ],
            ),
        ]
    ),
    dmc.Button("Open modal", id="open")
])


@callback(
    Output("modal-stack", "open"),
    Output("modal-stack", "closeAll"),
    Input("open", "n_clicks"),
    Input("cancel-1", "n_clicks"),
    Input("cancel-2", "n_clicks"),
    Input("cancel-3", "n_clicks"),
    Input("delete", "n_clicks"),
    Input("confirm", "n_clicks"),
    Input("final-confirm", "n_clicks"),
    prevent_initial_call=True,
)
def control_modals(*_):
    match ctx.triggered_id:
        case "open":
            return "delete-page", False
        case "cancel-1" | "cancel-2" | "cancel-3" | "final-confirm":
            return None, True
        case "delete":
            return "confirm-action", False
        case "confirm":
            return "really-confirm-action", False
        case _:
            return no_update, no_update
