---
name: Tabs
section: Navigation
head: Switch between different views.
description: Use the Tab and Tabs component to switch between views.
component: Tabs
---

##### Usage

The dmc.Tabs and dmc.Tab components can be used to create tabbed sections in your app. The dcc.Tab component controls 
the style and value of the individual tab and the dcc.Tabs component holds a collection of dcc.Tab components.

Three variants of Tabs are supported right now, namely, default, pills, and outline. You can also customize the color
of the Tabs in the default variant.

You can also set the orientation of the Tabs using the `orientation` prop.

```python
import dash_mantine_components as dmc

dmc.Tabs(
    color="red",
    orientation="vertical",
    children=[
        dmc.Tab(label="Section 1", children=[]),
        dmc.Tab(label="Section 2", children=[]),
    ]
)
```

.. exec::docs.tabs.interactive
    :prism: false

##### Tabs Position

Tabs' controls position is controlled with `grow` and `position` props. If `grow` property is set to true, controls
will take 100% of available space and `position` property is ignored.

```python
import dash_mantine_components as dmc

dmc.Tabs(
    position="right",
    grow=False,
    children=[
        dmc.Tab(label="Section 1", children=[]),
        dmc.Tab(label="Section 2", children=[]),
    ]
)
```

.. exec::docs.tabs.position
    :prism: false

##### Content As Callback

Attach a callback to the Tabs `value` prop and update a container's `children` property in your callback.

.. exec::docs.tabs.callback

##### Content As Tab Children

Instead of displaying the content through a callback, you can embed the content directly as the `children` property in
the Tab component.

.. exec::docs.tabs.content
