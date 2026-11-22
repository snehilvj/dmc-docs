---
name: MaskInput
description: Input with mask pattern for formatted text entry
endpoint: /components/maskinput
package: dash_mantine_components
category: Inputs
---

.. toc::
.. llms_copy::MaskInput


### Basic Usage


`MaskInput` is an input component that guides users to enter text in a specific format, such as a phone number, date,
or credit card number. The `mask` prop defines the format, including editable characters and fixed separators.

See the [Mask Pattern Syntax](#mask-pattern-syntax) section below for more details.


.. exec::docs.maskinput.usage


`MaskInput` supports mask options and standard input props, such as `label`, `description`, and `error`.

.. exec::docs.maskinput.interactive
    :code: false


### Dynamic Masks

Use the `modify` option to change the mask based on the current input value. This example switches between standard and
American Express credit card formats.

.. functions_as_props::

.. exec::docs.maskinput.dynamic_mask
    :code: false

.. sourcetabs::docs/maskinput/dynamic_mask.py, assets/examples-js/mask-creditcard.js
    :defaultExpanded: true
    :withExpandedButton: true


### Custom Tokens

Use the `tokens` prop to define custom characters in the mask. Each token maps to a regex pattern provided as a string.

DMC converts these strings to JavaScript `RegExp` objects in the browser.

.. exec::docs.maskinput.custom_tokens


### Transforming Input

Use the `transform` prop to convert each character before validation. This example automatically converts input to
uppercase, allowing lowercase letters to match the `A` token.

.. functions_as_props::

.. exec::docs.maskinput.transform
    :code: false

.. sourcetabs::docs/maskinput/transform.py, assets/examples-js/uppercase.js
    :defaultExpanded: true
    :withExpandedButton: true

### Mask List format

For more control over the characters accepted at each position, use the list format for `mask`. Each item can be a string
literal or a dictionary with a key of `regex` and value containing a regular expression pattern. This is useful for 
defining formats that cannot be expressed with the built-in mask tokens.

### Time (HH:MM)


.. exec::docs.maskinput.mask_list


### value props

`MaskInput` exposes the following props:

- `value`: The raw, unmasked value.
- `maskedValue`: Read-only. The formatted text displayed in the input.
- `complete`: Indicates whether all required mask slots have been filled. (Read-only)

.. exec::docs.maskinput.value


### Validation and Input Feedback

Use `complete` to determine whether the required mask slots have been filled.

The `error` and `success` props display validation feedback and apply the corresponding input styles.

.. exec::docs.maskinput.input_validation

You can also use `n_submit` and `n_blur` to trigger validation when the user presses Enter or leaves the input.

.. exec::docs.maskinput.input_validation_2


### Disabled State

Set `disabled=True` to prevent the user from editing the input.

.. exec::docs.maskinput.disabled


### Mask Pattern Syntax

Each character in the mask string is either a token, which defines an editable slot, or a literal, which is inserted automatically.

#### Built-in Tokens

- `9` – Any single digit (`[0-9]`)
- `a` – Any single letter (`[A-Za-z]`)
- `A` – Any uppercase letter (`[A-Z]`)
- `*` – Any alphanumeric character (`[A-Za-z0-9]`)
- `#` – A digit or sign (`[-+0-9]`)

#### Optional Slots

Append `?` after the last required character to make the remaining slots optional.

```python
dmc.MaskInput(mask="(999) 999-9999? x9999")  # Optional extension
```

#### Escaping

Prefix a token character with `\` to treat it as a literal:

```python
dmc.MaskInput(mask=r"\A999")  # "A" is literal, not a token
```


### Styles API

.. styles_api_text::


| Selector | Static selector | Description |
|----------|----------------|-------------|
| wrapper | .mantine-MaskInput-wrapper | Root element of the Input |
| input | .mantine-MaskInput-input | Input element |
| section | .mantine-MaskInput-section | Left and right sections |
| bottomSection | .mantine-MaskInput-bottomSection | Bottom section element, rendered inside the input border at the bottom |
| root | .mantine-MaskInput-root | Root element |
| label | .mantine-MaskInput-label | Label element |
| required | .mantine-MaskInput-required | Required asterisk element, rendered inside label |
| description | .mantine-MaskInput-description | Description element |
| error | .mantine-MaskInput-error | Error element |
| success | .mantine-MaskInput-success | Success element |

### Keyword Arguments
.. style_props_text::

#### MaskInput

.. kwargs::MaskInput
