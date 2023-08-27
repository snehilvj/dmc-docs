---
name: Drawer
description: Use Drawer component to create collapsible sidebars.
endpoint: /components/drawer
package: dash_mantine_components
---

.. toc::

### Simple Example

This is a basic example of dmc.Drawer. Set the `opened` property to open the drawer. The drawer can be closed in the
following ways:

* programmatically (using callbacks)
* by clicking on the cross button (if not disabled using `hideCloseButton` prop)
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

### Styles API

| Name    | Static selector         | Description                                                              |
|:--------|:------------------------|:-------------------------------------------------------------------------|
| root    | .mantine-Drawer-root    | Root element                                                             |
| inner   | .mantine-Drawer-inner   | Element used to position drawer, has fixed position, takes entire screen |
| content | .mantine-Drawer-content | Drawer.Content root element                                              |
| header  | .mantine-Drawer-header  | Contains title and close button                                          |
| overlay | .mantine-Drawer-overlay | Overlay displayed under the Drawer.Content                               |
| title   | .mantine-Drawer-title   | Drawer title (h2 tag), displayed in header                               |
| body    | .mantine-Drawer-body    | Drawer body, displayed after header                                      |
| close   | .mantine-Drawer-close   | Close button                                                             |

### Keyword Arguments

#### Drawer

.. kwargs::Drawer
