---
name: Styles API
endpoint: /styles-api
head: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
description: With Styles API you can overwrite styles of inner elements in Mantine components with classNames or styles props.
package: dash_mantine_components
category: Theming
order: 4  # sets order in navbar section
---

.. toc::


### What is Styles API

The Styles API is a set of properties that allows you to customize the style of any element inside a DMC component. All 
DMC components that have styles support the Styles API.

### Styles API selectors

Every DMC component that supports the Styles API has a set of element names that can be used to apply styles to inner
elements inside the component. For simplicity, these elements names are called selectors in the documentation. You can
find selectors information in each component's documentation.

Example of `dmc.Button` component selectors:


| Name    | Static selector         | Description                                                 |
|:--------|:------------------------|:------------------------------------------------------------|
| root    | .mantine-Button-root    | Root element                                                |
| loader  | .mantine-Button-loader  | Loader component, displayed only when `loading` prop is set |
| section | .mantine-Button-section | Left and right sections of the button                       |
| inner   | .mantine-Button-inner   | Contains all other elements, child of the `root` element    |
| label   | .mantine-Button-label   | Button children                                             |



1) You can use the  selectors from the "Name" column in `classNames` and `styles` component props:

    
    ```python
    import dash_mantine_components as dmc
    
    # Using `classNames`
    dmc.Button(
        "Button with custom classes",
        classNames={
                    # define the classes in a .css file in /assets
            "root": "my-root-class",   
            "label": "my-label-class",
            "inner": "my-inner-class",
        }
    )
    
    # Using inline `styles`
    dmc.Button(
        "Button with custom styles",
        styles={
            "root": {"backgroundColor": "red"},
            "label": {"color": "blue"},
            "inner": {"fontSize": 20},
        }
    )
    
    
    ``` 

2) You can use the selectors from the "Name" column in the `theme` prop in the `MantineProvider`.
    
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


3) You can use the selectors from the "Static selector" column in a `.css` file in the `/assets` folder. 
    
    ```css
    .mantine-Button-root {
        background-color: red;        
    }
    
     .mantine-Button-label {
        color: blue
     }
     
     .mantine-Button-inner {
         font-size: 20
     }     
    ```
4) Don't use classes like `m_77c9d27d` that you can see when inspecting elements in the browser. These classes are not
static and can change in different versions. For more information, refer to the Component Classes section below. 
    

### classNames Property

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



### styles Property

`styles` prop can be used similarly to style individual elements inside a component. 

The `styles` property works similarly to `classNames`, but applies inline styles. Note that inline styles have higher
specificity than classes, so you cannot override them with classes without using `!important`. You cannot use 
pseudo-classes (for example, `:hover`, `:first-of-type`) and media queries with inline styles.

> Styles Property Usage
>
> While some examples may use the `styles` property for convenience, it is recommended to use `classNames` or `className`
> as the primary means of styling components, as it is more flexible and has better performance.

See some examples using the `styles` prop below.

### className Property (Static Classes)

Every component that supports the Styles API includes static classes that can be used to style components without relying on the `classNames` or `styles` properties. By default, static classes follow the format `.mantine-{ComponentName}-{selector}`. For example, the `root` selector of the `dmc.Button` component will have the class `.mantine-Button-root`.

Static classes make it easy to style components directly with CSS.

To demonstrate, add the following CSS to a `.css` file in the `/assets` directory of your Dash app:

```css
/* Global style for all dmc.Button components */
.mantine-Button-root {
    color: red;
}

/* Specific style for buttons with "my-button" class */
.my-button .mantine-Button-root {
    color: yellow;
}
```

Here’s how this CSS is applied to two buttons:

```python
import dash_mantine_components as dmc

component = dmc.Stack(
    [
        dmc.Button("Yellow Button", className="my-button"),
        dmc.Button("Red Button"),
    ]
)
```

#### Global vs. Specific Styling

By using global and specific styles together, you can define default styles for all components while customizing individual components as needed.

In the example above, note that:
- The Red Button is styled by the global rule `.mantine-Button-root`, which applies to all `dmc.Button` components. This rule sets its background color to red.
- The Yellow Button has a `className` of `'my-button'`, so it is styled by the more specific rule `.my-button. mantine-Button-root`, which overrides the global style and sets its background color to yellow.

