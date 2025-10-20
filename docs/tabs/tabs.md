---
name: Tabs
description: Use the Tab and Tabs component to switch between views.
endpoint: /components/tabs
package: dash_mantine_components
category: Navigation
---

.. toc::
.. llms_copy::Tabs

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
    color="red", # default is blue
    orientation="horizontal", # or "vertical"
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

`Tabs` controls position is controlled with `grow` and `justify` properties in `TabsList` component. If `grow` property 
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

#### With Props  

This example demonstrates how to style tabs using only props, without requiring additional CSS files:  

- **Variant**: Sets `variant="pills"` to make the tabs resemble buttons.  
- **Grow Prop**: Uses the `grow` prop on the `TabsList` component, causing the tabs to expand and fill the full width of the viewport.  
- **Border**: Adds a border around the tabs with the `bd` prop. For more details, see the [Style Props](/style-props) section.  
- **Border Color**: Sets the border color using the Mantine CSS variable `var(--mantine-color-default-border)`, ensuring a border color that works well in both light and dark modes. See the [Colors](/colors) section for more details.  
- **Active Tab Color**: Sets the active tab color with `color="green.3"`. This specifies a lighter shade of a built-in color. Mantine’s color palette includes 10 shades for each color, indexed from 0 (lightest) to 9 (darkest). Learn more in the [Colors](/colors) section.  
- **Auto Contrast**: Enables `autoContrast=True` to automatically adjust the text color for better readability when using lighter or darker background colors. Additional details can be found in the [Colors](/colors) section.  

.. exec::docs.tabs.styleprops


#### With Styles API  

This example demonstrates styling tabs using the Styles API, allowing for precise control over the appearance of each element in the tabs component. For more information, see the Styles API section below.  

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

.. styles_api_text::

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
.. style_props_text::

#### Tabs

.. kwargs::Tabs

#### TabsList

.. kwargs::TabsList

#### TabsPanel

.. kwargs::TabsPanel

#### Tab

.. kwargs::TabsTab
