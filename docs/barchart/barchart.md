---
name: BarChart
description: Use BarChart component without type prop to render a regular bar chart. In a regular bar chart, each data series is plotted on its own and does not interact with other series.
endpoint: /components/barchart
package: dash_mantine_components
category: Charts
---

.. toc::

### Introduction

.. exec::docs.barchart.interactive
    :code: false

### Styles API
| Selector           | Static selector                   | Description                                      |
|:-------------------|:---------------------------------|:-------------------------------------------------|
| root               | .mantine-BarChart-root           | Root element                                    |
| bar                | .mantine-BarChart-bar            | Bar of the chart                                |
| axis               | .mantine-BarChart-axis           | X and Y axis of the chart                       |
| container          | .mantine-BarChart-container      | Recharts ResponsiveContainer component          |
| grid               | .mantine-BarChart-grid           | Recharts CartesianGrid component                |
| legend             | .mantine-BarChart-legend         | Legend root element                             |
| legendItem         | .mantine-BarChart-legendItem     | Legend item representing data series            |
| legendItemColor    | .mantine-BarChart-legendItemColor| Legend item color                               |
| legendItemName     | .mantine-BarChart-legendItemName | Legend item name                                |
| tooltip            | .mantine-BarChart-tooltip        | Tooltip root element                            |
| tooltipBody        | .mantine-BarChart-tooltipBody    | Tooltip wrapper around all items                |
| tooltipItem        | .mantine-BarChart-tooltipItem    | Tooltip item representing data series           |
| tooltipItemBody    | .mantine-BarChart-tooltipItemBody| Tooltip item wrapper around item color and name|
| tooltipItemColor   | .mantine-BarChart-tooltipItemColor| Tooltip item color                             |
| tooltipItemName    | .mantine-BarChart-tooltipItemName | Tooltip item name                              |
| tooltipItemData    | .mantine-BarChart-tooltipItemData | Tooltip item data                              |
| tooltipLabel       | .mantine-BarChart-tooltipLabel   | Label of the tooltip                            |
| referenceLine      | .mantine-BarChart-referenceLine  | Reference line                                  |
| axisLabel          | .mantine-BarChart-axisLabel      | X and Y axis labels                             |


### BarChart CSS variables

| Selector         | Variable             | Description                                      |
|:-----------------|:---------------------|:-------------------------------------------------|
| root             | --chart-grid-color   | Controls color of the grid and cursor lines      |
|                  | --chart-text-color   | Controls color of the axis labels                |
|                  | --chart-cursor-fill  | Controls fill color of the cursor line           |


### Keyword Arguments

#### BarChart

.. kwargs::BarChart
