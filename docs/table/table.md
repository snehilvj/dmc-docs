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
    withTableBorder=True,
    withColumnBorders=True,
    data={...}
)
```

.. exec::docs.table.striped
    :code: false


### Scroll container
To prevent viewport overflow wrap `Table` with `TableScrollContainer`. The component accepts `minWidth` prop which sets
minimum width below which table will be scrollable.

By default, `TableScrollContainer` uses `ScrollArea`, you can change it to native scrollbars by setting `type="native"`

You can also set `maxHeight` prop on `TableScrollContainer` to limit table height


.. exec::docs.table.scrollcontainer

### Vertical variant
Set `variant="vertical"` to render table with vertical layout:



.. exec::docs.table.vertical


### tableProps


Use `tableProps` to pass additional [HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table) 
to the underlying elements of a dmc.Table, such as `<td>`, `<tr>`, or `<th>`. This is useful when you need to control
layout behavior like `rowSpan`, `colSpan`.

You can pass tableProps to components like:
```python
dmc.TableTd("Monday", tableProps={"rowSpan": 2})
```

This example also shows how to include other dash components in table cells.

.. exec::docs.table.tableprops

### Styles API

.. styles_api_text::

#### Selectors

| Selector  | Static selector             | Description |
|-----------|-----------------------------|-------------|
| `table`   | `.mantine-Table-table`      | Root table element (Table component) |
| `thead`   | `.mantine-Table-thead`      | `<thead>` element (Table.Thead component) |
| `tbody`   | `.mantine-Table-tbody`      | `<tbody>` element (Table.Tbody component) |
| `tfoot`   | `.mantine-Table-tfoot`      | `<tfoot>` element (Table.Tfoot component) |
| `tr`      | `.mantine-Table-tr`         | `<tr>` element (Table.Tr component) |
| `th`      | `.mantine-Table-th`         | `<th>` element (Table.Th component) |
| `td`      | `.mantine-Table-td`         | `<td>` element (Table.Td component) |
| `caption` | `.mantine-Table-caption`    | `<caption>` element (Table.Caption component) |

#### CSS Variables

| Selector | Variable | Description |
|----------|----------|-------------|
| `table`  | `--table-border-color` | Controls border color of all elements inside table |
| `table`  | `--table-layout` | Controls `table-layout` of the table element, `auto` by default |
| `table`  | `--table-caption-side` | Controls `caption-side` of the table element, `bottom` by default |
| `table`  | `--table-horizontal-spacing` | Controls `padding-left` and `padding-right` of Table.Th and Table.Td elements |
| `table`  | `--table-vertical-spacing` | Controls `padding-top` and `padding-bottom` of Table.Td and Table.Th elements |
| `table`  | `--table-striped-color` | Controls `background-color` of even/odd Table.Tr elements |
| `table`  | `--table-highlight-on-hover-color` | Controls `background-color` of Table.Tr elements when hovered |
| `table`  | `--table-sticky-header-offset` | Controls top offset of sticky header |

#### Data Attributes

| Selector | Attribute | Condition | Value |
|----------|-----------|------------|-------|
| `table`  | `data-with-table-border` | `withTableBorder` prop is set on Table component | – |
| `th`, `td` | `data-with-column-border` | `withColumnsBorder` prop is set on Table component | – |
| `tr`      | `data-with-row-border` | `withRowsBorder` prop is set on Table component | – |
| `tr`      | `data-striped` | `striped` prop is set on Table component | `odd` \| `even` |
| `tr`      | `data-hover` | `highlightOnHover` prop is set on Table component | – |
| `tr`      | `data-size` | – | Value of `captionSize` prop on Table component |

### Keyword Arguments

#### Table

.. kwargs::Table

#### TableScrollContainer

.. kwargs::TableScrollContainer
