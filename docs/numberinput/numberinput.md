---
name: NumberInput
description: Use NumberInput to provide a field for entering numbers in your app with ability to set min, max and step.
endpoint: /components/numberinput
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::NumberInput

### Introduction

.. exec::docs.numberinput.interactive
    :code: false


### Value Type

The `value` prop in `NumberInput` can be either a string or a number. Generally, if the `value` can be represented as 
a number (e.g., 55, 1.28, -100), it will be treated as a number. However, there are specific cases where the value 
cannot be represented as a number and is instead treated as a string:

 - Empty State: An empty state is represented as an empty string (`''`). **To clear the value in a callback, use `''` instead of `None`.**
- Exceeding Safe Integer Limits: If the number is larger than [Number.MAX_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER) 
or smaller than [Number.MIN_SAFE_INTEGER](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MIN_SAFE_INTEGER),
it will be represented as a string (e.g., '90071992547409910').
- Multiple Zeros: Numbers that consist only of zeros or have trailing zeros are represented as strings (e.g., '0.', '0.0', '-0.00', etc.).


### min and max

Set `min` and `max` props to limit the input value:


.. exec::docs.numberinput.minmax

### Clamp behavior
By default, the `value` is clamped when the input is blurred. If you set `clampBehavior="strict"`, it will not be
possible to enter value outside of min/max range. Note that this option may cause issues if you have tight
`min` and `max`, for example `min=10` and `max=20`. If you need to disable value clamping entirely, set `clampBehavior="none"`.

.. exec::docs.numberinput.clamp

### Prefix and suffix
Set `prefix` and `suffix` props to add given string to the start or end of the input value:


.. exec::docs.numberinput.prefix_suffix

### Negative numbers
By default, negative numbers are allowed. Set `allowNegative=False` to allow only positive numbers.

.. exec::docs.numberinput.negative


### Decimal numbers
By default, decimal numbers are allowed. Set `allowDecimal=False` to allow only integers.

.. exec::docs.numberinput.decimal_numbers

### Decimal scale
`decimalScale` controls how many decimal places are allowed:

.. exec::docs.numberinput.decimal_scale

### Fixed decimal scale
Set `fixedDecimalScale=True` to always display fixed number of decimal places:


.. exec::docs.numberinput.fixed_decimal_scale

### Decimal separator
Set `decimalSeparator` to change decimal separator character:

.. exec::docs.numberinput.decimal_separator


### Thousand separator
Set `thousandSeparator` prop to separate thousands with a character. You can control
grouping logic with `thousandsGroupStyle`, it accepts: `thousand`, `lakh`, `wan`, `none` values.

.. exec::docs.numberinput.thousand_separator



### Left and right sections

You can use DashIconify to add icon to the NumberInput.

`NumberInput` supports `leftSection` and `rightSection` props. These sections are rendered with absolute position 
inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

- `rightSection/leftSection` – components to render on the corresponding side of input
- `rightSectionWidth/leftSectionWidth` – controls width of the right section and padding on the corresponding side of the input. By default, it is controlled by component size prop.
- `rightSectionPointerEvents/leftSectionPointerEvents` – controls pointer-events property of the section. If you want to render a non-interactive element, set it to none to pass clicks through to the input.

.. exec::docs.numberinput.icon


### Increment/decrement on hold

Set `stepHoldDelay` and `stepHoldInterval` props to define behavior when increment/decrement controls are clicked and 
held.

.. exec::docs.numberinput.hold


### Remove controls

Controls are not rendered in these cases:

- `hideControls` prop is set to `True`
- Input is disabled
- `variant` prop is set to "unstyled"

.. exec::docs.numberinput.controls

### Disabled state

.. exec::docs.numberinput.disabled

### Styles API

.. styles_api_text::

#### NumberInput Selectors

| Selector    | Static selector                | Description                                      |
|-------------|--------------------------------|--------------------------------------------------|
| wrapper     | .mantine-NumberInput-wrapper   | Root element of the Input                        |
| input       | .mantine-NumberInput-input     | Input element                                    |
| section     | .mantine-NumberInput-section   | Left and right sections                          |
| root        | .mantine-NumberInput-root      | Root element                                     |
| label       | .mantine-NumberInput-label     | Label element                                    |
| required    | .mantine-NumberInput-required  | Required asterisk element, rendered inside label |
| description | .mantine-NumberInput-description | Description element                              |
| error       | .mantine-NumberInput-error     | Error element                                    |
| controls    | .mantine-NumberInput-controls  | Increment and decrement buttons wrapper          |
| control     | .mantine-NumberInput-control   | Increment and decrement buttons                  |

#### NumberInput CSS Variables

| Selector  | Variable            | Description                                 |
|-----------|----------------------|---------------------------------------------|
| controls  | --ni-chevron-size    | Controls width and height of the chevron icon |

#### NumberInput Data Attributes

| Selector | Attribute       | Value                               |
|----------|------------------|-------------------------------------|
| control  | data-direction   | "up" or "down" depending on control |



### Keyword Arguments
.. style_props_text::

#### NumberInput

.. kwargs::NumberInput
