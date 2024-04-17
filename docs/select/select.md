---
name: Select
description: Select enables users to select an option in a dropdown.
endpoint: /components/select
package: dash_mantine_components
---

.. toc::

### Simple Example

Select component allows user to pick one option from the given data.

Note: Dash adds some css by default which can lead you to see an ugly red box when setting the `required` or `error` 
prop to True. Use the below css snippet to counteract it.

```css
input:invalid {
    outline: none !important;
}
```

.. exec::docs.select.simple

### Data Format

The data can be provided as either:
* an array of strings - use when label and value are same.
* an array of dicts with `label` and `value` properties.
* an array of dict with `group` and `items` as keys where items are one of the previous two types.

```python
data = ["React", "Angular", "Svelte", "Vue"]

# or

data = [
    {"value": "React", "label": "React"},
    {"value": "Angular", "label": "Angular"},
    {"value": "Svelte", "label": "Svelte"},
    {"value": "Vue", "label": "Vue"},
]

# or

data = [
    {"group": "Frontend", "items": ["React", "Angular"]},
    {"group": "Backend", "items": ["Express", "Django"]}
]

# or

data = [
    {
        "group": "Frontend",
        "items": [
            {"value": "React", "label": "React"},
            {"value": "Angular", "label": "Angular"},
        ],
    },
    {
        "group": "Backend",
        "items": [
            {"value": "Svelte", "label": "Svelte"},
            {"value": "Vue", "label": "Vue"},
        ],
    },
]
```

### Searchable

Set `searchable` prop to enable search in Select and use `nothingFoundMessage` prop to show a label when no option
matches the search.

.. exec::docs.select.searchable

### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec::docs.select.clearable

### Grouping Items

.. exec::docs.select.grouping

### Dropdown Position

By default, dropdown is placed below the input and when there is not enough space, it flips to be above the input. To
change this behavior, use `comboBoxProps` prop:

.. exec::docs.select.position

### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.select.error

### With Icons

.. exec::docs.select.icons

### Styles API

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

#### Select

.. kwargs::Select
