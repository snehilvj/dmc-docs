from dash import  html, Output, Input, callback
import dash_mantine_components as dmc


limit = 10
total = 145
total_pages = (total + limit - 1) // limit

component = dmc.Group(
    justify="flex-end",
    children=[
        dmc.Text(id="message-withPages", size="sm"),
        dmc.Pagination(id="pagination-withPages", total=total_pages, value=1, withPages=False),
    ],
)


@callback(
    Output("message-withPages", "children"),
    Input("pagination-withPages", "value"),
)
def update_message(page):
    start = limit * (page - 1) + 1
    end = min(total, limit * page)
    return f"Showing {start} – {end} of {total}"

