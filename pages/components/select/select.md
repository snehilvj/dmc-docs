Select | Custom searchable select

### Simple example

Select component allows user to pick one option from the given data.

> example:components/select/_simple.py

### Data Prop

The data can be provided as either:
1. an array of strings - use when label and value are same.
2. an array of dicts with `label` and `value` properties.

> snippet:components/select/_data.py:python

### Searchable

Set `searchable` prop to enable search in Select and use `nothingFound` prop to show a label when no option matches the search.

> example:components/select/_searchable.py

### Clearable

Set `clearable` prop to enable clearing selected value.

> example:components/select/_clearable.py

### Grouping

> example:components/select/_groups.py

### Invalid State and error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if you select USDJPY.

> example:components/select/_error.py

> apidoc:Select
