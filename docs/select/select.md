---
name: Select
section: Inputs & Buttons
head: Custom searchable select.
description: Select enables users to select an option in a dropdown. 
component: Select
---

##### Simple Example

Select component allows user to pick one option from the given data.

.. exec-block::docs.select.simple

##### Data Prop

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

##### Searchable

Set `searchable` prop to enable search in Select and use `nothingFound` prop to show a label when no option
matches the search.

.. exec-block::docs.select.searchable

##### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec-block::docs.select.clearable

##### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec-block::docs.select.error

##### Gallery

.. gallery-block::docs.select.icons
    :label: Select with icons
