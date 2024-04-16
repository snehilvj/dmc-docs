---
name: HoverCard
description: Use HoverCard component to show more information in a popover.
endpoint: /components/hovercard
package: dash_mantine_components
---

.. toc::

### Simple Example

.. exec::docs.hovercard.simple

### Delays

Set open and close delays in ms with `openDelay` and `closeDelay` properties.

.. exec::docs.hovercard.delay

### With Interactive elements

HoverCard is displayed only when mouse is over target element or dropdown, you can use anchors and buttons within dropdowns, using inputs is not recommended.

.. exec::docs.hovercard.interactive

### Styles API

| Name     | Static selector             | Description      |
|:---------|:----------------------------|:-----------------|
| dropdown | .mantine-HoverCard-dropdown | Dropdown element |
| arrow    | .mantine-HoverCard-arrow    | Dropdown arrow   |

### Keyword Arguments

#### HoverCard

.. kwargs::HoverCard

#### HoverCardDropdown

.. kwargs::HoverCardDropdown

#### HoverCardTarget

.. kwargs::HoverCardTarget
