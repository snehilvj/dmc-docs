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

### Clearable

Set `clearable` prop to display the clear button in the right section. The button is not displayed when:

* The component does not have a value
* The component is disabled
* The component is read only

.. exec::docs.tagsinput.clearable

### Max selected values

You can limit the number of selected values with `maxTags` prop. This will not allow adding more values once the limit is reached.

.. exec::docs.tagsinput.max-selected

### Allow duplicates

By default, `TagsInput` does not allow adding duplicate values, but you can change this behavior by setting `allowDuplicates` prop.
Value is considered duplicate if it is already present in the `value` array, regardless of the case and trailing whitespace.

```python
import dash_mantine_components as dmc

dmc.TagsInput(
    allowDuplicates=True
)
```

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

### Data Format

`TagsInput` `data` prop accepts data in one of the following formats:

```python
data = ["React", "Angular", "Svelte", "Vue"]

# or

data = [
    {"group": "Frontend", "items": ["React", "Angular"]},
    {"group": "Backend", "items": ["Express", "Django"]}
]
```

### Grouping

.. exec::docs.tagsinput.grouping

### Styles API

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
