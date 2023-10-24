---
name: ActionIcon
description: Use this component as an alternative to buttons when you just want to use an icon.
endpoint: /components/actionicon
package: dash_mantine_components
---

.. toc::

### Introduction

.. exec::docs.actionicon.interactive
    :code: false

### Usage

ActionIcon component is an alternative to [Button](/components/button) component. It can be customized with Mantine styles and used with its
`n_clicks` property.

.. exec::docs.actionicon.simple

### Children

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

### Variants

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ActionIcon(
    DashIconify(icon="clarity:settings-line"), color="blue", variant="subtle"
)
```

.. exec::docs.actionicon.variant
    :code: false

### Colors

```python
import dash_mantine_components as dmc
from dash_iconify import DashIconify

dmc.ActionIcon(
    DashIconify(icon="icomoon-free:sun"),
    variant="outline",
    color="orange",
)
```

.. exec::docs.actionicon.colors
    :code: false

### Radius and Size

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

### Keyword Arguments

#### ActionIcon

.. kwargs::ActionIcon
