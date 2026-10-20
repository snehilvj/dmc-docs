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

### Interactive dropdown
By default, the dropdown is closed as soon as the pointer leaves the target: if there is a gap between the target and
the dropdown, or if the pointer travels diagonally over unrelated elements, the dropdown may close before the pointer reaches it.

Set the `interactive` prop to keep the dropdown open while the pointer travels toward it. It is required by WCAG 1.4.13
if the dropdown contains interactive content. Note that an interactive dropdown intercepts pointer events of the content it overlaps:


.. exec::docs.hovercard.interactive_dropdown

### With Interactive elements

HoverCard is displayed only when mouse is over target element or dropdown, you can use anchors and buttons within dropdowns, using inputs is not recommended.

.. exec::docs.hovercard.interactive



### Activation events

The `events` prop controls which interactions open the dropdown. Unspecified fields retain their default values. For
example, `events={"focus": False}` disables focus activation while leaving hover activation enabled.

| Field | Default | Description |
|---|---|---|
| `hover` | `True` | Opens the dropdown when the target is hovered with a mouse. |
| `focus` | `True` | Opens the dropdown when the target receives keyboard focus. |
| `touch` | `False` | Opens the dropdown when the target is tapped on a touch device. Requires `hover=True`. |

Focus activation follows [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/:focus-visible) semantics.
The dropdown opens when the target receives keyboard focus, but not when it receives focus from a mouse click.

`touch` is disabled by default because touch devices do not support hover. Enabling it makes the first tap open the
dropdown instead of activating the target. Enable it only when the target has no separate tap action. `touch` extends
hover activation and has no effect when `hover=False`.

.. exec::docs.hovercard.activation

### Keyboard interactions

| Key      | Description                                                                    |
| -------- | ------------------------------------------------------------------------------ |
| `Tab`    | Moves focus to the target and opens the dropdown if `events.focus` is enabled. |
| `Escape` | Closes the dropdown. This behavior can be disabled with `closeOnEscape=False`. |

The dropdown also closes when the user presses outside the target and dropdown. Set `closeOnClickOutside=False` to
disable this behavior. `clickOutsideEvents` is not supported by `HoverCard`; outside presses are always detected using
the `pointerdown` event.

.. exec::docs.hovercard.keyboard


### HoverCard Target

Any component you specify in `HoverCardTarget` is wrapped by a `Box` component under the hood. So adding a margin
to your target component will also move the dropdown away. In order to prevent this, add margin to the wrapper component
using the prop `boxWrapperProps` in `HoverCardTarget`.


### Accessibility limitiations

The dropdown is rendered in a portal at the end of `document.body`, it is not a part of the tab order of the page. Keyboard
users can open, read and dismiss the dropdown, but cannot move focus into it – links and buttons inside the dropdown are
not reachable with the keyboard.

If the dropdown contains interactive content, that content must also be available elsewhere on the page. Do not use the
`trapFocus` prop to work around this limitation: focus cannot be moved into the dropdown in the first place, and trapping
focus in a hover-triggered element strands keyboard users.

With `withinPortal=False` the dropdown is rendered next to the target and focus can be moved into it with `Tab`, but
moving focus out of the dropdown with `Tab` does not close it – the dropdown is closed with `Escape`, with a press outside
or when the pointer leaves the target.

Hover and focus activations do not coordinate: if the pointer leaves the target while the target is focused with the
keyboard, the dropdown is closed after `closeDelay` and is not reopened until the target is blurred and focused again.

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
