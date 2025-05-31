---
name: JavaScript Functions as Props
endpoint: /functions-as-props
description: Introduction to using JavaScript functions with Dash Mantine Components
dmc: false
---


.. toc::

Some components props support JavaScript functions to control how elements look and behave — like labels, tooltips, dropdown options, and more.


### Basic Usage

To use a JavaScript function in a DMC component, pass a dictionary like this:

```python
{"function": "myFunctionName"}
```

This tells Dash to call a function named `myFunctionName` from a `.js` file in your app’s `/assets/` folder.



Example: Format a Slider label

See this example in the [Slider Control Label](/components/slider#control-label) section.

Python

```python
dmc.Slider(
    label={"function": "formatTemperature"},
    # other props
)
```


JavaScript (in `/assets/formatTemperature.js`)

```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatTemperature = function (value) {
  return `${value} °C`;
};
```

See this example in the [Slider Control Label](/components/slider#control-label) section.


### Passing Extra Options

You can pass extra options from Python to customize how the JavaScript function behaves:

.py
```python
label = {
    "function": "formatTemperature",
    "options": {"unit": "F"}
}
```

.js
```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatTemperature = function (value, { unit }) {
  if (unit === "F") {
    return `${(value * 9 / 5 + 32).toFixed(1)} °F`;
  }
  return `${value.toFixed(1)} °C`;
};
```
See examples the Render Options example in the [TagsInput](components/tagsinput#renderoption) and [MultiSelect](components/multiselect#renderoption) sections

###  Returning a Component

Its also possible to return React components.  To do this:

- Use `React.createElement()` (no JSX).
- access DMC components by using  `window.dash_mantine_components`.
- If you've imported other component libraries, you can use them too. For example  `window.dash_iconify`, `window.dash_core_components`, etc.

Example: Components in Dropdown Options


```python

colors = {
    "Pandas": "grape",
    "NumPy": "blue",
    "Matplotlib": "teal",
    "Plotly": "violet",
}

component = dmc.Select(
    label="Choose a library",
    placeholder="Pick one",
    data=list(colors.keys()),
    renderOption={
        "function": "renderLibraryBadge",
        "options": {"colors": colors},
    },
)
```

```js 
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderLibraryBadge = function ({ option }, { colors }) {
  return React.createElement(
    dmc.Badge,
    {
      color: colors[option.value] || "gray",
      variant: "light",
      radius: "sm",
    },
    option.value
  );
};
```


### Use AI to Help Write JavaScript
If you're more comfortable in Python, you can use AI to write JavaScript functions for DMC components. Just provide the
logic in Python and follow this prompt pattern.

#### Prompt Template
When asking AI to generate a function:

1. State the function name.
2. Mention it’s for Dash Mantine Components.
3. Ask it to assign the function to dmcfuncs.functionName.
4. Provide the Python logic.
5. Always include this global header:
    ```
    var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
    ```
6. If the function returns a component, mention:
   - Use `React.createElement`
   - Don’t use JSX
   - Use `window.dash_mantine_components`


#### Example 1:  Simple function

AI Prompt:

> Write a JavaScript function for Dash Mantine Components named `formatUsd`. Assign it to `dmcfuncs.formatUsd`. In Python, the function would be:
>
> ```python
> def formatUsd(value):
     return f"${value:,.2f}"
> ```

AI Output:

```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatUsd = function (value) {
  return `$${new Intl.NumberFormat("en-US", { minimumFractionDigits: 2 }).format(value)}`;
};
```



#### Example 2 Function with options

AI Prompt:

> Write a JavaScript function for Dash Mantine Components named `formatTemp`. Assign it to `dmcfuncs.formatTemp`. In Python, the function would be:
> ```python
> def formatTemp(value, unit="C"):
>    if unit == "F":
>        return f"{value * 9 / 5 + 32:.1f} °F"
>    return f"{value:.1f} °C"
>```

AI Output:

```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatTemp = function (value, { unit }) {
  if (unit === "F") {
    return `${(value * 9 / 5 + 32).toFixed(1)} °F`;
  }
  return `${value.toFixed(1)} °C`;
};
```

---

#### Example 3: Return a Component


AI Prompt

> Write a JavaScript function for Dash Mantine Components named `renderBadge`. Assign it to `dmcfuncs.renderBadge`. 
> This function returns a React component. Use `React.createElement`. Do not use JSX. Use `dmc = window.dash_mantine_components`.
> In Python, the function would be:

> ```python
> def renderBadge(option):
>    return dmc.Badge(
>        option["value"],
>        color= "red" if option["value"] == "A" else "blue",
>        variant="light",
>        radius="sm"        
>    )
> ```


AI Output

```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
var dmc = window.dash_mantine_components;

dmcfuncs.renderBadge = function ({ option }) {
  return React.createElement(
    dmc.Badge,
    {
      color: option.value === "A" ? "red" : "blue",
      variant: "light",
      radius: "sm"
    },
    option.value
  );
};

```

Supported props in V2.0.0

| Component         | Props                                             |
|------------------|---------------------------------------------------|
| Slider           | label, scale                                      |
| RangeSlider      | label, scale                                      |
| Select           | renderOption, filter                              |
| MultiSelect      | renderOption, filter                              |
| TagsInput        | renderOption, filter                              |
| DatePickerInput  | disabledDates                                     |
| DateInput        | disabledDates                                     |
| DateTimePicker   | disabledDates                                     |
| MonthPickerInput | disabledDates                                     |
| YearPickerInput  | disabledDates                                     |
| BarChart         | getBarColor, valueFormatter, tooltipProps         |
| AreaChart        | valueFormatter, tooltipProps                      |
| LineChart        | valueFormatter, tooltipProps                      |
| CompositeChart   | valueFormatter, tooltipProps                      |
| BubbleChart      | valueFormatter, tooltipProps                      |
| ScatterChart     | valueFormatter, tooltipProps                      |

