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

### Data Prop

The data can be provided as either:
* an array of strings - use when label and value are same.
* an array of dicts with `label` and `value` properties.

```python
data = ["React", "Angular", "Svelte", "Vue"]

# or

data = [
    {"value": "React", "label": "React"},
    {"value": "Angular", "label": "Angular"},
    {"value": "Svelte", "label": "Svelte"},
    {"value": "Vue", "label": "Vue"},
]
```

### Grouping

.. exec::docs.multiselect.grouping


### Searchable

Set `searchable` prop to enable search in MultiSelect and use `nothingFound` prop to show a label when no option
matches the search.

.. exec::docs.multiselect.searchable

### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec::docs.multiselect.clearable

### Max Selected Values

You can specify the maximum number of values that can be selected.

.. exec::docs.multiselect.max-selected

### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.multiselect.error

### Styles API

| Name               | Static selector                         | Description                                                               |
|:-------------------|:----------------------------------------|:--------------------------------------------------------------------------|
| wrapper            | .mantine-MultiSelect-wrapper            | Root Input element                                                        |
| dropdown           | .mantine-MultiSelect-dropdown           | Dropdown element                                                          |
| item               | .mantine-MultiSelect-item               | Item element, rendered inside dropdown                                    |
| nothingFound       | .mantine-MultiSelect-nothingFound       | Nothing found label                                                       |
| values             | .mantine-MultiSelect-values             | Values wrapper                                                            |
| value              | .mantine-MultiSelect-value              | Value element                                                             |
| searchInput        | .mantine-MultiSelect-searchInput        | Search input, rendered after all values                                   |
| defaultValue       | .mantine-MultiSelect-defaultValue       | Default value component wrapper                                           |
| defaultValueRemove | .mantine-MultiSelect-defaultValueRemove | Default value remove control                                              |
| defaultValueLabel  | .mantine-MultiSelect-defaultValueLabel  | Default value label                                                       |
| separator          | .mantine-MultiSelect-separator          | Divider wrapper                                                           |
| separatorLabel     | .mantine-MultiSelect-separatorLabel     | Divider Label                                                             |
| itemsWrapper       | .mantine-MultiSelect-itemsWrapper       | Wraps all items in dropdown                                               |
| icon               | .mantine-MultiSelect-icon               | Input icon wrapper on the left side of the input, controlled by icon prop |
| input              | .mantine-MultiSelect-input              | Main input element                                                        |
| root               | .mantine-MultiSelect-root               | Root element                                                              |
| label              | .mantine-MultiSelect-label              | Label element styles, defined by label prop                               |
| error              | .mantine-MultiSelect-error              | Error element styles, defined by error prop                               |
| description        | .mantine-MultiSelect-description        | Description element styles, defined by description prop                   |
| required           | .mantine-MultiSelect-required           | Required asterisk element styles, defined by required prop                |

### Keyword Arguments

#### MultiSelect

.. kwargs::MultiSelect
