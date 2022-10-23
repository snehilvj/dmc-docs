---
name: ActionIcon
section: Inputs & Buttons
head: Icon button to indicate secondary action.
description: Use this component as an alternative to buttons when you just want to use an icon.
component: ActionIcon
---

##### Interactive Demo

.. exec::docs.actionicon.interactive
    :prism: false

##### Usage

ActionIcon component is an alternative to [Button](/components/button) component. It can be customized with Mantine styles and used with its
`n_clicks` property.

.. exec::docs.actionicon.simple

##### Children

ActionIcon accepts any React node as child. It does not control the icon size, you need to specify it manually on icon
component (such as DashIconify) to match ActionIcon size.

For example, if you were to use DashIconify, you can set the icon size like this:

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ActionIcon(
    DashIconify(icon="bi:github", width=20),
    size="lg"
)
```

##### Variants

ActionIcon has 6 variants: subtle, filled, outline, light, default, transparent, gradient.

.. exec::docs.actionicon.variant

##### Colors

ActionIcon supports all colors from Mantine's theme.

.. exec::docs.actionicon.colors

##### Radius and Size

Control button width and height with `size` and border-radius with `radius` props respectively. Both props have
predefined values: xs, sm, md, lg, xl. Alternatively, use a number to set radius or size in px.

```python
import dash_mantine_components as dmc

dmc.Group(
    [
        dmc.ActionIcon(size="sm", children=[...]),
        dmc.ActionIcon(radius="xl", children=[...]),
        dmc.ActionIcon(size=20, children=[...]),
    ]
)
```
