---
name: RollingNumber
description: Animate value changes with rolling digits
endpoint: /components/rolling-number
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::RollingNumber


### Usage

`RollingNumber` animates value changes with rolling digit transitions. Each digit
independently rolls to its new position when the value changes.

.. exec::docs.rollingnumber.usage


### Prefix and suffix

Set `prefix` and `suffix` props to add static text before or after the animated number.
Use `thousandSeparator` to separate thousands and `decimalScale` with `fixedDecimalScale`
to control decimal formatting:


.. exec::docs.rollingnumber.prefix_suffix

### Animation duration

Control animation speed with `animationDuration` prop (in milliseconds, default is `600`).
Use `timingFunction` prop to change the CSS timing function (default is `ease`):


.. exec::docs.rollingnumber.annimation

### Text selection and copying

Selecting and copying `RollingNumber` always produces the value as it is displayed,
for example `$ 1,234.56 USD`. Animated digits are not selectable, text selection
is handled by a transparent copy of the formatted value rendered on top of them.


### Styles API

.. styles_api_text::


#### RollingNumber selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-RollingNumber-root | Root element |
| digit | .mantine-RollingNumber-digit | Wrapper of a single digit, clips the digits column |
| digitColumn | .mantine-RollingNumber-digitColumn | Column of digits inside `digit`, animated on value change |
| char | .mantine-RollingNumber-char | Non-digit character: prefix, suffix, decimal and thousands separators |

#### RollingNumber CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | --rn-duration | Controls animation duration |
| root | --rn-timing-function | Controls animation timing function |

#### RollingNumber data attributes

| Selector | Attribute | Condition | Value |
|----------|-----------|-----------|-------|
| root | data-tabular-numbers | `tabularNumbers` prop is set | - |



### Keyword Arguments
.. style_props_text::

#### RollingNumber

.. kwargs::RollingNumber

