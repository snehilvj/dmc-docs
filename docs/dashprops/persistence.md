---
name: persistence props
endpoint: /persistence
description:  Dash Mantine Components support Dash’s built-in persistence system, allowing component values to be remembered across page reloads, tabs, or user sessions — without writing extra callbacks.

category: Dash
---


.. toc::


### What It Does

When a user interacts with a component (like typing in a `TextInput` or selecting a `Date`), its value is
stored in local memory (or optionally, in localStorage or sessionStorage). If the user refreshes the page, navigates
away and returns, or reopens the tab, that value can be restored automatically.

This helps maintain app state with minimal effort.

### How to Enable

You can enable persistence on any supported component by setting these three props:

```python
persistence=True
persisted_props=["value"]  # or other prop(s) to persist. 
persistence_type="local"   # "local", "session", or "memory" (default is local)
```

Note:  In DMC, the `persisted_prop` is set to the correct default for each component so this prop can be ignored.

### Example: Persistent TextInput
Try typing something in each box, then refresh the browser to see which one remembers your input.
    
.. exec::docs.dashprops.persistence


### Supported DMC Components

Persistence is available for all stateful inputs in DMC — including:

* `TextInput`, `Textarea`, `PasswordInput`, `NumberInput`
* `Select`, `MultiSelect`, `TagsInput`
* `Checkbox`, `RadioGroup`, `Switch`
* `DateInput`, `DateTimePicker`, `TimeInput`, etc.

To check if a specific component supports persistence, look for the `persistence`, `persisted_props`, and
`persistence_type` props in the Keyword Arguments section of its documentation.



### Reference

For more details see the [Persistence section in the Dash documentation.](https://dash.plotly.com/persistence)

- `persistence` (boolean | string | number; optional): Any truthy value will enable persistence for this component. Persistence is keyed to the combination of component id and this persistence value, so if this value changes you will see different persisted settings. For example, perhaps you have dropdowns for country and city, and you know that your users want to see the same country pre-filled as the last time they used your app - you can just set persistence=True on the country dropdown. But for the city they would like to see the same one as the last time they chose that country - just set persistence=country_name (where country_name is the value of the chosen country) on the city dropdown and we'll save one preferred city for each country.

- `persistence_type` ('local', 'session', or 'memory'; default 'local'): Where persisted user changes will be stored:

  - `memory`: only kept in memory, reset on page refresh. This is useful for example if you have a tabbed app, that deletes the component when a different tab is active, and you want changes persisted as you switch tabs but not after reloading the app.
  - `local`: uses window.localStorage. This is the default, and keeps the data indefinitely within that browser on that computer.
  - `session`: uses window.sessionStorage. Like 'local' the data is kept when you reload the page, but cleared when you close the browser or open the app in a new browser tab.

- `persistence_props` (list of strings; optional): These are the props whose values will persist. Typically this defaults to all user-editable props, which in many cases is just one (ie 'value'). dash-table has many props users can edit, and all of them except 'data' are included here by default. Sometimes only a part of a prop is saved; this happens with table headers, which are only part of the columns prop. The corresponding persistence_props value is 'columns.name'.