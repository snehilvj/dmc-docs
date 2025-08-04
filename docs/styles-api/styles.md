---
name: Styles API
endpoint: /styles-api
head: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
description: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
package: dash_mantine_components
category: Styling
order: 4  # sets order in navbar section
---

.. toc::

### Styles API Overview

Most Dash users are familiar with the `style` prop — a dictionary of CSS rules applied to a component’s outermost container. Mantine supports this too, but also introduces a more powerful alternative: the `styles` prop.

Many Mantine components may look simple — for example, `TextInput` appears to be just an `<input type="text">`. But under the hood, it's composed of multiple nested elements for things like the label, description, error message, and layout.

This internal structure allows you to set props  like:

* `label` — a label for the input
* `description` — additonal helper text for the input
* `error` — a validation message

Instead of requiring you to manually render and style each element, Mantine includes them as part of the component — and the `styles` prop gives you control over how each part looks.

* Use `style` to apply styles to the outermost wrapper.
* Use `styles` to target specific internal parts (like the label, input, or error text).

Each component’s documentation lists which internal parts are available for styling via the `styles` prop.

### Styles API Selectors

To let you style these internal parts individually, each component exposes a set of style selectors — string identifiers like `"label"`, `"input"`, or `"error"` that represent specific internal elements.

You use them like this:

```python
styles={
    "label": {"fontWeight": 700},
    "input": {"backgroundColor": "#f0f0f0"},
    "error": {"color": "red"},
}
```

Each component has its own set of selectors based on its structure. These are documented in the Styles API section of each component’s page.

If you've used `className` in Dash this is similar — but built directly into the component system and consistent across Mantine.


#### Example: `dmc.Button` Selectors

| Name    | Static selector         | Description                      |
| :------ | :---------------------- | :------------------------------- |
| root    | .mantine-Button-root    | Root element                     |
| loader  | .mantine-Button-loader  | Loader shown when `loading=True` |
| section | .mantine-Button-section | Left and right icon sections     |
| inner   | .mantine-Button-inner   | Container for label and content  |
| label   | .mantine-Button-label   | The button’s text                |


You can use these selectors in multiple ways:

#### 1) With `classNames` or `styles` props

```python
# Using classNames
dmc.Button(
    "Styled with classNames",
    classNames={
        "root": "my-root-class",
        "label": "my-label-class",
        "inner": "my-inner-class",
    }
)

# Using inline styles
dmc.Button(
    "Styled with styles prop",
    styles={
        "root": {"backgroundColor": "red"},
        "label": {"color": "blue"},
        "inner": {"fontSize": 20},
    }
)
```

#### 2) In a global `theme` via `MantineProvider`

```python
theme = {
    "components": {
        "Button": {
            "classNames": {
                "root": "my-root-class",
                "label": "my-label-class",
                "inner": "my-inner-class",
            },
            "styles": {
                "root": {"backgroundColor": "red"},
                "label": {"color": "blue"},
                "inner": {"fontSize": 20},
            }
        }
    }
}

app.layout = dmc.MantineProvider(
    theme=theme,
    children=dmc.Button("Themed Button")
)
```

#### 3) In a `.css` file using static selectors

```css
.mantine-Button-root {
    background-color: red;
}

.mantine-Button-label {
    color: blue;
}

.mantine-Button-inner {
    font-size: 20px;
}
```

#### 4) Avoid dynamic class names

When inspecting elements in the browser, you may see generated class names like `m_77c9d27d`. These are internal to Mantine and not stable between versions. Don’t target these in CSS.

Instead, use:

* the `styles` or `classNames` props
* static class selectors like `.mantine-Button-root`



### Global vs. Specific Styling

You can combine global styling (via `theme` or static CSS) with component-specific overrides using `styles` or `classNames`.

For example:

* A default red background can be applied globally using `.mantine-Button-root`
* A specific button can override this with its own `className` or `styles`

Note: For components rendered in a portal — such as `Popover`, `Tooltip`, or `Modal` — static selectors often won’t work because parts of the DOM are rendered outside the main tree. In these cases, use `classNames` or `styles`, or set `withinPortal=False` if appropriate.


### Component Classes

Mantine uses hashed class names (e.g., `m_77c9d27d`) for internal styling. These class names may change between versions or builds, so you should never rely on them directly.

**Do not do this:**

```css
/* This is fragile and will likely break */
.m_77c9d27d {
  background: blue;
}
```

**Instead, do this:**

```css
/* Use static selectors */
.mantine-Button-root {
  background: blue;
}
```

Or:

```python
# Use the Styles API
dmc.Button(
    "Styled Button",
    classNames={"root": "my-custom-button"}
)
```



### Data Attributes

Many Mantine components use `data-*` attributes to reflect state or props. These can be useful for styling in CSS, especially when using features like loading states, icons, or layout modifiers.

You’ll find a list of data attributes for each component in its Styles API docs.

Example (`dmc.Button`):

| Selector  | Attribute                | Set When…            | Example value     |
| --------- | ------------------------ | -------------------- | ----------------- |
| `root`    | `data-disabled`          | `disabled=True`      | –                 |
| `root`    | `data-loading`           | `loading=True`       | –                 |
| `root`    | `data-block`             | `fullWidth=True`     | –                 |
| `root`    | `data-with-left-section` | `leftSection` is set | –                 |
| `section` | `data-position`          | Always               | `left` or `right` |

Example CSS targeting data attributes:

```css
/* Style disabled buttons */
.dmc-data-attributes-demo[data-disabled="true"] {
    color: red;
    cursor: not-allowed;
}

/* Style buttons while loading */
.dmc-data-attributes-demo[data-loading="true"] {
    background-color: darkgray;
}

/* Style left icon section */
.dmc-data-attributes-demo .mantine-Button-section[data-position="left"] {
    color: var(--mantine-color-yellow-filled);
}
```

.. exec::docs.styles-api.data-attributes



### More Examples

Here are a few component-specific examples. Refer to each component’s Styles API section for the full list of selectors and attributes.

#### Button

.. exec::docs.styles-api.button

#### Badge

.. exec::docs.styles-api.badge

#### TextInput

.. exec::docs.styles-api.input


### Styles with Callbacks

.. exec::docs.styles-api.conditional

### Slider

See the [Styling the Slider](/components/slider#styling-the-slider) section for a detailed example including:

* Dynamic theming with `light-dark`
* Custom styling for tracks, marks, and thumbs
* Attribute-based styling using `[data-filled]`


### Tabs

For another advanced example, see the [Styling the Tabs](/components/tabs#styling-the-tabs) section.


### DatePickerInput

Components that use portals (like `Popover`, `Modal`, and `Tooltip`) often render outside the DOM tree. To style their internal parts:

* Use `classNames` or `styles` props
* Or set `withinPortal=False` if supported

.. exec::docs.styles-api.datepickerinput
