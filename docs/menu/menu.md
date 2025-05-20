---
name: Menu
description: Use the Menu and MenuX components to show an interactive menu dropdown with links and buttons.
endpoint: /components/menu
package: dash_mantine_components
category: Overlay
---

.. toc::

### Simple Example

Menu is built using MenuItem(s), MenuDropdown and MenuTarget. You can use MenuItem as either a link or a button. Just passing the `href` property will make it a link otherwise it will act as a button.
When MenuItem is used as a button, you can write callbacks on it.

.. exec::docs.menu.simple

### Submenus

.. exec::docs.menu.submenus
    :code: false

.. sourcetabs::docs/menu/submenus.py
    :defaultExpanded: false
    :withExpandedButton: true


### Menu on Hover

Set `trigger` to `hover` to reveal dropdown when user hovers over menu target and dropdown. `closeDelay` and `openDelay` props can be used to control open and close delay in ms.
Note that:

* If you set `closeDelay=0` then menu will close before user will reach dropdown, so set `offset=0` to remove space between target element and dropdown.
* Menu with hover trigger is not accessible - users that navigate with keyboard will not be able to use it.

```python
import dash_mantine_components as dmc

component = dmc.Menu(trigger="hover", openDelay=100, closeDelay=400, children=[
  # menu target
  # menu dropdown
    # menu items
])
```

### Menu Target

Any component you specify in dmc.MenuTarget is wrapped by a dmc.Box component under the hood. So adding a margin
to your target component will also move the dropdown away. In order to prevent this, add margin to the wrapper component
using the prop `boxWrapperProps` in dmc.MenuTarget.

### Transitions

Menu dropdown can be animated with any of the ready-made transitions.

.. exec::docs.menu.transition

### Custom component as Target

.. exec::docs.menu.custom

### Icons, Right Section, and Colors

Menu component can be customised by changing icons, right section and even colors. Here's an example.

.. exec::docs.menu.colors

### Styles API

.. styles_api_text::

| Name        | Static selector           | Description                            |
|:------------|:--------------------------|:---------------------------------------|
| dropdown    | .mantine-Menu-dropdown    | Dropdown element                       |
| arrow       | .mantine-Menu-arrow       | Dropdown arrow                         |
| divider     | .mantine-Menu-divider     | `Menu.Divider` root element            |
| label       | .mantine-Menu-label       | `Menu.Label` root element              |
| item        | .mantine-Menu-item        | `Menu.Item` root element               |
| itemLabel   | .mantine-Menu-itemLabel   | Label of `Menu.Item`                   |
| itemSection | .mantine-Menu-itemSection | Left and right sections of `Menu.Item` |

### Keyword Arguments

#### Menu

.. kwargs::Menu

#### MenuTarget

.. kwargs::MenuTarget

#### MenuDropdown

.. kwargs::MenuDropdown

#### MenuItem

.. kwargs::MenuItem

#### MenuDivider

.. kwargs::MenuDivider

#### MenuLabel

.. kwargs::MenuLabel
