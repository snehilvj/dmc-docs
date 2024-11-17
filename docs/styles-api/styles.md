---
name: Styles API
endpoint: /styles-api
head: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
description: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
dmc: false
---

.. toc::


### What is Styles API

The Styles API is a set of properties that allows you to customize the style of any element inside a dash-mantine-components (dmc) component. All dmc components that have styles support the Styles API.

### Styles API selectors

Every dmc component that supports the Styles API has a set of element names that can be used to apply styles to inner elements inside the component. For simplicity, these elements names are called selectors in the documentation. You can find selectors information in each component's documentation.

Example of `dmc.Button` component selectors:


| Name    | Static selector         | Description                                                 |
|:--------|:------------------------|:------------------------------------------------------------|
| root    | .mantine-Button-root    | Root element                                                |
| loader  | .mantine-Button-loader  | Loader component, displayed only when `loading` prop is set |
| section | .mantine-Button-section | Left and right sections of the button                       |
| inner   | .mantine-Button-inner   | Contains all other elements, child of the `root` element    |
| label   | .mantine-Button-label   | Button children                                             |



You can use these selectors in `classNames` and `styles` in component props and `theme`:

```python
import dash_mantine_components as dmc

# Using classNames
dmc.Button(
    "Button with custom classes",
    classNames={
        "root": "my-root-class",
        "label": "my-label-class",
        "inner": "my-inner-class",
    }
)

# Using inline styles
dmc.Button(
    "Button with custom styles",
    styles={
        "root": {"backgroundColor": "red"},
        "label": {"color": "blue"},
        "inner": {"fontSize": 20},
    }
)
```

```python
# Using in the theme
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
    children={dmc.Button("Button")}
)

```


### classNames property

With the `classNames` property, you can add classes to inner elements of dmc components. It accepts a dictionary with 
selector names as keys and classes as values:

This example styles the Slider.  Find the selectors in [Slider Styles API](/components/slider#slider-selectors) section of the docs

.. exec::docs.styles-api.slider
    :code: false



The component is defined as:

```python
import dash_mantine_components as dmc

component = dmc.Slider(
    value=69,
    classNames={"bar": "dmc-bar", "thumb": "dmc-thumb"},
)
```

and include this in your `.css` file in the `/assets` folder:

```css
.dmc-bar {
    background-image: linear-gradient(to right, yellow, orange);
}

.dmc-thumb {
    border-color: orange;
    height: 20px;
    width: 20px;
    background-color: white;
}
```



### Styling with inline styles

`styles` prop can be used similarly to style individual elements inside a component. 

The `styles` property works similarly to `classNames`, but applies inline styles. Note that inline styles have higher
specificity than classes, so you cannot override them with classes without using `!important`. You cannot use 
pseudo-classes (for example, `:hover`, `:first-of-type`) and media queries with inline styles.

Here are three examples.  Please refer to the Styles API section on the component page.

#### Button

.. exec::docs.styles-api.button

#### Badge

.. exec::docs.styles-api.badge

#### TextInput

.. exec::docs.styles-api.input

> **styles property usage**
>
> While some examples may use the `styles` property for convenience, it is recommended to use `classNames` as the
> primary means of styling components, as it is more flexible and has better performance.

### Styles with Callbacks

.. exec::docs.styles-api.conditional


### Static classes

Every component that supports Styles API includes static classes that can be used to style components without using
`classNames` or `styles` properties. By default, static classes have `.mantine-{ComponentName}-{selector}` format. 
For example, the `root` selector of `dmc.Button` component will have `.mantine-Button-root` class.

You can use static classes to style a component with CSS:

Place this in the `.css` file in `/assets`:

```css
.mantine-Button-root {
    background-color: red;
}

.my-button.mantine-Button-root {
    background-color: yellow;
}
```

```python
import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Button("Yellow Button", className="my-button"),
        dmc.Button("Red Button"),
    ]
)

```
