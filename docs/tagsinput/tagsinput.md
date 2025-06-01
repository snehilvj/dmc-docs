---
name: TagsInput
description: Capture a list of values from user with free input and suggestions
endpoint: /components/tagsinput
package: dash_mantine_components
category: Combobox
---

.. toc::

### Simple Example

`TagsInput` provides a way to enter multiple values. It can be used with suggestions or without them.
`TagsInput` is similar to MultiSelect, but it allows entering custom values.

By default, `enter key` and `,` will select the typed value.

.. exec::docs.tagsinput.simple



### Data Format

Note that the `data` format is different than components like `Select` and `Multi Select`.  See [Why can I not use value/label data structure with TagsInput?](https://help.mantine.dev/q/autocomplete-value-label)

`TagsInput` `data` prop accepts data in one of the following formats:

```python
data = ["React", "Angular", "Svelte", "Vue"]

# or

data = [
    {"group": "Frontend", "items": ["React", "Angular"]},
    {"group": "Backend", "items": ["Express", "Django"]}
]
```

### Clearable

Set `clearable` prop to display the clear button in the right section. The button is not displayed when:

* The component does not have a value
* The component is disabled
* The component is read only

.. exec::docs.tagsinput.clearable

### Max selected values

You can limit the number of selected values with `maxTags` prop. This will not allow adding more values once the limit is reached.

.. exec::docs.tagsinput.max-selected

### Accept value on blur
By default, if the user types a value and blurs the input, the value is added to the list. You can change this behavior
by setting `acceptValueOnBlur` to `False`. In this case, the value is added only when the user presses `Enter` or clicks
on a suggestion.

.. exec::docs.tagsinput.acceptvalueonblur

### Allow duplicates

By default, `TagsInput` does not allow adding duplicate values, but you can change this behavior by setting `allowDuplicates` prop.
Value is considered duplicate if it is already present in the `value` array, regardless of the case and trailing whitespace.


.. exec::docs.tagsinput.duplicates


### Split chars

By default, `TagsInput` splits values by comma (`,`), but you can change this behavior by setting `splitChars` prop to an array of strings.
All values from `splitChars` cannot be included in the final value. Values are also split on paste.

Example of splitting by `,`, `|` and `space`:

.. exec::docs.tagsinput.split

### With suggestions

`TagsInput` can be used with suggestions, it will render suggestions list under input and allow selecting suggestions 
with keyboard or mouse. Note that user is not limited to suggestions, it is still possible to enter custom values. 
If you want to allow values only from suggestions, use [MultiSelect](/components/multiselect) component instead.

.. exec::docs.tagsinput.suggestions


### Grouping

.. exec::docs.tagsinput.grouping


### Large data sets
The best strategy for large data sets is to limit the number of options that are rendered at the same time. You can do
it with `limit` prop. 

Example of `TagsInput` with 100 000 options, 5 options are rendered at the same time:


.. exec::docs.tagsinput.large_data_sets


### renderOption

`renderOption` function allows you to customize option rendering.

.. functions_as_props::

.. exec::docs.tagsinput.render_option
    :code: false

.. sourcetabs::docs/tagsinput/render_option.py, assets/examples-js/render_option_tagsinput.js
    :defaultExpanded: true
    :withExpandedButton: true


### Options filtering

By default, `TagsInput` filters options by checking if the option label contains input value. You can change this behavior 
with `filter`. The filter function receives an object with the following properties as a single argument:
 - `options` – array of options or options groups, all options are in `{ value: string; label: string; disabled?: boolean }` format
 - `search` – current search query
 - `limit` – value of limit prop passed to `Select`


.. functions_as_props::

Example of a custom filter function that matches options by words instead of letters sequence:

.. exec::docs.tagsinput.option_filter
    :code: false

.. sourcetabs::docs/tagsinput/option_filter.py, assets/examples-js/option_filter.js
    :defaultExpanded: true
    :withExpandedButton: true 


### Sort options

By default, options are sorted by their position in the data array. You can change this behavior with `filter` function:

.. functions_as_props::

.. exec::docs.tagsinput.option_sort
    :code: false

.. sourcetabs::docs/tagsinput/option_sort.py, assets/examples-js/option_sort.js
    :defaultExpanded: true
    :withExpandedButton: true 




### Scrollable dropdown

By default, the options list is wrapped with `ScrollArea.Autosize`. You can control dropdown max-height with 
`maxDropdownHeight` prop if you do not change the default settings.

If you want to use native scrollbars, set `withScrollArea=False`. Note that in this case, you will need to change 
dropdown styles with `Styles API`.


.. exec::docs.tagsinput.scrollable

### Disabled options  

When an option is disabled, it cannot be selected and is ignored in keyboard navigation. Note that user can still enter
disabled option as a value. If you want to prohibit certain values, use a callback to filter them out.

.. exec::docs.tagsinput.disabledoptions


### Combobox props
You can override `Combobox` props with `comboboxProps`. It is useful when you need to change some of the props that are
not exposed by `TagsInput`, for example `withinPortal`:

```python
dmc.TagsInput(comboboxProps={"withinPortal": False})
```


### Change dropdown z-index

```python
dmc.TagsInput(comboboxProps={"zIndex": 1000})
```

### Inside Popover

To use `TagsInput` inside popover, you need to set `withinPortal=False`:

.. exec::docs.tagsinput.popover


### Dropdown open in a callback

.. exec::docs.tagsinput.opened

### Dropdown position

By default, the dropdown is displayed below the input if there is enough space; otherwise it is displayed above the
input. You can change this behavior by setting `position` and `middlewares` props, which are passed down to the
underlying `Popover` component.

Example of dropdown that is always displayed above the input:

.. exec::docs.tagsinput.dropdown_position

### Dropdown width

To change dropdown width, set `width` prop in `comboboxProps`. By default, dropdown width is equal to the input width.

.. exec::docs.tagsinput.dropdown_width


### Dropdown offset

To change dropdown offset, set `offset` prop in `comboboxProps`:  

.. exec::docs.tagsinput.dropdown_offset

### Dropdown animation
By default, dropdown animations are disabled. To enable them, you can set `transitionProps`, which will be passed
down to the underlying `Transition` component.

.. exec::docs.tagsinput.dropdown_animation

### Dropdown padding

.. exec::docs.tagsinput.dropdown_padding


### Dropdown shadow

.. exec::docs.tagsinput.dropdown_shadow



### Left and right sections

`MultiSelect` supports `leftSection` and `rightSection` props. These sections are rendered with absolute position
inside the input wrapper. You can use them to display icons, input controls or any other elements.

You can use the following props to control sections styles and content:

- `rightSection`/`leftSection` – component to render on the corresponding side of input
- `rightSectionWidth`/`leftSectionWidth` – controls width of the right section and padding on the corresponding side of the input. By default, it is controlled by component size prop.
- `rightSectionPointerEvents`/`leftSectionPointerEvents` – controls pointer-events property of the section. If you want to render a non-interactive element, set it to none to pass clicks through to the input.

.. exec::docs.tagsinput.left_right


### Input Props
`TagsInput` component supports `Input` and Input Wrapper components features and all input element props.
`TagsInput` documentation does not include all features supported by the component – see Input documentation to learn about all available features.

 
.. exec::docs.tagsinput.interactive
   :code: false

### Read only
Set `readOnly` to make the input read only. When `readOnly` is set, `TagsInput` will not show suggestions and value
cannot be updated by the user entering data in the input.

.. exec::docs.tagsinput.readonly

### Disabled
Set `disabled` to disable the input. When `disabled` is set, user cannot interact with the input and `TagsInput` will not show suggestions.

.. exec::docs.tagsinput.disabled

### Styles API

.. styles_api_text::

Refer to the Mantine TagsInput Style API [interactive demo](https://mantine.dev/core/tags-input/#styles-api) for help in identifying each selector.


| Name        | Static selector                | Description                                      |
|:------------|:-------------------------------|:-------------------------------------------------|
| wrapper     | .mantine-TagsInput-wrapper     | Root element of the Input                        |
| input       | .mantine-TagsInput-input       | Input element                                    |
| section     | .mantine-TagsInput-section     | Left and right sections                          |
| root        | .mantine-TagsInput-root        | Root element                                     |
| label       | .mantine-TagsInput-label       | Label element                                    |
| required    | .mantine-TagsInput-required    | Required asterisk element, rendered inside label |
| description | .mantine-TagsInput-description | Description element                              |
| error       | .mantine-TagsInput-error       | Error element                                    |
| dropdown    | .mantine-TagsInput-dropdown    | Dropdown root element                            |
| options     | .mantine-TagsInput-options     | Options wrapper                                  |
| option      | .mantine-TagsInput-option      | Option                                           |
| empty       | .mantine-TagsInput-empty       | Nothing found message                            |
| group       | .mantine-TagsInput-group       | Options group wrapper                            |
| groupLabel  | .mantine-TagsInput-groupLabel  | Options group label                              |
| pill        | .mantine-TagsInput-pill        | Value pill                                       |
| inputField  | .mantine-TagsInput-inputField  | Input field                                      |
| pillsList   | .mantine-TagsInput-pillsList   | List of pills, also contains input field         |

### Keyword Arguments

#### TagsInput

.. kwargs::TagsInput
