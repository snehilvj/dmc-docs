---
name: Autocomplete
description: Autocomplete user input with any list of options.
endpoint: /components/autocomplete
package: dash_mantine_components
category: Combobox
---

.. toc::  

> Need users to select multiple items? See `MultiSelect`.  Need users to type their own options? See `TagsInput`.


Use `Autocomplete` component in the following cases:

- You want to allow user to enter any value
- You want to display suggestions to the user based on the input value
- You want to preserve user input on blur if option was not selected from the dropdown
- value and label of the option are the same, for example, 'United States'

In the example below, suggestions are based on the input value, but the user can enter any value and it will be preserved on blur.



### Simple Example

`Autocomplete` provides user a list of suggestions based on the input, however user is not limited to suggestions and can type anything.


.. exec::docs.autocomplete.simple

### Not a searchable select

`Autocomplete` is not a searchable select, it is a text input with suggestions. Values are not enforced to be one of
the suggestions, user can type anything. If you need a searchable select, use `Select` component instead.

### Select first option on change

Set the `selectFirstOptionOnChange` prop to automatically select the first option in the dropdown when the input value
changes. This feature allows users to type a value and immediately press Enter to select the first matching option,
without needing to press the arrow down key first.

.. exec::docs.autocomplete.select_first_option


### Data Format

`Autoselect` `data` prop accepts data in one of the following formats:

```python
data = ["Pandas", "NumPy", "TensorFlow", "PyTorch"]

# or

data = [
    {"group": "US", "items": ["New York", "Seattle"]},
    {"group": "Canada", "items": ["Montreal", "Vancouver"]}
]
```

### Options filtering

By default, `Autocomplete` filters options by checking if the option label contains input value. You can change this behavior 
with `filter`. The filter function receives an object with the following properties as a single argument:
 - `options` – array of options or options groups, all options are in `{ value: string; label: string; disabled?: boolean }` format
 - `search` – current search query
 - `limit` – value of limit prop passed to `Autocomplete`


.. functions_as_props::

Example of a custom filter function that matches options by words instead of letters sequence:

.. exec::docs.autocomplete.option_filter
    :code: false

.. sourcetabs::docs/autocomplete/option_filter.py, assets/examples-js/option_filter.js
    :defaultExpanded: true
    :withExpandedButton: true 


### Sort options

By default, options are sorted by their position in the data array. You can change this behavior with `filter` function:

.. functions_as_props::

.. exec::docs.autocomplete.option_sort
    :code: false

.. sourcetabs::docs/autocomplete/option_sort.py, assets/examples-js/option_sort.js
    :defaultExpanded: true
    :withExpandedButton: true 


### Large Data Sets

The best strategy for large data sets is to limit the number of options that are rendered at the same time. You can
do it with limit prop. 

Note that if you use a custom `filter` function, you need to implement your own logic to limit the number of options in filter

Example of `Autocomplete` with 100 000 options, 10 options are rendered at the same time:

.. exec::docs.autocomplete.large_data_sets


### renderOption

`renderOption` function allows you to customize option rendering.

.. functions_as_props::


.. exec::docs.autocomplete.render_option
    :code: false


.. sourcetabs::docs/autocomplete/render_option.py, assets/examples-js/render_option_select.js
    :defaultExpanded: true
    :withExpandedButton: true


### Nothing found message

`Autocomplete` component does not support nothing found message. It is designed to accept any string as a value, so it
does not make sense to show nothing found message. If you want to limit user input to suggestions, you can use
searchable `Select` component instead. To learn more about the differences between `Autocomplete` and `Select`, check this [help center article](https://help.mantine.dev/q/select-autocomplete-difference).


### Scrollable dropdown

By default, the options list is wrapped with `ScrollArea.Autosize`. You can control dropdown max-height with 
`maxDropdownHeight` prop if you do not change the default settings.

If you want to use native scrollbars, set `withScrollArea=False`. Note that in this case, you will need to change 
dropdown styles with `Styles API`.


.. exec::docs.autocomplete.scrollable



### Grouping Items

.. exec::docs.autocomplete.grouping


### Combobox props
You can override `Combobox` props with `comboboxProps`. It is useful when you need to change some of the props that are
not exposed by `MultiSelect`, for example `withinPortal`:

```python
dmc.Autocomplete(comboboxProps={"withinPortal": False})
```


### Change dropdown z-index


```python
dmc.Autocomplete(comboboxProps={"zIndex": 1000})
```

### Inside Popover

To use `Select` inside popover, you need to set `withinPortal=False`:

.. exec::docs.autocomplete.popover


### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec::docs.autocomplete.clearable

### Dropdown open in a callback

.. exec::docs.autocomplete.opened

### Dropdown position

By default, the dropdown is displayed below the input if there is enough space; otherwise it is displayed above the
input. You can change this behavior by setting `position` and `middlewares` props, which are passed down to the
underlying `Popover` component.

Example of dropdown that is always displayed above the input:

.. exec::docs.autocomplete.dropdown_position

### Dropdown width

To change dropdown width, set `width` prop in `comboboxProps`. By default, dropdown width is equal to the input width.

.. exec::docs.autocomplete.dropdown_width


### Dropdown offset

To change dropdown offset, set `offset` prop in `comboboxProps`:  

.. exec::docs.autocomplete.dropdown_offset

### Dropdown animation
By default, dropdown animations are disabled. To enable them, you can set `transitionProps`, which will be passed
down to the underlying `Transition` component.

.. exec::docs.autocomplete.dropdown_animation

### Dropdown padding

.. exec::docs.autocomplete.dropdown_padding


### Dropdown shadow

.. exec::docs.autocomplete.dropdown_shadow

### Left and right sections

`MultiSelect` supports `leftSection` and `rightSection` props. These sections are rendered with absolute position
inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

- `rightSection`/`leftSection` – component to render on the corresponding side of input
- `rightSectionWidth`/`leftSectionWidth` – controls width of the right section and padding on the corresponding side of the input. By default, it is controlled by component size prop.
- `rightSectionPointerEvents`/`leftSectionPointerEvents` – controls pointer-events property of the section. If you want to render a non-interactive element, set it to none to pass clicks through to the input.

.. exec::docs.autocomplete.left_right


### Input Props
`Select` component supports `Input` and Input Wrapper components features and all input element props.
`Select` documentation does not include all features supported by the component – see Input documentation to learn about all available features.


.. exec::docs.autocomplete.interactive
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

.. exec::docs.autocomplete.error


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

#### Autocomplete

.. kwargs::Autocomplete
