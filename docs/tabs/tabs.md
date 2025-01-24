---
name: Tabs
description: Use the Tab and Tabs component to switch between views.
endpoint: /components/tabs
package: dash_mantine_components
category: Navigation
---

.. toc::

### Usage

.. exec::docs.tabs.interactive
    :code: false


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
    orientation="vertical", # or "horizontal"
    variant="default", # or "outline" or "pills"
    value="gallery"
)
```

### Variants

Use the `variant` can be set to `"default"`,  `"outline"` or `"pills"`

.. exec::docs.tabs.variant
    :code: false

### Change colors
To change colors of all tabs, set `color` on `Tabs` component, to change color of the individual tab, set `color`
on `TabsTab`.


.. exec::docs.tabs.color

### Icons on right or left

You can use any dash component as icon and rightSection in dmc.TabsTab component.

.. exec::docs.tabs.icons

.. exec::docs.tabs.section

### Tabs Position

`Tabs` controls position is controlled with `grow` and `justify` properties in TabsList component. If `grow` property 
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

To display tab on the opposite side, set `margin-left` to auto with `ml="auto"` in `TabsTab` component.

.. exec::docs.tabs.right

### Inverted Tabs

To make tabs inverted, place `TabsPanel` components before `TabsList` and add `inverted=True` prop to `Tabs` component.

.. exec::docs.tabs.inverted

### Vertical Tabs placement

To change placement of `TabsList` in vertical orientation, set `placement` prop in `Tabs`.

.. exec::docs.tabs.vertical
    :code: false

### Disabled tabs

Set `disabled=True` prop on `TabsTab` component to disable tab. Disabled tab cannot be activated with mouse or keyboard,
and they will be skipped when user navigates with arrow keys:

.. exec::docs.tabs.disabled

### Activation mode
By default, tabs are activated when user presses arrows keys or Home/End keys. To disable that set
`activateTabWithKeyboard=False` on `Tabs` component.  

This can be useful if the tab content is updated in a long running callback.  Try clicking on a tab to focus, then
navigate to other tabs with arrow keys, or home/end keys:

.. exec::docs.tabs.activation
    :code: false



```python
import dash_mantine_components as dmc

dmc.Tabs(
    activateTabWithKeyboard=False,
    children=[
        # tabs content
    ],    
)
```

### Tab deactivation
By default, active tab cannot be deactivated. To allow that set `allowTabDeactivation=True` on Tabs component:

Try clicking on the active tab to see the deactivated state:


.. exec::docs.tabs.deactivation
    :code: false


### Content As Callback

Attach a callback to the Tabs `value` prop and update a container's `children` property in your callback.

.. exec::docs.tabs.callback

### Content As Tab Children

Instead of displaying the content through a callback, you can embed the content directly as the `children` property in
the Tab component.

.. exec::docs.tabs.content

### Styling the Tabs

Here is an example of styling the tabs using the Styles API:

.. exec::docs.tabs.styles

Put the following in a `.css` file in the `/assets` folder

```css
.dmc-tabs {
  position: relative;
  border: 1px solid light-dark(var(--mantine-color-gray-2), var(--mantine-color-dark-4));
  background-color: light-dark(var(--mantine-color-white), var(--mantine-color-dark-6));

  &:first-of-type {
    border-radius: 4px 0 0 4px;
  }

  &:last-of-type {
    border-radius: 0 4px 4px 0;
  }

  & + & {
    border-left-width: 0;
  }

  &:hover {
    background-color: light-dark(var(--mantine-color-gray-0), var(--mantine-color-dark-5));
  }

  &[data-active] {
    z-index: 1;
    background-color: var(--mantine-color-blue-filled);
    border-color: var(--mantine-color-blue-filled);
    color: var(--mantine-color-white);

    &:hover {
      background-color: var(--mantine-color-blue-filled-hover);
    }
  }
}

```

### Styles API


This component supports [Styles API](/styles-api). With Styles API, you can customize styles of any inner element.
For more information on styling components,  please also refer to the [Mantine Styles](https://mantine.dev/styles/styles-overview/) documentation.

Refer to the Mantine Tabs Style API [interactive demo](https://mantine.dev/core/tabs/#styles-api) for help in identifying each selector.

#### Tabs Selectors


| Selector     | Static selector             | Description                              |
|--------------|------------------------------|------------------------------------------|
| root         | .mantine-Tabs-root           | Root element (Tabs component)            |
| list         | .mantine-Tabs-list           | List of tabs (Tabs.List component)       |
| panel        | .mantine-Tabs-panel          | Panel with tab content (Tabs.Panel component) |
| tab          | .mantine-Tabs-tab            | Tab button (Tabs.Tab component)          |
| tabLabel     | .mantine-Tabs-tabLabel       | Label of Tabs.Tab                        |
| tabSection   | .mantine-Tabs-tabSection     | Left and right sections of Tabs.Tab      |



#### Tabs CSS Variables

| Selector | Variable        | Description                                                  |
|----------|-----------------|--------------------------------------------------------------|
| root     | --tabs-color    | Controls colors of Tabs.Tab, only applicable for `pills` or `default` variant |
|          | --tabs-radius   | Controls Tabs.Tab border-radius                              |



#### Tabs Data Attributes

| Selector          | Attribute          | Condition                                 | Value                        |
|-------------------|--------------------|-------------------------------------------|------------------------------|
| root, tab, list, panel | data-orientation  | –                                         | Value of `orientation` prop |
| root, tab, list   | data-placement     | `orientation` is "vertical" on Tabs component | Value of `placement` prop   |
| tab, list         | data-inverted      | `inverted` prop is set on Tabs component  | –                            |
| list              | data-grow          | `grow` prop is set on Tabs.List component | –                            |
| tabSection        | data-position      | –                                         | Position of the section (left or right) |



### Keyword Arguments

#### Tabs

.. kwargs::Tabs

#### TabsList

.. kwargs::TabsList

#### TabsPanel

.. kwargs::TabsPanel

#### Tab

.. kwargs::TabsTab
