---
name: ScrollArea
description: Use the ScrollArea component to customize scrollbars.
endpoint: /components/scrollarea
package: dash_mantine_components
category: Miscellaneous
---

.. toc::
.. llms_copy::ScrollArea

### Introduction

The ScrollArea component supports the following props:

- `type` defines scrollbars behavior:
    - `hover` - scrollbars are visible on hover
    - `scroll` - scrollbars are visible on scroll
    - `auto` - similar to `overflow: auto` - scrollbars are always visible when the content is overflowing
    - `always` - same as auto but scrollbars are always visible regardless of whether the content is overflowing
    - `never` - scrollbars are always hidden
- `offsetScrollbars` - offset scrollbars with padding
    - x – adds padding to offset horizontal scrollbar only
    - y – adds padding to offset vertical scrollbar only
    - xy – adds padding to offset both scrollbars
    - present – adds padding only when scrollbars are visible

- `scrollbarSize` - scrollbar size, controls scrollbar and thumb width/height
- `scrollHideDelay` - delay in ms to hide scrollbars, applicable only when type is hover or scroll
- `overscrollBehavior` – controls overscroll-behavior of the viewport
- `scrollTo` sets scroll position of the viewport

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


### Disable horizontal scrollbars
To disable horizontal scrollbars set `scrollbars="y"` prop:


.. exec::docs.scrollarea.horizontal_disabled

### Scroll To

The `scrollTo` prop sets the scroll position of the viewport with the following options:

  * `top` – The vertical position as pixels (number) or percentage (string) from '0%' to '100%'
  * `left` – The horizontal position as pixels (number) or percentage (string) from '0%' to '100%'
  * `behavior` – scroll behavior: `auto` (instant) or `smooth` (animated), `smooth` by default

For example:

```python
# Scroll to specific pixel positions
dmc.ScrollArea(scrollTo={"top": 100, "left": 50})

# Scroll to percentage positions
dmc.ScrollArea(scrollTo={"top": "25%", "left": "75%"})

# Mixed usage
dmc.ScrollArea(scrollTo={"top": 200, "left": "50%", "behavior": "auto"})
```

---

.. exec::docs.scrollarea.scrollto

### ScrollAreaAutosize

`ScrollAreaAutosize` component allows to create scrollable containers when given max-height is reached.

.. exec::docs.scrollarea.autosize


### Styles API

.. styles_api_text::

####  ScrollArea Selectors
| Selector  | Static selector                 | Description                                       |
| --------- | ------------------------------- | ------------------------------------------------- |
| root      | `.mantine-ScrollArea-root`      | Root element                                      |
| content   | `.mantine-ScrollArea-content`   | Wraps component children                          |
| viewport  | `.mantine-ScrollArea-viewport`  | Main scrollable area                              |
| scrollbar | `.mantine-ScrollArea-scrollbar` | Horizontal or vertical scrollbar root             |
| thumb     | `.mantine-ScrollArea-thumb`     | Scrollbar thumb                                   |
| corner    | `.mantine-ScrollArea-corner`    | Corner between horizontal and vertical scrollbars |



#### ScrollArea CSS variables

| Selector | Variable                     | Description    |
|----------|------------------------------|----------------|
| root     | `--scrollarea-scrollbar-size`   | Scrollbar size |


#### ScrollArea data attributes

| Selector         | Attribute          | Condition                          | Value                               |
|------------------|--------------------|------------------------------------|-------------------------------------|
| scrollbar, corner| `data-hidden`         | `type="never"`                     | –                                   |
| corner           | `data-hovered`        | One of the scrollbars is hovered   | –                                   |
| scrollbar        | `data-orientation`    | –                                  | "horizontal" or "vertical" depending on scrollbar position |





### Keyword Arguments
.. style_props_text::

#### ScrollArea

.. kwargs::ScrollArea
