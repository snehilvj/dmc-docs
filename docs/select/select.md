---
name: Select
description: Select enables users to select an option in a dropdown.
endpoint: /components/select
package: dash_mantine_components
category: Combobox
---

.. toc::  
.. llms_copy::Select

> Need users to select multiple items? See `MultiSelect`.  Need users to type their own options? See `TagsInput` or `Autocomplete`

### Made with Combobox

`Select` is built on top of `Combobox` and covers common use cases. If you need more advanced behavior or want to extend
its functionality, you can create your own custom `Select` using `Combobox`.

For working examples and guidance, see this [GitHub repository](https://github.com/AnnMarieW/dmc_custom_components).


### Simple Example

`Select` component allows user to pick one option from the given data. Unlike `Autocomplete`, `Select` does not allow entering custom values.


.. exec::docs.select.simple

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
### autoSelectOnBlur

Set `autoSelectOnBlur=True` to automatically select the highlighted option when the input loses focus. To see this
feature in action: select an option with up/down arrows, then click outside the input:


.. exec::docs.select.autoselectonblur

### Searchable

Set `searchable=True` to allow filtering options by user input.

.. exec::docs.select.searchable


### clearSearchOnFocus

When `clearSearchOnFocus=True` and the `Select` is in searchable mode, the search input will be cleared each time the
field gains focus.  This is useful when you want the user to start with an empty search box each time, without having 
to manually delete the existing text.


.. exec::docs.select.clearsearchonfocus


### Nothing Found

Set the `nothingFoundMessage` prop to display a given message when no options match the search query or there is 
no data available. If the `nothingFoundMessage` prop is not set, the `MultiSelect` dropdown will be hidden.

.. exec::docs.select.nothing_found

### Checked option icon
Set `checkIconPosition` prop to left or right to control position of check icon in active option. To remove the 
check icon, set `withCheckIcon=False`.


.. exec::docs.select.check_option

### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec::docs.select.clearable

### Allow deselect
`allowDeselect` prop determines whether the value should be deselected when user clicks on the selected option. By 
default, `allowDeselect` is True:


.. exec::docs.select.allow_deselect

### Large Data Sets

The best strategy for large data sets is to limit the number of options that are rendered at the same time. You can
do it with limit prop. 

Note that if you use a custom `filter` function, you need to implement your own logic to limit the number of options in filter

Example of `Select` with 100 000 options, 10 options are rendered at the same time:

.. exec::docs.select.large_data_sets


### renderOption

`renderOption` function allows you to customize option rendering.

.. functions_as_props::

.. exec::docs.select.render_option
    :code: false

.. sourcetabs::docs/select/render_option.py, assets/examples-js/render_option_select.js
    :defaultExpanded: true
    :withExpandedButton: true

### Options filtering

By default, `Select` filters options by checking if the option label contains input value. You can change this behavior 
with `filter`. The filter function receives an object with the following properties as a single argument:
 - `options` – array of options or options groups, all options are in `{ value: string; label: string; disabled?: boolean }` format
 - `search` – current search query
 - `limit` – value of limit prop passed to `Select`


.. functions_as_props::

Example of a custom filter function that matches options by words instead of letters sequence:

.. exec::docs.select.option_filter
    :code: false

.. sourcetabs::docs/select/option_filter.py, assets/examples-js/option_filter.js
    :defaultExpanded: true
    :withExpandedButton: true 


### Sort options

By default, options are sorted by their position in the data array. You can change this behavior with `filter` function:

.. functions_as_props::

.. exec::docs.select.option_sort
    :code: false

.. sourcetabs::docs/select/option_sort.py, assets/examples-js/option_sort.js
    :defaultExpanded: true
    :withExpandedButton: true 



### Scrollable dropdown

By default, the options list is wrapped with `ScrollArea.Autosize`. You can control dropdown max-height with 
`maxDropdownHeight` prop if you do not change the default settings.

If you want to use native scrollbars, set `withScrollArea=False`. Note that in this case, you will need to change 
dropdown styles with `Styles API`.


.. exec::docs.select.scrollable



### Grouping Items

.. exec::docs.select.grouping


### Combobox props
You can override `Combobox` props with `comboboxProps`. It is useful when you need to change some of the props that are
not exposed by `Select`, for example `withinPortal`:

```python
dmc.Select(comboboxProps={"withinPortal": False})
```


### Change dropdown z-index


```python
dmc.Select(comboboxProps={"zIndex": 1000})
```

### Inside Popover

To use `Select` inside popover, you need to set `withinPortal=False`:

.. exec::docs.select.popover



### Dropdown open in a callback

.. exec::docs.select.opened

### Dropdown position

By default, the dropdown is displayed below the input if there is enough space; otherwise it is displayed above the
input. You can change this behavior by setting `position` and `middlewares` props, which are passed down to the
underlying `Popover` component.

Example of dropdown that is always displayed above the input:

.. exec::docs.select.dropdown_position

### Dropdown width

To change dropdown width, set `width` prop in `comboboxProps`. By default, dropdown width is equal to the input width.

.. exec::docs.select.dropdown_width


### Dropdown offset

To change dropdown offset, set `offset` prop in `comboboxProps`:  

.. exec::docs.select.dropdown_offset

### Dropdown animation
By default, dropdown animations are disabled. To enable them, you can set `transitionProps`, which will be passed
down to the underlying `Transition` component.

.. exec::docs.select.dropdown_animation

### Dropdown padding

.. exec::docs.select.dropdown_padding


### Dropdown shadow

.. exec::docs.select.dropdown_shadow

### Left and right sections

`Select` supports `leftSection` and `rightSection` props. These sections are rendered with absolute position
inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

- `rightSection`/`leftSection` – component to render on the corresponding side of input
- `rightSectionWidth`/`leftSectionWidth` – controls width of the right section and padding on the corresponding side of the input. By default, it is controlled by component size prop.
- `rightSectionPointerEvents`/`leftSectionPointerEvents` – controls pointer-events property of the section. If you want to render a non-interactive element, set it to none to pass clicks through to the input.

.. exec::docs.select.left_right


### Input Props
`Select` component supports `Input` and Input Wrapper components features and all input element props.
`Select` documentation does not include all features supported by the component – see Input documentation to learn about all available features.

 
.. exec::docs.select.interactive
   :code: false


### Invalid State And Error


Note: Dash adds some css by default which can lead you to see a red box when setting the `required` or `error` 
prop to True. Use the below css snippet to counteract it.

```css
input:invalid {
    outline: none !important;
}
```

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.select.error


### Styles API

.. styles_api_text::

| Name        | Static selector             | Description                                      |
|:------------|:----------------------------|:-------------------------------------------------|
| wrapper     | .mantine-Select-wrapper     | Root element of the Input                        |
| input       | .mantine-Select-input       | Input element                                    |
| section     | .mantine-Select-section     | Left and right sections                          |
| root        | .mantine-Select-root        | Root element                                     |
| label       | .mantine-Select-label       | Label element                                    |
| required    | .mantine-Select-required    | Required asterisk element, rendered inside label |
| description | .mantine-Select-description | Description element                              |
| error       | .mantine-Select-error       | Error element                                    |
| dropdown    | .mantine-Select-dropdown    | Dropdown root element                            |
| options     | .mantine-Select-options     | Options wrapper                                  |
| option      | .mantine-Select-option      | Option                                           |
| empty       | .mantine-Select-empty       | Nothing found message                            |
| group       | .mantine-Select-group       | Options group wrapper                            |
| groupLabel  | .mantine-Select-groupLabel  | Options group label                              |


### Keyword Arguments
.. style_props_text::

#### Select

.. kwargs::Select
