---
name: HoverCard
description: Use HoverCard component to show more information in a popover.
endpoint: /components/hovercard
package: dash_mantine_components
category: Overlay
---

.. toc::
.. llms_copy::HoverCard

### Simple Example

.. exec::docs.hovercard.simple

### Delays

Set open and close delays in ms with `openDelay` and `closeDelay` properties.

.. exec::docs.hovercard.delay

### With Interactive elements

HoverCard is displayed only when mouse is over target element or dropdown, you can use anchors and buttons within dropdowns, using inputs is not recommended.

.. exec::docs.hovercard.interactive

### HoverCard Target

Any component you specify in dmc.HoverCardTarget is wrapped by a dmc.Box component under the hood. So adding a margin
to your target component will also move the dropdown away. In order to prevent this, add margin to the wrapper component
using the prop `boxWrapperProps` in dmc.HoverCardTarget.

### Styles API

.. styles_api_text::

| Name     | Static selector             | Description      |
|:---------|:----------------------------|:-----------------|
| dropdown | .mantine-HoverCard-dropdown | Dropdown element |
| arrow    | .mantine-HoverCard-arrow    | Dropdown arrow   |


### Keyword Arguments
.. style_props_text::

#### HoverCard

.. kwargs::HoverCard

#### HoverCardDropdown

.. kwargs::HoverCardDropdown

#### HoverCardTarget

.. kwargs::HoverCardTarget
