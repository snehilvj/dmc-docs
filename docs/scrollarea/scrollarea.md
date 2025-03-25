---
name: ScrollArea
description: Use the ScrollArea component to customize scrollbars.
endpoint: /components/scrollarea
package: dash_mantine_components
category: Miscellaneous
---

.. toc::

### Introduction

The ScrollArea component works well with light and dark color schemes and supports the following props:

- `type` defines scrollbars behavior:
    - `hover` - scrollbars are visible on hover
    - `scroll` - scrollbars are visible on scroll
    - `auto` - similar to overflow: auto - scrollbars are always visible when the content is overflowing
    - `always` - same as auto but scrollbars are always visible regardless of whether the content is overflowing
    - `never` - scrollbars are always hidden
- `offsetScrollbars` - offset scrollbars with padding
- `scrollbarSize` - scrollbar size, controls scrollbar and thumb width/height
- `scrollHideDelay` - delay in ms to hide scrollbars, applicable only when type is hover or scroll

This example has a vertical scroll bar. 

.. exec::docs.scrollarea.interactive
   :code: false

This is how the ScrollArea height and width is defined in the example above 

```python

html.Div(
    [
        dmc.Title("Charizard (Pokémon)", order=3),
        dmc.ScrollArea(
            h=250, w=350,
            children = dmc.Paper(dmc.Text(text), withBorder=True),        
        )
    ]
)
```
### Horizontal scrollbars

The horizontal scroll bar will be displayed when the content of the ScrollArea is wider than the ScrollArea.

.. exec::docs.scrollarea.horizontal

### Styles API

.. styles_api_text::

####  ScrollArea Selectors

| Selector  | Static selector               | Description    |
|-----------|-------------------------------|----------------|
| root      | .mantine-ScrollArea-root       | Root element   |
| viewport  | .mantine-ScrollArea-viewport   |                |
| scrollbar | .mantine-ScrollArea-scrollbar  |                |
| thumb     | .mantine-ScrollArea-thumb      |                |
| corner    | .mantine-ScrollArea-corner     |                |



#### ScrollArea CSS variables

| Selector | Variable                     | Description    |
|----------|------------------------------|----------------|
| root     | --scrollarea-scrollbar-size   | Scrollbar size |


#### ScrollArea data attributes

| Selector         | Attribute          | Condition                          | Value                               |
|------------------|--------------------|------------------------------------|-------------------------------------|
| scrollbar, corner| data-hidden         | `type="never"`                     | –                                   |
| corner           | data-hovered        | One of the scrollbars is hovered   | –                                   |
| scrollbar        | data-orientation    | –                                  | "horizontal" or "vertical" depending on scrollbar position |




### Keyword Arguments

#### ScrollArea

.. kwargs::ScrollArea
