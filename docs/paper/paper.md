---
name: Paper
section: Miscellaneous
head: Renders white or dark background depending on color scheme.
description: Render white or dark background depending on color scheme with Paper component with border, shadow, etc. 
component: Paper
---

##### Interactive Demo

Paper component renders white (or theme.colors.dark[7] for dark theme) background with shadow, border-radius and
padding from theme.

.. exec::docs.paper.interactive
    :prism: false

##### Shadow

```python
import dash_mantine_components as dmc

dmc.Paper(
    children=[],
    shadow="xs",
)
```

##### Padding

```python
import dash_mantine_components as dmc

dmc.Paper(
    children=[],
    p="xs", # or p=10 for padding of 10px
)
```

##### Radius

```python
import dash_mantine_components as dmc

dmc.Paper(
    children=[],
    radius="sm", # or p=10 for border-radius of 10px
)
```
