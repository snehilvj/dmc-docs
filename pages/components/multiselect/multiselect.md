MultiSelect | Custom searchable multi select

### Simple example

MultiSelect component allows user to pick any number of option from the given data.

> example:components/multiselect/_simple.py

### Data Prop

The data can be provided as either:
1. an array of strings - use when label and value are same.
2. an array of dicts with `label` and `value` properties.

> snippet:components/multiselect/_data.py:python

### Searchable

Set `searchable` prop to enable search in MultiSelect and use `nothingFound` prop to show a label when no option matches the search.

> example:components/multiselect/_searchable.py

### Clearable

Set `clearable` prop to enable clearing selected values.

> example:components/multiselect/_clearable.py

### Grouping

> example:components/multiselect/_groups.py

### Max selected values

You can specify the maximum number of values that can be selected.

> example:components/multiselect/_max.py

### Invalid State and error

You can let the user know if the selected value is invalid. In the example below, you will get an error message if 
you select less than 2 currency pairs.

> example:components/multiselect/_error.py

> apidoc:MultiSelect
