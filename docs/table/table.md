---
name: Table
section: Typography
head: Render table with theme styles.
description: Use the Table component to display tables with Mantine's theme styles. An alternative to html.Table
component: Table
---

##### Simple Example

Use Table component to add Mantine styled tables in your app. use `dmc.Table` as a drop-in replacement for `html.Table` 
when constructing your table with dash-html-components i.e. `html.Th`, `html.Tr`, `html.Td`, `html.Tbody` and 
`html.Thead`.

.. exec::docs.table.simple

##### Spacing

To control spacing use `horizontalSpacing` and `verticalSpacing` props. Both props support spacing from Mantine's theme
and number values to set cell padding in px.

```python
import dash_mantine_components as dmc

dmc.Table(
    verticalSpacing="sm",
    horizontalSpacing=10,
    children=[...]
)
```

.. exec::docs.table.spacing
    :prism: false

A simple function can be written to construct this table directly from a dataframe.

```python
import dash_mantine_components as dmc
from dash import html

def create_table(df):
    columns, values = df.columns, df.values
    header = [html.Tr([html.Th(col) for col in columns])]
    rows = [html.Tr([html.Td(cell) for cell in row]) for row in values]
    table = [html.Thead(header), html.Tbody(rows)]
    return table
```

##### Striped and Rows Hover

```python
import dash_mantine_components as dmc

dmc.Table(
    striped=True,
    highlightOnHover=True,
    children=[...]
)
```

.. exec::docs.table.striped
    :prism: false
