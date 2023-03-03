---
name: Menu
section: Overlay
head: Combine a list of secondary actions into single interactive area.
description: Use the Menu and MenuX components to show an interactive menu dropdown with links and buttons.
component: Menu, MenuTarget, MenuDropdown, MenuItem, MenuDivider, MenuLabel
props: false
styles: menu
---

##### Simple Example

Menu is built using MenuItem(s), MenuDropdown and MenuTarget. You can use MenuItem as either a link or a button. Just passing the `href` property will make it a link otherwise it will act as a button.
When MenuItem is used as a button, you can write callbacks on it.

.. exec::docs.menu.simple

##### Menu on Hover

Set `trigger="hover"` to reveal dropdown when user hovers over menu target and dropdown. `closeDelay` and `openDelay` props can be used to control open and close delay in ms.
Note that:

* If you set `closeDelay=0` then menu will close before user will reach dropdown, so set `offset=0` to remove space between target element and dropdown.
* Menu with `trigger="hover"` is not accessible - users that navigate with keyboard will not be able to use it.

```python
import dash_mantine_components as dmc

component = dmc.Menu(trigger="hover", openDelay=100, closeDelay=400, children=[
  # menu target
  # menu dropdown
    # menu items
])
```

##### Transitions

Menu dropdown can be animated with any of the premade transitions.

.. exec::docs.menu.transition

##### Cutom component as Target

.. exec::docs.menu.custom

##### Icons, Right Section, and Colors

Menu component can be customised by changing icons, right section and even colors. Here's an example.

.. exec::docs.menu.colors
