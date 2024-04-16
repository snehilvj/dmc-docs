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

### Searchable

Set `searchable` prop to enable search in Select and use `nothingFound` prop to show a label when no option
matches the search.

.. exec::docs.select.searchable

### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec::docs.select.clearable

### Grouping Items

.. exec::docs.select.grouping

### Dropdown Position

By default, dropdown is placed below the input and when there is not enough space, it flips to be above the input. To
change this behavior, set dropdownPosition prop:

.. exec::docs.select.position

### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.select.error

### With Icons

.. exec::docs.select.icons

### Input Props

.. exec::docs.select.input


### Styles API

| Name           | Static selector                | Description                                                               |
|:---------------|:-------------------------------|:--------------------------------------------------------------------------|
| dropdown       | .mantine-Select-dropdown       | Dropdown element                                                          |
| item           | .mantine-Select-item           | Item element, rendered inside dropdown                                    |
| nothingFound   | .mantine-Select-nothingFound   | Nothing found label                                                       |
| separator      | .mantine-Select-separator      | Divider wrapper                                                           |
| separatorLabel | .mantine-Select-separatorLabel | Separator Label                                                           |
| itemsWrapper   | .mantine-Select-itemsWrapper   | Wraps all items in dropdown                                               |
| wrapper        | .mantine-Select-wrapper        | Root Input element                                                        |
| icon           | .mantine-Select-icon           | Input icon wrapper on the left side of the input, controlled by icon prop |
| input          | .mantine-Select-input          | Main input element                                                        |
| rightSection   | .mantine-Select-rightSection   | Input right section, controlled by rightSection prop                      |
| root           | .mantine-Select-root           | Root element                                                              |
| label          | .mantine-Select-label          | Label element styles, defined by label prop                               |
| error          | .mantine-Select-error          | Error element styles, defined by error prop                               |
| description    | .mantine-Select-description    | Description element styles, defined by description prop                   |
| required       | .mantine-Select-required       | Required asterisk element styles, defined by required prop                |

### Keyword Arguments

#### Select

.. kwargs::Select
