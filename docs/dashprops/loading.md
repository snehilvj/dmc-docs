---
name: Dash Loading States
endpoint: /dash-loading
description: Learn how to show loading states in Dash apps using DMC components like Loader, Skeleton, and LoadingOverlay. Includes integration with dcc.Loading and examples of custom CSS-based spinners.

dmc: false
category: Dash
---


.. toc::
.. llms_copy::Dash Loading States


### DMC Loading components

DMC has several components that are often used to indicate a component's loading state:

- [Loader](/components/loader): A basic visual spinner (oval, bars, or dots) for simple loading states. Can be customized with size, color, and type.

- [LoadingOverlay](/components/loadingoverlay): Overlays a parent element with a loader, disabling user interaction to indicate a loading state, commonly used for forms.
- [Progress](/components/progress): A progress bar that shows task status and completion percentage. Customizable with value, color, label, and sections.
- [Button](/components/button) and [ActionIcon](/components/actionicon) (`loading` prop): Integrates a `Loader` into buttons and icons.  Disables Button while `loading=True`.
- [Skeleton](/components/skeleton): Creates placeholders resembling content layout to give users a preview while loading, reducing perceived wait time.


### With dcc.Loading

For greater control over when the DMC loading components are displayed and for how long, use the `dcc.Loading` component from
`dash-core-components`. DMC components such as `Skeleton`, `Loader`, `LoadingOverlay` can be displayed in the `custom_spinner` prop.

You can configure options such as:  

- `delay_show`: Specifies the wait time before displaying the loading component. This helps prevent flickering for fast-loading content.  
- `delay_hide`: Defines how long the loading component remains visible after loading completes, creating a smoother transition between the placeholder and final content.  
- `target_components`: Determines which components trigger the loader to display. This makes the loading effect triggered only by specific components rather than  being triggered by any of the children.

Refer to the [Dash Documentation](https://dash.plotly.com/dash-core-components/loading) for more details.

Here is an example of `delay_hide` prop in `dcc.Loading` to prevent the `Skeleton` from showing for a very short time.

.. exec::docs.skeleton.dccloading




### Custom CSS Loaders Using data-dash-is-loading


Dash automatically adds the attribute `data-dash-is-loading="true"` to components that are being updated in a callback.
You can use this attribute to apply custom loading indicators using CSS — no extra Python code or spinner components needed!


#### Basic Example

You can hide a component’s content and display a custom loader using just CSS:

```css
/* Hide the content while it's loading */
[data-dash-is-loading="true"] {
    visibility: hidden;
    position: relative;
}

/* Show a loader */
[data-dash-is-loading="true"]::before {
    content: "Loading...";
    visibility: visible;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}
```


In your Dash layout:

```python
dmc.Text(id="output-id", className="my-output")
```

In your `assets/style.css`:

```css
.my-output[data-dash-is-loading="true"]::before {
    /* Custom loader styles */
}
```

Now, whenever `output-id` is being updated by a callback, your custom loader will appear in place of the original content.

### Example with 3 custom spinners

This example has 3 custom spinner defined in the `.css` file in `/assets`.  The different loaders are applied to the
component based on the `className`.



.. exec::docs.dashprops.dash-is-loading
    :code: false

.. sourcetabs::docs/dashprops/dash-is-loading.py, assets/examples/loading-spinners.css
    :defaultExpanded: false
    :withExpandedButton: true

