---
name: Spoiler
section: Data Display
head: Hide long sections of content under spoiler.
description: Use the Spoiler component to hide long sections of content.
component: Spoiler
---

##### Simple Example

Use Spoiler to hide long sections of content. Pass `maxHeight` prop to control the point at which content will be
hidden under the spoiler and control to show/hide extra appears. If content height is less than `maxHeight`, spoiler
will just render children.

Props `hideLabel` and `showLabel` are required - they are used as spoiler toggle button label in corresponding state.

.. exec-block::docs.spoiler.simple
