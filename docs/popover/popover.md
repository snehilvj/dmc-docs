---
name: Popover
description: Display popover section relative to given target element.
endpoint: /components/popover
package: dash_mantine_components
category: Overlay
---

.. toc::

### Simple Example

.. exec::docs.popover.simple

### Popover Target

Any component you specify in dmc.PopoverTarget is wrapped by a dmc.Box component under the hood. So adding a margin
to your target component will also move the dropdown away. In order to prevent this, add margin to the wrapper component
using the prop `boxWrapperProps` in dmc.PopoverTarget.

### Focus Trap

If you need to use any interactive elements within Popover, set `trapFocus` prop:

.. exec::docs.popover.focustrap

### Inline elements

Enable inline middleware to use Popover with inline elements.

.. exec::docs.popover.inline


### Same width

Set w="target" prop to make Popover dropdown take the same width as target element.
.. exec::docs.popover.same-width

### With overlay
Set `withOverlay` prop to add overlay behind the dropdown. You can pass additional configuration to `Overlay` component with `overlayProps` prop:

.. exec::docs.popover.overlay

### Hide detached

Use `hideDetached` prop to configure how the dropdown behaves when the target element is hidden with styles 
(`display: none, visibility: hidden,` etc.), removed from the DOM, or when the target element is scrolled out of the viewport.

By default, `hideDetached` is enabled – the dropdown is hidden with the target element. You can change this behavior
with `hideDetached=False`. To see the difference, try to scroll the root element of the following demo:


.. exec::docs.popover.hidedetached

### Click outside
By default, `Popover` closes when you click outside of the dropdown. To disable this behavior, set `closeOnClickOutside=False`.

You can configure events that are used for click outside detection with `clickOutsideEvents` prop. By default, `Popover`
listens to `mousedown` and `touchstart` events. You can change it to any other events, for example, `mouseup` and `touchend`:


.. exec::docs.popover.clickoutside

### Styles API

.. styles_api_text::

#### Popover Selectors

| Selector  | Static selector             | Description          |
|-----------|------------------------------|----------------------|
| dropdown  | .mantine-Popover-dropdown    | Dropdown element     |
| arrow     | .mantine-Popover-arrow       | Dropdown arrow       |
| overlay   | .mantine-Popover-overlay     | Overlay element      |


#### Popover CSS Variables

| Selector  | Variable           | Description                    |
|-----------|--------------------|--------------------------------|
| dropdown  | --popover-radius   | Controls dropdown border-radius |
|           | --popover-shadow   | Controls dropdown box-shadow    |


#### Popover Data Attributes

| Selector  | Attribute       | Value                             |
|-----------|-----------------|-----------------------------------|
| dropdown  | data-position   | Value of floating UI dropdown position |


### Keyword Arguments

#### Popover

.. kwargs::Popover

#### PopoverTarget

.. kwargs::PopoverTarget

#### PopoverDropdown

.. kwargs::PopoverDropdown
