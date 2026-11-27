---
name: Toggle
description:  A toggleable button with active/inactive states
endpoint: /components/toggle
package: dash_mantine_components
category: Buttons
---

.. toc::
.. llms_copy::Toggle

### Usage

Toggle is a button that can be toggled between active and inactive states.

.. exec::docs.toggle.usage

### Auto contrast


Set `autoContrast` prop to automatically adjust icon color based on the active toggle
background color, for example with `variant="filled"` and light colors.


.. exec::docs.toggle.autocontrast


### Auto width

By default, `Toggle` renders as a square button. Set `autoWidth` to allow
the width to adjust to content.

.. exec::docs.toggle.autowidth


### Configurator

.. exec::docs.toggle.interactive
    :code: false

### Accessibility
`Toggle` renders a button element with aria-pressed attribute that reflects the active state. When using icon-only
toggles, provide an aria-label prop so that screen readers can announce the button purpose.


### Styles API

.. styles_api_text::

#### Toggle Selectors


| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-Toggle-root | Root element |

#### Toggle CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | --toggle-size | Controls toggle `height` and `min-width` |
| root | --toggle-radius | Controls `border-radius` |
| root | --toggle-active-bg | Controls active state `background-color` |
| root | --toggle-active-hover | Controls active state hover `background-color` |
| root | --toggle-active-color | Controls active state text `color` |

#### Toggle data attributes

| Selector | Attribute | Condition | Value |
|----------|-----------|-----------|-------|
| root | data-active | Toggle is in active state | - |
| root | data-disabled | `disabled` prop is set | - |
| root | data-auto-width | `autoWidth` prop is set | - |



### Keyword Arguments
.. style_props_text::

#### Toggle

.. kwargs::Toggle
