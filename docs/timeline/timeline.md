---
name: Timeline
section: Data Display
head: Display list of events in chronological order.
description: Use the Timeline and TimelineItem components to display a list of events in chronological order.
component: Timeline, TimelineItem
styles: timeline
---

##### Interactive Demo

.. exec::docs.timeline.interactive
    :prism: false

##### Usage

Control timeline appearance with the following props:

- `active` - index of current active element, all elements before this index will be highlighted with color
- `color` - color from theme that should be used to highlight active items, defaults to theme.primaryColor
- `lineWidth` - controls line width and bullet border, value is in px
- `bulletSize` - bullet width, height and border-radius in px
- `align` - defines line and bullets position relative to content, also sets text-align

.. exec::docs.timeline.simple
    :center: true
