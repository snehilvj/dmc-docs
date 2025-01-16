---
name: Tabs
description: Use the Tab and Tabs component to switch between views.
endpoint: /components/tabs
package: dash_mantine_components
category: Navigation
---

.. toc::

### Usage

The dmc.Tabs and its associated components can be used to create tabbed sections in your app.
You can set the orientation of the Tabs using the `orientation` prop.

```python
import dash_mantine_components as dmc

dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.TabsTab("Gallery", value="gallery"),
                dmc.TabsTab("Messages", value="messages"),
                dmc.TabsTab("Settings", value="settings"),
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
    :code: false

### Icons and Right Section

You can use any dash component as icon and rightSection in dmc.TabsTab component.

.. exec::docs.tabs.icons

.. exec::docs.tabs.section

### Tabs Position

Tabs' controls position is controlled with `grow` and `justify` properties in TabsList component. If `grow` property 
is set to `True`, controls will take 100% of available space and `justify` property is ignored.

```python
import dash_mantine_components as dmc

dmc.Tabs(
    children=[
        dmc.TabsList(
            justify="right",
            grow=False,
            children=[...],
        )
        # tabs panel below
    ]
)
```

.. exec::docs.tabs.position
    :code: false

### Separated Tabs

To display tab on the opposite side, set margin-left to auto with ml="auto" in dmc.TabsTab component.

.. exec::docs.tabs.right

### Inverted Tabs

To make tabs inverted, place Tabs.Panel components before Tabs.List and add inverted prop to Tabs component.

.. exec::docs.tabs.inverted

### Vertical Tabs placement

To change placement of dmc.TabsList in vertical orientation, set `placement` prop in dmc.Tabs.

.. exec::docs.tabs.vertical
    :code: false

### Content As Callback

Attach a callback to the Tabs `value` prop and update a container's `children` property in your callback.

.. exec::docs.tabs.callback

### Content As Tab Children

Instead of displaying the content through a callback, you can embed the content directly as the `children` property in
the Tab component.

.. exec::docs.tabs.content

### Styles API

| Name       | Static selector          | Description                                     |
|:-----------|:-------------------------|:------------------------------------------------|
| root       | .mantine-Tabs-root       | Root element (`Tabs` component)                 |
| list       | .mantine-Tabs-list       | List of tabs (`Tabs.List` component)            |
| panel      | .mantine-Tabs-panel      | Panel with tab content (`Tabs.Panel` component) |
| tab        | .mantine-Tabs-tab        | Tab button (`Tabs.Tab` component)               |
| tabLabel   | .mantine-Tabs-tabLabel   | Label of `Tabs.Tab`                             |
| tabSection | .mantine-Tabs-tabSection | Left and right sections of `Tabs.Tab`           |

### Keyword Arguments

#### Tabs

.. kwargs::Tabs

#### TabsList

.. kwargs::TabsList

#### TabsPanel

.. kwargs::TabsPanel

#### Tab

.. kwargs::TabsTab
