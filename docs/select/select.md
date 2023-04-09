---
name: Select
section: Inputs
head: Custom searchable select.
description: Select enables users to select an option in a dropdown. 
component: Select
styles: select
---

##### Simple Example

Select component allows user to pick one option from the given data.

Note: Dash adds some css by default which can lead you to see an ugly red box when setting the `required` or `error` 
prop to True. Use the below css snippet to counteract it.

```css
input:invalid {
    outline: none !important;
}
```

.. exec::docs.select.simple

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

.. exec::docs.select.searchable

##### Clearable

Set `clearable` prop to enable clearing selected values.

.. exec::docs.select.clearable

##### Creatable

Set `creatable` and `searchable` props to enable creating new select item. Following select has no data pre-filled, so
you can go ahead and create your own options.

.. exec::docs.select.creatable

##### Invalid State And Error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you
select less than 2 currency pairs.

.. exec::docs.select.error

##### With Icons

.. exec::docs.select.icons
