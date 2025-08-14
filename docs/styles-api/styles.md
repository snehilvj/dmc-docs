---
name: Styles API
endpoint: /styles-api
head: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
description: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
package: dash_mantine_components
category: Styling
order: 2  # sets order in navbar section
---

.. toc::


### Styles API Overview

DMC supports `style` and `className` props for styling the root element, just like other Dash libraries.
However, many DMC components have nested elements.  For example the `TextInput` includes `label`, `description`,
`error` props.

The Styles API is a set of props and techniques that allows you to customize the style of any element inside a Mantine
component - inline using the  `classNames` or `styles` props, or using the [Theme Object](/theme-object).


### Styles API Selectors

Each component has its own set of selectors based on its structure. These are documented in the Styles API section of each component’s page.


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

#### 2) In the `theme` prop in  `MantineProvider`

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

### classNames Prop

The `classNames` prop is used to apply custom CSS class names to specific inner elements of a Mantine component. It 
accepts a dictionary  with element names as keys and classes as values. This approach is preferred for larger-scale styling and
maintainability.


### Styles Prop

The `styles` prop is used to apply inline styles directly to specific inner elements of a Mantine component. It accepts
an dictionary where keys correspond to the names of the inner elements (as defined in the component's Styles API documentation)
and values are style objects. Inline styles have higher specificity than classes, meaning they will override styles
defined by classes unless `!important` is explicitly used in the class definition.

You cannot use pseudo-classes (for example, `:hover`, `:first-of-type`) and media queries inside the `styles` prop.


> styles prop usage
>
> Some examples and demos in the documentation use the `styles` prop for convenience, but it is not recommended to use the `styles` prop as the primary means of styling components, as the `classNames` prop is more flexible and has better performance.

### Avoid dynamic class names

When inspecting elements in the browser, you may see generated class names like `m_77c9d27d`. These are internal to Mantine and can change between versions. Don’t target these in your CSS.

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


### attributes prop

Use `attributes` prop to pass attributes to inner elements of all components that support Styles API. For example,
it can be used to add data attributes for testing purposes:


.. exec::docs.styles-api.attributes



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
