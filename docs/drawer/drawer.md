---
name: Drawer
section: Overlay
head: Display overlay area at any side of the screen.
description: Use Drawer component to create collapsible sidebars.
component: Drawer
---

##### Simple Example

This is a basic example of dmc.Drawer. Set the `opened` property to open the drawer. The drawer can be closed in the
following ways:

* programmatically (using callbacks)
* by clicking on the cross button (if not disabled using `hideCloseButton` prop)
* by clicking outside the drawer area (if not disabled using `closeOnClickOutside` prop)
* by pressing the ESC key (if not disabled using `closeOnEscape` prop)

.. exec::docs.drawer.simple

##### Different Sizes

Set the size of the drawer using the `size` prop.

.. exec::docs.drawer.sizes

##### Placement

By default, Drawer will start to appear from the left, but this position can be customized by setting the `position` 
prop.

.. exec::docs.drawer.placement
