---
name: Table
description: Use the Table component to display tables with Mantine's theme styles. An alternative to html.Table
endpoint: /components/table
package: dash_mantine_components
category: Typography
---

.. toc::

### Simple Example

Use Table component to add Mantine styled tables in your app. use `dmc.Table` and associated components as
drop-in replacements for `html.Table` and associated components respectively.

.. exec::docs.table.simple

### data prop

You can use `data` prop to automatically generate table rows from raw data. 
`data` prop accepts an object with the following properties: `head`, `foot`, `body`, `caption`:

.. exec::docs.table.data

### Spacing

To control spacing use `horizontalSpacing` and `verticalSpacing` props. Both props support spacing from Mantine's theme
and number values to set cell padding in px.

```python
import dash_mantine_components as dmc

dmc.Table(
    verticalSpacing="sm",
    horizontalSpacing=10,
    data={...}
)
```

.. exec::docs.table.spacing
    :code: false

### Striped and Rows Hover

```python
import dash_mantine_components as dmc

dmc.Table(
    striped=True,
    highlightOnHover=True,
    withBorder=True,
    withColumnBorders=True,
    data={...}
)
```

.. exec::docs.table.striped
    :code: false

### Styles API

| Name    | Static selector        | Description                                   |
|:--------|:-----------------------|:----------------------------------------------|
| table   | .mantine-Table-table   | Root `table` element (`Table` component)      |
| thead   | .mantine-Table-thead   | `thead` element (`Table.Thead` component)     |
| tbody   | .mantine-Table-tbody   | `tbody` element (`Table.Tbody` component)     |
| tfoot   | .mantine-Table-tfoot   | `tfoot` element (`Table.Tfoot` component)     |
| tr      | .mantine-Table-tr      | `tr` element (`Table.Tr` component)           |
| th      | .mantine-Table-th      | `th` element (`Table.Th` component)           |
| td      | .mantine-Table-td      | `td` element (`Table.Td` component)           |
| caption | .mantine-Table-caption | `caption` element (`Table.Caption` component) |

### Keyword Arguments

#### Table

.. kwargs::Table
