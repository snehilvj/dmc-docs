---
name: Tabs
section: Navigation
head: Switch between different views.
description: Use the Tab and Tabs component to switch between views.
component: Tabs, TabsList, TabsPanel, Tab
---

##### Usage

The dmc.Tabs and its associated components can be used to create tabbed sections in your app.
You can set the orientation of the Tabs using the `orientation` prop.

```python
import dash_mantine_components as dmc

dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab("Gallery", value="gallery"),
                dmc.Tab("Messages", value="messages"),
                dmc.Tab("Settings", value="settings"),
            ]
        ),
        dmc.TabsPanel("Gallery tab content", value="gallery"),
        dmc.TabsPanel("Messages tab content", value="messages"),
        dmc.TabsPanel("Settings tab content", value="settings"),
    ],
    color="red",
    orientation="vertical",
)
```

.. exec::docs.tabs.interactive
    :prism: false

##### Icons and Right Section

You can use any dash component as icon and rightSection in dmc.Tab component.

.. exec::docs.tabs.icons

.. exec::docs.tabs.section

##### Tabs Position

Tabs' controls position is controlled with `grow` and `position` properties in TabsList component. If `grow` property 
is set to true, controls will take 100% of available space and `position` property is ignored.

```python
import dash_mantine_components as dmc

dmc.Tabs(
    children=[
        dmc.TabsList(
            position="right",
            grow=False,
            children=[...],
        )
        # tabs panel below
    ]
)
```

.. exec::docs.tabs.position
    :prism: false

##### Separated Tabs

To display tab on the opposite side, set margin-left to auto with ml="auto" in dmc.Tab component.

.. exec::docs.tabs.right

##### Inverted Tabs

To make tabs inverted, place Tabs.Panel components before Tabs.List and add inverted prop to Tabs component.

.. exec::docs.tabs.inverted

##### Vertical Tabs placement

To change placement of dmc.TabsList in vertical orientation, set `placement` prop in dmc.Tabs.

.. exec::docs.tabs.vertical
    :prism: false

##### Content As Callback

Attach a callback to the Tabs `value` prop and update a container's `children` property in your callback.

.. exec::docs.tabs.callback

##### Content As Tab Children

Instead of displaying the content through a callback, you can embed the content directly as the `children` property in
the Tab component.

.. exec::docs.tabs.content
