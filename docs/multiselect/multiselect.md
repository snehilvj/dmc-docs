---
name: MultiSelect
description: MultiSelect enables users to select multiple options in a dropdown.
endpoint: /components/multiselect
package: dash_mantine_components
category: Combobox
---

.. toc::

### Simple Example

MultiSelect component allows user to pick any number of option from the given data.
I you would like users to be able to enter custom values, see `TagsInput`.

.. exec::docs.multiselect.simple

### Data Format

The data can be provided as either:
* an array of strings - use when label and value are same.
* an array of dicts with `label` and `value` properties.
* an array of dict with `group` and `items` as keys where items are one of the previous two types.

```python
data = ["Pandas", "NumPy", "TensorFlow", "PyTorch"]

# or

data = [
    {"value": "Pandas", "label": "Pandas"},
    {"value": "NumPy", "label": "NumPy"},
    {"value": "TensorFlow", "label": "TensorFlow"},
    {"value": "PyTorch", "label": "PyTorch"},
]

# or

data = [
    {"group": "Data Analysis", "items": ["Pandas", "NumPy"]},
    {"group": "Deep Learning", "items": ["TensorFlow", "Pytorch"]}
]

# or

data = [
    {
        "group": "Data Analysis",
        "items": [
            {"value": "Pandas", "label": "Pandas"},
            {"value": "NumPy", "label": "NumPy"},
        ],
    },
    {
        "group": "Deep Learning",
        "items": [
            {"value": "TensorFlow", "label": "TensorFlow"},
            {"value": "PyTorch", "label": "PyTorch"},
        ],
    },
]
```

### Clearable

Set `clearable` prop to display the clear button in the right section. The button is not displayed when:

- The component does not have a value
- The component is disabled
- The component is read only


.. exec::docs.multiselect.clearable


### Searchable

Set `searchable` prop to allow filtering options by user input.

.. exec::docs.multiselect.searchable


### Nothing Found

Set the `nothingFoundMessage` prop to display a given message when no options match the search query or there is 
no data available. If the `nothingFoundMessage` prop is not set, the `MultiSelect` dropdown will be hidden.

.. exec::docs.multiselect.nothing_found


### Checked option icon
Set `checkIconPosition` prop to left or right to control position of check icon in active option. To remove the 
check icon, set `withCheckIcon=False`.

.. exec::docs.multiselect.check_option

### Checked option icon

Set `checkIconPosition` prop to `left` or `right` to control position of check icon in active option.
To remove the check icon, set `withCheckIcon=False`.

.. exec::docs.multiselect.check


### Max Selected Values

You can limit the number of selected values with `maxValues` prop. This will not allow adding more values
once the limit is reached.

.. exec::docs.multiselect.max-selected

### Hide selected options

To remove selected options from the list of available options, set `hidePickedOptions` prop:

.. exec::docs.multiselect.hide

### Large Data Sets

The best strategy for large data sets is to limit the number of options that are rendered at the same time. You can
do it with limit prop. 

Example of `MultiSelect` with 100 000 options, 10 options are rendered at the same time:

.. exec::docs.multiselect.large_data_sets

### Scrollable dropdown

By default, the options list is wrapped with `ScrollArea.Autosize`. You can control dropdown max-height with 
`maxDropdownHeight` prop if you do not change the default settings.

If you want to use native scrollbars, set `withScrollArea=False`. Note that in this case, you will need to change 
dropdown styles with `Styles API`.


.. exec::docs.multiselect.scrollable

### Grouping

.. exec::docs.multiselect.grouping

### Combobox props
You can override `Combobox` props with `comboboxProps`. It is useful when you need to change some of the props that are
not exposed by `MultiSelect`, for example `withinPortal`:

```python
dmc.MultiSelect(comboboxProps={"withinPortal": False})
```


### Change dropdown z-index


```python
dmc.MultiSelect(comboboxProps={"zIndex": 1000})
```


### Inside Popover

To use MultiSelect inside popover, you need to set `withinPortal=False`:

.. exec::docs.multiselect.popover


### Dropdown open in a callback

.. exec::docs.multiselect.opened

### Dropdown position

By default, the dropdown is displayed below the input if there is enough space; otherwise it is displayed above the
input. You can change this behavior by setting `position` and `middlewares` props, which are passed down to the
underlying `Popover` component.

Example of dropdown that is always displayed above the input:

.. exec::docs.multiselect.dropdown_position

### Dropdown width

To change dropdown width, set `width` prop in `comboboxProps`. By default, dropdown width is equal to the input width.

.. exec::docs.multiselect.dropdown_width


### Dropdown offset

To change dropdown offset, set `offset` prop in `comboboxProps`:  

.. exec::docs.multiselect.dropdown_offset

### Dropdown animation
By default, dropdown animations are disabled. To enable them, you can set `transitionProps`, which will be passed
down to the underlying `Transition` component.

.. exec::docs.multiselect.dropdown_animation

### Dropdown padding

.. exec::docs.multiselect.dropdown_padding


### Dropdown shadow

.. exec::docs.multiselect.dropdown_shadow

### Left and right sections

`MultiSelect` supports `leftSection` and `rightSection` props. These sections are rendered with absolute position
inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

- `rightSection`/`leftSection` – component to render on the corresponding side of input
- `rightSectionWidth`/`leftSectionWidth` – controls width of the right section and padding on the corresponding side of the input. By default, it is controlled by component size prop.
- `rightSectionPointerEvents`/`leftSectionPointerEvents` – controls pointer-events property of the section. If you want to render a non-interactive element, set it to none to pass clicks through to the input.

.. exec::docs.multiselect.left_right



### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.multiselect.error

### Input Props
`MultiSelect` component supports `Input` and Input Wrapper components features and all input element props.
`MultiSelect` documentation does not include all features supported by the component – see Input documentation to learn about all available features.

 
.. exec::docs.multiselect.interactive
   :code: false

### Styles API

| Name        | Static selector                  | Description                                      |
|:------------|:---------------------------------|:-------------------------------------------------|
| wrapper     | .mantine-MultiSelect-wrapper     | Root element of the Input                        |
| input       | .mantine-MultiSelect-input       | Input element                                    |
| section     | .mantine-MultiSelect-section     | Left and right sections                          |
| root        | .mantine-MultiSelect-root        | Root element                                     |
| label       | .mantine-MultiSelect-label       | Label element                                    |
| required    | .mantine-MultiSelect-required    | Required asterisk element, rendered inside label |
| description | .mantine-MultiSelect-description | Description element                              |
| error       | .mantine-MultiSelect-error       | Error element                                    |
| dropdown    | .mantine-MultiSelect-dropdown    | Dropdown root element                            |
| options     | .mantine-MultiSelect-options     | Options wrapper                                  |
| option      | .mantine-MultiSelect-option      | Option                                           |
| empty       | .mantine-MultiSelect-empty       | Nothing found message                            |
| group       | .mantine-MultiSelect-group       | Options group wrapper                            |
| groupLabel  | .mantine-MultiSelect-groupLabel  | Options group label                              |
| pill        | .mantine-MultiSelect-pill        | Value pill                                       |
| inputField  | .mantine-MultiSelect-inputField  | Input field                                      |
| pillsList   | .mantine-MultiSelect-pillsList   | List of pills, also contains input field         |

### Keyword Arguments

#### MultiSelect

.. kwargs::MultiSelect
