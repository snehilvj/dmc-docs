---
name: Drawer
description: Use Drawer component to create collapsible sidebars.
endpoint: /components/drawer
package: dash_mantine_components
category: Overlay
---

.. toc::

### Simple Example

This is a basic example of dmc.Drawer. Set the `opened` property to open the drawer. The drawer can be controlled in following ways:

* programmatically (using callbacks)
* by clicking on the cross button (if not disabled using `withCloseButton` prop)
* by clicking outside the drawer area (if not disabled using `closeOnClickOutside` prop)
* by pressing the ESC key (if not disabled using `closeOnEscape` prop)

.. exec::docs.drawer.simple

### Different Sizes

Set the size of the drawer using the `size` prop.

.. exec::docs.drawer.sizes

### Placement

By default, Drawer will start to appear from the left, but this position can be customized by setting the `position` 
prop.

.. exec::docs.drawer.placement

### Transition

You can customize transition, timing function and duration for Drawer transition.

.. exec::docs.drawer.transition


### Drawer Stack

Use `DrawerStack` component to render multiple drawers at the same time. `DrawerStack` keeps track of opened drawers, 
manages `z-index` values, focus trapping and `closeOnEscape` behavior.

#### Differences from using multiple Drawer components:

- `DrawerStack` children must be `ManagedDrawer` components
- `DrawerStack` manages `z-index` values – drawers that are opened later will always have higher `z-index` value disregarding their order in the DOM
- `DrawerStack` disables focus trap and `Escape` key handling for all drawers except the one that is currently opened
- Drawers that are not currently visible are present in the DOM but are hidden with `opacity: 0` and `pointer-events: none`
- Only one overlay is rendered at a time


.. exec::docs.drawer.drawerstack



### Styles API

.. styles_api_text::

#### Drawer Selectors

| Selector  | Static selector             | Description                                                             |
| --------- | --------------------------- | ----------------------------------------------------------------------- |
| `root`    | `.mantine-Drawer-root`       | Root element                                                            |
| `inner`   | `.mantine-Drawer-inner`      | Element used to center modal, has fixed position, takes entire screen    |
| `content` | `.mantine-Drawer-content`    | Drawer.Content root element                                              |
| `header`  | `.mantine-Drawer-header`     | Contains title and close button                                          |
| `overlay` | `.mantine-Drawer-overlay`    | Overlay displayed under the Drawer.Content                               |
| `title`   | `.mantine-Drawer-title`      | Drawer title (`h2` tag), displayed in the header                         |
| `body`    | `.mantine-Drawer-body`       | Drawer body, displayed after header                                      |
| `close`   | `.mantine-Drawer-close`      | Close button                                                            |



#### Drawer CSS variables


| Selector | Variable          | Description                              |
|----------|-------------------|------------------------------------------|
| root     | --drawer-offset    | Controls margin of Drawer.Content        |
|          | --drawer-size      | Controls width of Drawer.Content         |
|          | --drawer-flex      | Controls flex property of Drawer.Content |
|          | --drawer-align     | Controls align-items property of Drawer.Content |
|          | --drawer-justify   | Controls justify-content property of Drawer.Content |
|          | --drawer-height    | Controls height property of Drawer.Content |


### Keyword Arguments

#### Drawer

.. kwargs::Drawer


#### DrawerStack

.. kwargs::DrawerStack

#### ManagedDrawer

> Note:  ManagedDrawer is for use in the DrawerStack component. id is required.  open/closed state is controlled by DrawerStack.

.. kwargs::ManagedDrawer
