---
name: JavaScript Functions as Props
endpoint: /functions-as-props
description: Introduction to using JavaScript functions with Dash Mantine Components
dmc: false
---


.. toc::


Some Dash Mantine Components support custom JavaScript functions to let you control how things appear — such as tooltips,
labels, dropdown options, and formatting.


### Basic Usage

To use a JavaScript function in a DMC component, you pass a dictionary like this in Python:

```python
{"function": "myFunctionName"}
```

This tells Dash to look for a function named `myFunctionName` in a `.js` file in your app’s `/assets/` folder.



#### Example: Format Temperature

You might use this with a component like `Slider` to display a formatted label above the slider value.

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


### Passing Extra Options

If you want to customize behavior from Python — for example, choose Celsius or Fahrenheit — you can pass an `options` 
dictionary to the JavaScript function.  This makes your function flexible without rewriting it for every variation.

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

Some props in Dash Mantine Components — like `renderOption`, `tooltipProps.content`, and others — let you return a
component, not just a string.

This lets you customize how things look using Mantine elements like `Text`, `Group`, `Avatar`, and more.

To return a component, you use `React.createElement(...)`, which is how components are created in JavaScript (without using JSX).

You must also use the DMC component library available in the browser as:

```js
window.dash_mantine_components
```


#### Example: Render a custom dropdown option


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


### Using AI to Write JavaScript Functions 

If you're more comfortable writing Python than JavaScript, you can use AI (like ChatGPT) to generate JavaScript functions for use in Dash Mantine Components.

This section shows how to start with a Python function and write a prompt that AI can use to generate the correct JavaScript version — ready to use with `{"function": "..."}` in DMC.

---

### Prompt Pattern

Always tell AI:

1. The function name
2. That it's for Dash Mantine Components
3. That it should be assigned to `dmcfuncs.functionName`
4. Show the Python version of the logic
5. For functions that return components — tell AI to use `React.createElement` and avoid JSX
6. Always include this global header:

   ```js
   var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};
   ```


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

> Write a JavaScript function for Dash Mantine Components named `renderLibraryBadge`. Assign it to `dmcfuncs.renderLibraryBadge`. 
> This function returns a React component. Use `React.createElement`. Do not use JSX. Use `dmc = window.dash_mantine_components`.
> In Python, the function would be:

> ```python
> def renderLibraryBadge(option):
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

dmcfuncs.renderLibraryBadge = function ({ option }) {
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
