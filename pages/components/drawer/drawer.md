Drawer | Display overlay area at any side of the screen.

### Simple Example

This is a basic example of dmc.Drawer. Set the `opened` property to open the drawer. The drawer can be closed in the
following ways:

* programmatically (using callbacks)
* by clicking on the cross button (if not disabled using `hideCloseButton` prop)
* by clicking outside the drawer area (if not disabled using `noCloseOnClickOutside` prop)
* by pressing the ESC key (if not disabled using `noCloseOnEscape` prop)

> example:components/drawer/_simple.py

### Different Sizes

Set the size of the drawer using the `size` prop.

> example:components/drawer/_sizes.py

### Placement

By default, Drawer will start to appear from the left, but this position can be customized by setting the `position` prop.

> example:components/drawer/_placement.py

> apidoc:Drawer