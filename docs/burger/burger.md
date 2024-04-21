---
name: Burger
description: Open/close navigation button. Use the dmc.Burger component to toggle navigation menus.
endpoint: /components/burger
package: dash_mantine_components
category: Navigation
---

.. toc::

### Simple Example

Burger component renders open/close menu button. If it's burger state is clicked, the `opened` property is set to `True`,
and if it's cross state is clicked, the `opened` property is set to `False`.

.. exec::docs.burger.simple

### Colors

.. exec::docs.burger.color

### Styles API

| Name   | Static selector        | Description                              |
|:-------|:-----------------------|:-----------------------------------------|
| root   | .mantine-Burger-root   | Root element (button)                    |
| burger | .mantine-Burger-burger | Inner element that contains burger lines |

### Keyword Arguments

#### Burger

.. kwargs::Burger
