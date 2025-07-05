---
name: Dash Ag Grid
description: Combine Dash AG Grid with Dash Mantine Components to build high-performance, interactive data grids. This guide covers how to apply AG Grid themes that match your DMC app and how to embed DMC components as custom cell renderers and editors.
endpoint: /dash-ag-grid
package: dash_mantine_components
---

.. toc::

### Introduction

If you're new to Dash AG Grid, check out the [official Dash AG Grid documentation](https://dash.plotly.com/dash-ag-grid) for an overview of its features and capabilities.

By default, you get a lot features with just a few lines of code:

* Built-in theme pairs well with the DMC default theme
* Columns are resizable (drag the column header edges)
* Rows are sortable (click header; shift-click for multi-sort)
* Smooth row animations during filtering and sorting
* Boolean values are rendered as checkboxes
* Columns can be reordered by dragging
* Columns can be pinned to either side of the grid




### Basic Features Demo

.. exec::docs.dash-ag-grid.demo
   :code: false

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


### Light and Dark Mode

This example uses `dash-ag-grid` v31.3.0. You can switch between light and dark grid themes dynamically by updating the `className` prop in a callback.

See the [Dash AG Grid styling guide](https://dash.plotly.com/dash-ag-grid/styling-themes) or the upstream [AG Grid v31.3 themes docs](https://www.ag-grid.com/archive/31.3.0/react-data-grid/themes/) for more details and a list of built-in themes.

Click the light/dark mode toggle in the top right of this page to see the grid theme update live.

.. exec::docs.dash-ag-grid.simple

### Using DMC components in cell renderers

To go beyond plain text in grid cells, you can use custom components as cell renderers. AG Grid provides a powerful
system for embedding your own React components, and DMC components work great for this.

Key concepts:

* Use the `cellRenderer` prop to name the custom function.
* Use the `cellRendererParams` prop to pass props to that component from Python.

To use a custom component, define it in a `.js` file in your `/assets/` folder under the `window.dashAgGridComponentFunctions` namespace. AG Grid will automatically register it.


For an introduction to [dash-ag-grid Cell Renderers](https://dash.plotly.com/dash-ag-grid/cell-renderer-components) refer to the dash documentation.


```js
var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.MyFunction = function (props) {
   // define your cell renderer here
}
```

#### Example 1: DMC Card in Grid Cell

This example renders a `Card` layout using `Dash Mantine Components` within each cell. The layout is defined in the JavaScript function `DMC_Card`.

Want help writing these custom cell functions? See [Using AI to Generate Functions](/functions-as-props#using-ai-to-generate-javascript-functions) for how to describe the logic in plain English or Python and convert it to JavaScript.


.. exec::docs.dash-ag-grid.cell_renderer_card
    :code: false

.. sourcetabs::docs/dash-ag-grid/cell_renderer_card.py, assets/examples-ag-grid-js/dmc_card.js
    :defaultExpanded: false
    :withExpandedButton: true 




#### Example 2: Buttons with `cellRendererParams`

This example shows how to place interactive buttons inside grid cells. The JavaScript function `DMC_Button` is used in the `cellRenderer` prop. You can pass different visual props (color, icon, variant, etc.) using `cellRendererParams` per column.

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



## Using Dash Mantine Components as Cell Editors

Dash AG Grid includes several [built-in cell editors](https://dash.plotly.com/dash-ag-grid/provided-cell-editors), such as:
- Text Cell Editor
- Large Text Cell Editor
- Select Cell Editor
- Rich Select Cell Editor (AG Grid Enterprise)
- Number Cell Editor
- Date Cell Editor
- Checkbox Cell Editor

These editors are easy to use and require no extra JavaScript. But if you need more control or want to use Dash Mantine
Components as cell editors, you can create a custom cell editor.

To do this, define a JavaScript function in your app’s `/assets` folder. The example below uses a generic editor that 
works with any DMC component.

You simply pass the component to the `component` key inside `cellEditorParams`. Dash handles the rest.

```python
"cellEditorParams": {
    "component": dmc.Select(data=["A", "B", "C"])
}
```


### Example: Using DMC Components as Editors

This example shows how to use:

* `dmc.DatePickerInput` for selecting a date
* `dmc.TagsInput` for entering multiple values
* `dmc.Select` for choosing a fixed option

Note: Set `cellEditorPopup=True` for any editor that displays dropdowns, popovers, or calendars. This prevents clipping inside the grid.



.. exec::docs.dash-ag-grid.cell_editor
    :code: false

.. sourcetabs::docs/dash-ag-grid/cell_editor.py, assets/examples-ag-grid-js/dmc_cell_editor.js
    :defaultExpanded: false
    :withExpandedButton: true 