Note that with components that are rendered within a portal, such as `Popover`, `Tooltip`, `Modal`, It is impossible to
style inner elements with static selectors because some elements will be rendered outside of the
component root and inner elements are not part of the component tree.  Either set `withinPortal=False` or use the
`classNames` or `styles` props.

### Component classes

If you inspect the browser, you will notice classes that look something like  `m_77c9d27d`. Those classes come from
Mantine and they are hashed class names generated at build time to ensure uniqueness and avoid naming collisions.

Note that these class names can change between different versions of Mantine as the styles are rebuilt or if the styles change.

Because of this, you shouldn't rely on or hardcode these specific class names in your code. Instead, you should:

1. Use the Styles API props (`classNames` and `styles`)
2. Use the static class names, such as `.mantine-Button-root` etc.

Example of what NOT to do:
```css
/* Don't do this - could break in future versions */
.m_77c9d27d {
  background: blue;
}
```

Instead do this:
```css
/* Do this - uses static class names */
.mantine-Button-root {
  background: blue;
}
```

Or:
```python
# Do this - uses Styles API
dmc.Button(
    "My Button",
    classNames={"root": "my-custom-button"}
)
```

### Data Attributes

Data attributes are custom attributes added to HTML elements that allow you to apply targeted styles or behavior based
on the component's state or configuration. In Dash Mantine Components, data attributes are dynamically added to elements
to reflect certain prop conditions or settings. This feature enables developers to write CSS rules that adapt to a 
component's state without needing to manage additional logic.

#### Using Data Attributes  

Data attributes follow the format `data-{attribute-name}` and can be used to style components directly in your CSS.

The data attributes are listed in the `Styles API`section for each component. Note that most components also have a
`data-dash-is-loading` attribute which is set based on the loading state coming from the dash renderer.

As an example, here are the data
attributes for `Button`:


| **Selector**   | **Attribute**         | **Condition**            | **Value**                       |
|----------------|-----------------------|---------------------------|---------------------------------|
| `root`         | `data-disabled`       | When `disabled` is set    | –                               |
| `root, label`  | `data-loading`        | When `loading` is set     | –                               |
| `root`         | `data-block`          | When `fullWidth` is set   | –                               |
| `root`         | `data-with-left-section`  | When `leftSection` is set  | –                               |
| `root`         | `data-with-right-section` | When `rightSection` is set | –                               |
| `section`      | `data-position`       | –                         | Section position: `left` or `right` |


Here’s how you can use data attributes to customize a `dmc.Button`:

```css

.dmc-data-attributes-demo[data-disabled="true"] {
    color: red;
    cursor: not-allowed;
}

.dmc-data-attributes-demo[data-loading="true"] {
    background-color: darkgray;
}

.dmc-data-attributes-demo .mantine-Button-section[data-position="left"] {
    color: var(--mantine-color-yellow-filled);
}
```

.. exec::docs.styles-api.data-attributes

### More Examples

Here are more examples.  Please refer to the Styles API section on each component's page for more information on the selectors.

#### Button

.. exec::docs.styles-api.button

#### Badge

.. exec::docs.styles-api.badge

#### TextInput

.. exec::docs.styles-api.input


#### Styles with Callbacks

.. exec::docs.styles-api.conditional


#### Slider

Don't miss this detailed example of styling a component in the [Styling the Slider](/components/slider#styling-the-slider) section.

- Dynamic Theming with `light-dark`: Styles adapt automatically to light and dark themes using the `light-dark` function and Mantine's color variables.  
- Track Customization: Adjusts the background color of the slider track to theme-specific colors.  
- Mark Customization:  
  - Changes the size, shape, and border of slider marks.  
  - Applies conditional styling to filled marks with the `[data-filled]` attribute.  
- Mark Label Customization: Modifies the font size, color, and spacing of labels displayed next to marks.  
- Thumb Customization: Customizes the size, background color, border, and shadow of the slider's draggable thumb.  

#### Tabs

See another detailed example of styling a component in the [Styling the Tabs](/components/tabs#styling-the-tabs) section.


#### DatePickerInput

This is an example of styling elements that are in a portal, such as Popover, Modal, Tooltip.  By default, the dropdown
calendar is rendered using the Popover component and `withinPortal=True`.  It's necessary to use the `classNames` or the
`styles` properties because the static selectors cannot target elements in the portal.


.. exec::docs.styles-api.datepickerinput


