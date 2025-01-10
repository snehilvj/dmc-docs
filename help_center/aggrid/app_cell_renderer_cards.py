"""
styling with custom cell renderer - Cards

Note:
Custom components  must be defined in the dashAgGridComponentFunctions.js in assets folder.
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc, _dash_renderer
import pandas as pd
import dash_mantine_components as dmc

_dash_renderer._set_react_version("18.2.0")
data = {

    "stats": ["Revenue", "EBITDA", "Net Income"],
    "results": ['$13,120,000','$1,117,000', '$788,000'],
    "change": [10.1, -22.1, 18.6],
    'comments': ['', '', '']
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "",
        "cellRenderer": "DMC_Card",
    },
    {
        "field": "comments",
        "editable": True,
        "cellEditorPopup": True,
        "cellEditor": "agLargeTextCellEditor",
        "minWidth": 300,
    },
]

grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="autoSize",
    dashGridOptions={"rowHeight": 100}
)


app = Dash(__name__)

app.layout = dmc.MantineProvider(html.Div(
    [
        dcc.Markdown("Example of cellRenderer with dash-mantine-components Card"),
        grid,
    ],
    style={"margin": 20},
), forceColorScheme="light")



if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder

---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};



dagcomponentfuncs.DMC_Card = function (props) {
    return React.createElement(
        window.dash_mantine_components.Card,
        {
            withBorder:true
        },
        React.createElement(
            window.dash_mantine_components.Text,
            {c:"dimmed", tt: "uppercase", fw:700},
            props.data.stats
        ),
        React.createElement(
            window.dash_mantine_components.Text,
            {size: "lg"},
            props.data.results
        ),
        React.createElement(
            window.dash_mantine_components.Text,
            {size: "sm", c: (props.data.change > 0) ? "green" : "red"},
            props.data.change + "%"
        )
    );
};



"""