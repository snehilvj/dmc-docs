---
name: Timeline
section: Data Display
head: Display list of events in chronological order
description: Use Timeline to list events in chronological order.
component: Timeline
---


##### Simple Example

This is a basic example showing how you can use timeline.

.. exec::docs.timeline.simple


##### Interactive Demo

Control timeline appearance with the following props:

- `color` – color from theme that should be used to highlight active items, defaults to theme.primaryColor
- `radius` - adjust the radius of the bullet
- `active` – index of current active element, all elements before this index will be highlighted with color
- `lineWidth` – controls line width and bullet border, value is in px
- `bulletSize` – bullet width, height and border-radius in px
- `align` – defines line and bullets position relative to content, also sets text-align


.. exec::docs.timeline.interactive
    :prism: false



##### Gallery

.. gallery::docs.timeline.icons
    :center: false
    :label: Customizing timeline bullets with icons
