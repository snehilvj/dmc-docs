---
name: Text
section: Typography
head: Display text and links with theme styles.
description: Use the Text component to display text and links with Mantine's theme styles.
component: Text
---

##### Usage

.. exec-block::docs.text.simple

##### Dimmed Text

Text supports special dimmed value in `color` prop. It sets color to theme.colors.dark[2] in dark theme and to 
theme.colors.gray[6] in light.

.. exec-block::docs.text.dimmed

##### Gradient

To use gradient as text color, set `variant` to gradient, and `gradient` to
{ "from": "color-from", "to": "color-to", "deg": 135 }, where:

* color-from and color-to are colors from theme.colors
* deg is linear gradient deg

.. exec-block::docs.text.gradient


