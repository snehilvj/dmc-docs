---
name: MultiSelect
section: Inputs
head: Custom searchable multi select.
description: MultiSelect enables users to select multiple options in a dropdown. 
component: MultiSelect
---

##### Simple Example

MultiSelect component allows user to pick any number of option from the given data.

.. exec::docs.multiselect.simple

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

Set `searchable` prop to enable search in MultiSelect and use `nothingFound` prop to show a label when no option
matches the search.

.. exec::docs.multiselect.searchable

##### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec::docs.multiselect.clearable

##### Max Selected Values

You can specify the maximum number of values that can be selected.

.. exec::docs.multiselect.max-selected

##### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.multiselect.error
