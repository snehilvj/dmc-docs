---
name: RadioGroup
description: RadioGroup component gives user radio inputs to allow only one selection from a small set of options.
endpoint: /components/radiogroup
package: dash_mantine_components
category: Inputs
---

.. toc::

### Simple Usage

Use the `value` prop for callbacks.

.. exec::docs.radiogroup.callback

### Customizing Radio

Each Radio item in a RadioGroup can be customized. The Radio component is a wrapper for input type radio.  Use Stack or Group to arrange multiple Radio items

.. exec::docs.radiogroup.interactive
    :code: false

### Color

In a RadioGroup component, the color property can be customized at the individual Radio level.

.. exec::docs.radiogroup.color

### Size

You can set the size of all the Radio items by using the `size` prop in the RadioGroup component.  Use one of xs, sm, md, lg and xl.

.. exec::docs.radiogroup.size

### Group or Stack

In a RadioGroup component, the Radio items can be arranged by using the Group or Stack components.

.. exec::docs.radiogroup.group


### Deselectable RadioGroup

To enable deselecting a radio chip, set `deselectable=True`

.. exec::docs.radiogroup.deselectable


### RadioIndicator component

`RadioIndicator` looks exactly the same as `Radio` component, but it does not have any semantic meaning, it's just a 
visual representation of radio state. You can use it in any place where you need to display radio state without any 
interaction related to the indicator. For example, it is useful in cards based on buttons, trees, etc.

> Note that `RadioIndicator` cannot be focused or selected with keyboard. It is not accessible and should not be used as
a replacement for Radio component.

.. exec::docs.radiogroup.radioindicator


### RadioCard component

RadioCard component can be used as a replacement for `Radio` to build custom cards/buttons/other things that work as
radios. The root element of the component has `role="radio"` attribute, it is accessible by default and supports the
same keyboard interactions as `input[type="radio"]`.


.. exec::docs.radiogroup.radiocard



### RadioCard with RadioGroup

You can use `RadioCard` with `RadioGroup` the same way as `Radio` component.

Note - do not set the `checked` prop in the `RadioIndicator` component otherwise the `RadioIndicator` will not be updated.
This example also shows how to add hover styles

.. exec::docs.radiogroup.radiocardgroup
    :code: false

.. sourcetabs::docs/radiogroup/radiocardgroup.py, assets/radiocard.css
    :defaultExpanded: false
    :withExpandedButton: true



### Styles API

#### Radio Selectors

| Selector       | Static selector              | Description                           |
|---------------|------------------------------|---------------------------------------|
| root          | .mantine-Radio-root          | Root element                         |
| radio         | .mantine-Radio-radio         | Input element (input[type="radio"])  |
| icon          | .mantine-Radio-icon          | Radio icon, used to display checked icon |
| inner         | .mantine-Radio-inner         | Wrapper for icon and input           |
| body          | .mantine-Radio-body          | Input body, contains all other elements |
| labelWrapper  | .mantine-Radio-labelWrapper  | Contains label, description, and error |
| label         | .mantine-Radio-label         | Label element                        |
| description   | .mantine-Radio-description   | Description displayed below the label |
| error         | .mantine-Radio-error         | Error message displayed below the label |

#### Radio CSS Variables

| Selector | Variable           | Description                                |
|----------|-------------------|--------------------------------------------|
| root     | --radio-color     | Controls checked radio background-color   |
|          | --radio-radius    | Controls radio border-radius              |
|          | --radio-size      | Controls radio width and height           |
|          | --radio-icon-color | Controls radio icon color                 |
|          | --radio-icon-size  | Controls radio icon width and height      |

#### Radio Data Attributes

| Selector | Attribute           | Condition         | Value |
|----------|--------------------|------------------|-------|
| radio    | data-error         | `error` prop is set | –     |
| inner    | data-label-position | –                | Value of `labelPosition` prop |

#### RadioGroup Selectors

| Selector    | Static selector               | Description                         |
|------------|------------------------------|-------------------------------------|
| root       | .mantine-RadioGroup-root     | Root element                       |
| label      | .mantine-RadioGroup-label    | Label element                      |
| required   | .mantine-RadioGroup-required | Required asterisk element, rendered inside label |
| description | .mantine-RadioGroup-description | Description element                |
| error      | .mantine-RadioGroup-error    | Error element                      |

#### RadioIndicator Selectors

| Selector   | Static selector                   | Description   |
|------------|----------------------------------|---------------|
| indicator  | .mantine-RadioIndicator-indicator | Root element  |
| icon       | .mantine-RadioIndicator-icon     | Radio icon    |

#### RadioIndicator CSS Variables

| Selector   | Variable           | Description                                |
|------------|-------------------|--------------------------------------------|
| indicator  | --radio-color     | Controls checked radio background-color   |
|            | --radio-radius    | Controls radio border-radius              |
|            | --radio-size      | Controls radio width and height           |
|            | --radio-icon-color | Controls radio icon color                 |
|            | --radio-icon-size  | Controls radio icon width and height      |

#### RadioIndicator Data Attributes

| Selector   | Attribute     | Condition         |
|------------|-------------|------------------|
| indicator  | data-checked | `checked` prop is set |
| indicator  | data-disabled | `disabled` prop is set |

#### RadioCard Selectors

| Selector | Static selector          | Description   |
|----------|--------------------------|---------------|
| card     | .mantine-RadioCard-card  | Root element  |

#### RadioCard CSS Variables

| Selector | Variable      | Description                  |
|----------|-------------|------------------------------|
| card     | --card-radius | Controls card border-radius |

#### RadioCard Data Attributes

| Selector | Attribute       | Condition                  |
|----------|----------------|----------------------------|
| card     | data-checked    | `checked` prop is set      |
| card     | data-with-border | `withBorder` prop is set  |

### Keyword Arguments

#### RadioGroup

.. kwargs::RadioGroup

#### Radio

.. kwargs::Radio


#### RadioIndicator

.. kwargs::RadioIndicator


#### RadioCard

.. kwargs::RadioCard
