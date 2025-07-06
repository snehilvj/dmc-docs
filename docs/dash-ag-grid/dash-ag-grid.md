---
name: Dash Ag Grid
description: Build high-performance, interactive data tables with Dash AG Grid and Dash Mantine Components. Learn how to apply light and dark grid themes and use DMC components as custom cell renderers and editors.
endpoint: /dash-ag-grid
package: dash_mantine_components
category: Dash
---

.. toc::

### Dash AG Grid quickstart

If you're new to Dash AG Grid, check out the [official Dash AG Grid documentation](https://dash.plotly.com/dash-ag-grid) for detailed information.

Here are just some of the features enabled by default in the quickstart example below:

* Built-in theme pairs well with the Mantine default theme
* Columns are resizable (drag the column header edges)
* Rows are sortable (click header; shift-click for multi-sort)
* Smooth row animations during filtering and sorting
* Boolean values are rendered as checkboxes
* Columns can be reordered by dragging
* Columns can be pinned to either side of the grid



### Quickstart Demo

.. exec::docs.dash-ag-grid.demo
   :code: false


```bash
pip install dash-ag-agrid

```

---

```python
import dash_mantine_components as dmc
import dash_ag_grid as dag
import pandas as pd
from dash import Dash

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/space-mission-data.csv")

app = Dash()

component = dag.AgGrid(
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
)

app.layout=dmc.MantineProvider(component)

app.run(debug=True)


```


### Explore More Grid Features

Be sure to check out the [Dash AG Grid documentation](https://dash.plotly.com/dash-ag-grid) for even more features, such as:

- Column: resizing, reordering, pinning, spanning, and grouping.
- Row: sorting, selection (including with checkboxes), reordering, dragging, spanning, pinned rows, and full width rows.
- Data Manipulation and Display: pagination, cell data types with automatic inference, custom filtering, and cell editing,  value getters and formatters, conditional formatting, and CSV data export.
- Layout and Styling:  themes (Alpine, Material, Quartz) with light/dark options, customizable themes, and conditional styling for various elements. Custom icons and more.
- Other Features: tooltips in cells and headers, keyboard navigation, accessibility support, and localization. 
- Enterprise Features:  All the above features are free in AG Grid Community.  Additional advanced features are available with an AG Grid Enterprise licence.

The next sections show how to apply AG Grid themes that match your Mantine light or dark theme, and how to use DMC
components as custom cell renderers and editors. 


### Theming: Light and Dark Mode Support

This example uses `dash-ag-grid` v31.3.0. The grid theme is set with the `className` prop.

To apply a built-in theme:

* Light mode: `className="ag-theme-alpine"` (default)
* Dark mode: `className="ag-theme-alpine-dark"`

Switch between light and dark themes by updating the `className` prop in a callback.

For more details and a full list of built-in themes and how to customize the theme, see the [Dash AG Grid styling guide](https://dash.plotly.com/dash-ag-grid/styling-themes) or the [AG Grid v31.3 theme docs](https://www.ag-grid.com/archive/31.3.0/react-data-grid/themes/).

Click the theme switch in the top right of this page to see the grid theme update live.

.. exec::docs.dash-ag-grid.simple


###  Custom Cell Renderers with DMC

For an introduction to [dash-ag-grid Cell Renderers](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) refer to the dash documentation.

A cell renderer is a JavaScript function that returns a component to customize the cell content, rather
than displaying simple text.  You can use DMC components as custom cell renderers.

Key concepts:

* Define the cell renderer function in a `.js` file in  `/assets/` under `window.dashAgGridComponentFunctions` namespace. Dash registers these components with the grid.
* Set `cellRenderer` to the function name.
* Pass extra props to the function with `cellRendererParams`.


```js
var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.MyFunction = function (props) {
   // define your cell renderer here
}
```



Want help writing these custom cell render functions? See [Using AI to Generate Functions](/functions-as-props#using-ai-to-generate-javascript-functions) for how to describe the logic in plain English or Python and convert it to JavaScript.



#### Example 1:  Card

This example displays grid data in a DMC `Card` in cells. The card layout is defined in a `.js` file in the `/assets` folder, with
the function named `DMC_Card`.


.. exec::docs.dash-ag-grid.cell_renderer_card
    :code: false

.. sourcetabs::docs/dash-ag-grid/cell_renderer_card.py, assets/examples-ag-grid-js/dmc_card.js
    :defaultExpanded: true
    :withExpandedButton: true 




#### Example 2: Buttons

This example shows how to place interactive buttons inside grid cells. The `DMC_Button` is defined in a `.js` file in
`/assets` is used in the `cellRenderer` prop. You can pass `Button` props (color, icon, variant, etc.) using 
`cellRendererParams` per column.

Here’s an example for the `"buy"` column:

```python
columnDefs = [
    {
        "field": "buy",
        "cellRenderer": "DMC_Button",
        "cellRendererParams": {
            "variant": "outline",
            "leftIcon": "ic:baseline-shopping-cart",
            "color": "green",
            "radius": "xl"
        },
    },
    #  other columns...

]


```


.. exec::docs.dash-ag-grid.cell_renderer_button
    :code: false

.. sourcetabs::docs/dash-ag-grid/cell_renderer_button.py, assets/examples-ag-grid-js/dmc_button.js
    :defaultExpanded: false
    :withExpandedButton: true 



###  Custom Cell editors with DMC

Dash AG Grid includes several [built-in cell editors](https://dash.plotly.com/dash-ag-grid/provided-cell-editors), such as:
- Text Cell Editor
- Large Text Cell Editor
- Select Cell Editor
- Rich Select Cell Editor (AG Grid Enterprise)
- Number Cell Editor
- Date Cell Editor
- Checkbox Cell Editor

These editors are easy to use and require no extra JavaScript. But if you need more control or want to use DMC components
as cell editors, you can create a custom cell editor.

The example below uses a generic editor function that works with any DMC component. Just copy the `.js` file into your app’s `/assets` folder to use it.
(Thanks to Dash community member [@BSd3v](https://github.com/BSd3v) for creating this!)

Then in your dash app you can pass a component written in Python to the function using the `cellEditorParams` prop:

```python
columnDefs = [
    {
        'cellEditor': {'function': 'AllFunctionalComponentEditors'},
        "cellEditorParams": {
            "component": dmc.Select(data=["A", "B", "C"])
        }
    },
    
]
```


#### Example: DatePickerInput, TagsInput, Select 

This example shows how to use the following DMC components as custom cell editors:

* `dmc.DatePickerInput`
* `dmc.TagsInput`
* `dmc.Select`

Note: Set `cellEditorPopup=True` for any editor that displays dropdowns, popovers, or calendars. This prevents clipping inside the grid.



.. exec::docs.dash-ag-grid.cell_editor
    :code: false

.. sourcetabs::docs/dash-ag-grid/cell_editor.py, assets/examples-ag-grid-js/dmc_cell_editor.js
    :defaultExpanded: false
    :withExpandedButton: true 

