---
name: JavaScript Functions as Props
endpoint: /functions-as-props
description: Introduction to using JavaScript functions with Dash Mantine Components
dmc: false
---


.. toc::


### How Function Props Work

In JavaScript libraries like [Mantine](https://mantine.dev), some component props accept functions — for example, to
dynamically format a value, render custom content, or control behavior. Here is an example of formating the label of the `Slider`

**In Mantine**
```js
<Slider label={(value) => `${value} °C`}  />
```

However, in a Dash app, you can’t pass a function to the component because functions don't serialize over the network.

To support this safely, Dash Mantine Components allows you to pass named references to JavaScript functions instead.

You write your function in a `.js` file in the `/assets` folder, and refer to it by name in Python:

**app.py**
```python
dmc.Slider(label={"function": "celsiusLabel"}, value=40)
```

**assets/formatCelsius.js**
```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.celsiusLabel = function(value) {
  return `${value} °C`;
};
```

DMC knows how to call this function in the browser for props like `label`.


### Example: Formatting a Slider label

See more examples in the [Slider section](/components/slider) section.


.. exec::docs.dashprops.slider_label
    :code: false

.. sourcetabs::docs/dashprops/slider_label.py, assets/examples-js/celcius_label.js
    :defaultExpanded: true
    :withExpandedButton: true



### Function Props in Mantine Components

Not all Mantine props accept functions — only specific ones are designed to.

Here are some examples:

* `Slider`: `label`
* `Select`: `renderOption`
* `BarChart`: `getBarColor`
* `ScatterChart`: `valueFormat`

For a full list of supported function props in Dash Mantine Components, see the table at the bottom of this page.

Each function must match the structure expected by Mantine. To learn what arguments each one receives — and how they’re
used — refer to the [Mantine documentation](https://mantine.dev). You’ll also find complete working examples in the relevant sections of the DMC docs.






### Passing Extra Options

You can pass extra options from Python to customize how the JavaScript function behaves.

In this example, the same function can be used to format the label using either Celsius or Fahrenheit.

.py
```python
dmc.Slider(
    label={
        "function": "formatTemperature",
        "options": {"unit": "F"}
    },
    # other props
)
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
- If you've imported other component libraries in your Dash app, you can use them too. For example  `window.dash_iconify`, `window.dash_core_components`, etc.

See examples of including icons in the dropdown data in the `Select` section of the docs.

### Example: Components and passing extra options

This example shows
  - Returning a component.  Note the dropdown data is formated as a `Badge`.
  - Passing extra options to the JavaScript function.  The colors for each badge are passed to the function from the dash app.


.. exec::docs.dashprops.return_component
    :code: false

.. sourcetabs::docs/dashprops/return_component.py, assets/examples-js/render_badge.js
    :defaultExpanded: true
    :withExpandedButton: true




### Using Other JavaScript Libraries
You can use third-party JavaScript libraries inside your Dash functions — as long as you include them correctly in your app.

Here is an example of including the `dayjs` library as an external script:

```python
app = Dash(exteral_scripts=["https://cdnjs.cloudflare.com/ajax/libs/dayjs/1.10.8/dayjs.min.js"])
```

.js
```json
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.excludeDate = function(dateStr) {
   const date = dayjs(dateStr, "YYYY-MM-DD");
   return date.isValid() && date.day() !== 5;
}
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

Supported props in V2

The following props support JavaScript functions in Dash Mantine Components version >=2.0.0.
If there’s a Mantine prop you’d like to see added, feel free to [open an issue on GitHub.](https://github.com/snehilvj/dash-mantine-components/issues)

| Component        | Props                                     |
|------------------|-------------------------------------------|
| Slider           | label, scale                              |
| RangeSlider      | label, scale                              |
| Select           | renderOption, filter                      |
| MultiSelect      | renderOption, filter                      |
| TagsInput        | renderOption, filter                      |
| DatePickerInput  | disabledDates                             |
| DateInput        | disabledDates                             |
| DateTimePicker   | disabledDates                             |
| MonthPickerInput | disabledDates                             |
| YearPickerInput  | disabledDates                             |
| BarChart         | getBarColor, valueFormatter, tooltipProps |
| AreaChart        | valueFormatter, tooltipProps              |
| LineChart        | valueFormatter, tooltipProps              |
| CompositeChart   | valueFormatter, tooltipProps              |
| BubbleChart      | valueFormatter, tooltipProps              |
| ScatterChart     | valueFormatter, tooltipProps              |
| Tree             | renderNode (as of v2.1.0)                 |




