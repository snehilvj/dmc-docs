---
name: LineChart
description: Line chart component
endpoint: /components/linechart
package: dash_mantine_components
category: Charts
---

.. toc::

### Introduction

.. exec::docs.linechart.interactive
    :code: false

### Styles API

| Selector         | Static selector                    | Description                                      |
|:-----------------|:----------------------------------|:-------------------------------------------------|
| root             | .mantine-LineChart-root           | Root element                                    |
| line             | .mantine-LineChart-line           | Line of the chart                               |
| axis             | .mantine-LineChart-axis           | X and Y axis of the chart                       |
| container        | .mantine-LineChart-container      | Recharts ResponsiveContainer component          |
| grid             | .mantine-LineChart-grid           | Recharts CartesianGrid component                |
| legend           | .mantine-LineChart-legend         | Legend root element                             |
| legendItem       | .mantine-LineChart-legendItem     | Legend item representing data series            |
| legendItemColor  | .mantine-LineChart-legendItemColor| Legend item color                               |
| legendItemName   | .mantine-LineChart-legendItemName | Legend item name                                |
| tooltip          | .mantine-LineChart-tooltip        | Tooltip root element                            |
| tooltipBody      | .mantine-LineChart-tooltipBody    | Tooltip wrapper around all items                |
| tooltipItem      | .mantine-LineChart-tooltipItem    | Tooltip item representing data series           |
| tooltipItemBody  | .mantine-LineChart-tooltipItemBody| Tooltip item wrapper around item color and name|
| tooltipItemColor | .mantine-LineChart-tooltipItemColor| Tooltip item color                             |
| tooltipItemName  | .mantine-LineChart-tooltipItemName | Tooltip item name                              |
| tooltipItemData  | .mantine-LineChart-tooltipItemData | Tooltip item data                              |
| tooltipLabel     | .mantine-LineChart-tooltipLabel   | Label of the tooltip                            |
| referenceLine    | .mantine-LineChart-referenceLine  | Reference line                                  |
| axisLabel        | .mantine-LineChart-axisLabel      | X and Y axis labels                             |


### LineChart CSS variables

| Selector         | Variable             | Description                                      |
|:-----------------|:---------------------|:-------------------------------------------------|
| root             | --chart-grid-color   | Controls color of the grid and cursor lines      |
|                  | --chart-text-color   | Controls color of the axis labels                |


### Keyword Arguments

#### LineChart

.. kwargs::LineChart
