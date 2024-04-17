---
name: MultiSelect
description: MultiSelect enables users to select multiple options in a dropdown.
endpoint: /components/multiselect
package: dash_mantine_components
---

.. toc::

### Simple Example

MultiSelect component allows user to pick any number of option from the given data.

.. exec::docs.multiselect.simple

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

### Grouping

.. exec::docs.multiselect.grouping

### Searchable

Set `searchable` prop to enable search in MultiSelect and use `nothingFoundMessage` prop to show a label when no option
matches the search.

.. exec::docs.multiselect.searchable

### Max Selected Values

You can specify the maximum number of values that can be selected.

.. exec::docs.multiselect.max-selected

### Checked option icon

Set `checkIconPosition` prop to `left` or `right` to control position of check icon in active option.
To remove the check icon, set `withCheckIcon=False`.

.. exec::docs.multiselect.check

### Hide selected options

To remove selected options from the list of available options, set `hidePickedOptions` prop:

.. exec::docs.multiselect.hide

### Inside Popover

To use MultiSelect inside popover, you need to set `withinPortal=False`:

.. exec::docs.multiselect.popover

### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.multiselect.error

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
