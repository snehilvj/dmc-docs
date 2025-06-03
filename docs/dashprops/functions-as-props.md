---
name: JavaScript Functions as Props
endpoint: /functions-as-props
description: Introduction to using JavaScript functions with Dash Mantine Components
dmc: false
---


.. toc::


### How Function Props Work

In JavaScript libraries like [Mantine](https://mantine.dev), some component props accept functions — for example, to
format a value, render custom content, or control behavior. Here is an example of formating the label of the `Slider`

```js
<Slider label={(value) => `${value} °C`} />
```

However, in a Dash app, you can’t pass a Python function to a JavaScript component running in the browser. Functions
don't serialize over the network.

To support this safely, Dash Mantine Components allows you to pass named references to JavaScript functions instead.

You write your function in a `.js` file in the `/assets` folder, and refer to it by name in Python:

```python
label = {"function": "formatCelsius"}
```

assets/formatCelsius.js
```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.formatCelsius = function (value) {
  return `${value} °C`;
};
```

DMC knows how to call this function in the browser for props like `label`.



### About Mantine Function Props

Only specific props in Mantine support functions. For example:

* `Slider.label`
* `Select.renderOption`
* `BarChart.getBarColor`
* `ScatterChart.valueFormat`

Each function must follow the structure defined by Mantine. You can refer to the [Mantine documentation](https://mantine.dev) 
for details on what props accept functions and what each function receives.



### Example: Slider label

See this example in the [Slider Control Label](/components/slider#control-label) section.

In Mantine:

```js
<Slider label={(value) => `${value} °C`} />
```

In DMC:

```python
dmc.Slider(label={"function": "formatCelsius"})
```

```js
dmcfuncs.formatCelsius = function (value) {
  return `${value} °C`;
};
```



### Passing Extra Options

You can pass extra options from Python to customize how the JavaScript function behaves.

In this example, the same function can be used to format the label using either Celsius or Fahrenheit.

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

###  Returning a Component

Its also possible to return React components.  To do this:

- Use `React.createElement()` (no JSX).
- access DMC components by using  `window.dash_mantine_components`.
- If you've imported other component libraries, you can use them too. For example  `window.dash_iconify`, `window.dash_core_components`, etc.

Example: Components in Dropdown Options

.py
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

.js
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

Most Dash users are more comfortable writing Python than JavaScript. You can use AI tools like ChatGPT to generate the
JavaScript functions needed for Dash Mantine Components.

While it's possible to describe the logic in plain English, in practice, writing the function in Python and asking the 
AI to translate it tends to produce more accurate and usable results. It gives the model a clear structure and avoids
ambiguity, especially for functions with conditions, formatting rules, or custom output.

#### Prompt Template
When asking AI to generate a function:

1. State the function name.
2. Mention it’s for Dash Mantine Components.
3. Ask it to assign the function to dmcfuncs.functionName.
4. Provide the Python logic (or natural language)
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

The following props support JavaScript functions in Dash Mantine Components version 2.0.0.
If there’s a Mantine prop you’d like to see added, feel free to [open an issue on GitHub.](https://github.com/snehilvj/dash-mantine-components/issues)

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

