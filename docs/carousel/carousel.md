---
name: Carousel
description: Use the Carousel component to cycle through elements like a slideshow.
endpoint: /components/carousel
package: dash_mantine_components
category: Data Display
---

.. toc::



### CSS Extensions

.. admonition::CSS Extensions
   :icon: radix-icons:info-circled
   :color: red

   Carousel require additional CSS styles.

The Carousel component require an additional CSS stylesheet.  See the [Getting Started](/getting-started) section for more information.

Be sure to include:
```python
app = Dash(external_stylesheets=[dmc.styles.CAROUSEL])
```
Or, if you want to include all optional stylesheets:
```python
app = Dash(external_stylesheets=dmc.styles.ALL)
```


### Simple Example

.. exec::docs.carousel.simple


### Options


.. exec::docs.carousel.interactive
    :code: false

### Size and Gap

Set `slideSize` and `slideGap` on `Carousel` component to control size and gap of every slide:

.. exec::docs.carousel.size_gap

### Responsive styles

`slideSize` and `slideGap` props work the same way as `style` props, you can pass an object with values for different breakpoints:


.. exec::docs.carousel.responsive

### Drag free

`dragFree` will disable slides snap points – user will be able to stop dragging at any position:

.. exec::docs.carousel.drag_free

### Vertical orientation

Carousel with `orientation="vertical"` requires `height` prop to be set:

.. exec::docs.carousel.vertical


### Controls icons
You can replace default next/previous controls icons with any component:


.. exec::docs.carousel.controls_icons

### Autoplay
Enable autoplay by setting `autoplay=True` or by passing in a `dict` with options. Refer to [Embla Carousel Autoplay Options](https://www.embla-carousel.com/plugins/autoplay/#options) to learn more.

.. exec::docs.carousel.autoplay
Here’s an example of passing props to the Embla component. In this example, the `delay` is set to 2000ms, and autoplay pauses when hovering over a slide:

```python
autoplay={"delay": 2000, "stopOnMouseEnter": True, "stopOnInteraction":False}

```
.. exec::docs.carousel.autoplay_props

### Styles API

Carousel supports Styles API, you can add styles to any inner element of the component with `classNames` prop. Refer to the  [Styles API documentation](/styles-api) to learn more.

### Indicator styles
This example styles the indicators to emphasize the active slide.

.. exec::docs.carousel.indicator_styles

Put the following in a .css file in the `assets` folder:

```css
.dmc-indicator {
  width: 12px;
  height: 4px;
  transition: width 250ms ease;

  &[data-active] {
    width: 40px;
  }
}
```

### Hide inactive controls

.. exec::docs.carousel.hide_inactive_controls

Put the following in a .css file in the `assets` folder:

```css
.dmc-control {
  &[data-inactive] {
    opacity: 0;
    cursor: default;
  }
}
```

### Show controls on hover

.. exec::docs.carousel.show_controls_on_hover

Put the following in a .css file in the `assets` folder:
```css

.dmc-controls {
  transition: opacity 150ms ease;
  opacity: 0;
}

.dmc-root {
  &:hover {
    .dmc-controls {
      opacity: 1;
    }
  }
}
```

### Set initial slide

To set the initial slide to display, use the index number of the slide.

.. exec::docs.carousel.initial

### Active prop for callbacks

The `active` prop represents the index of the currently displayed slide and can be used to trigger Dash callbacks. Note
that this prop is read-only. To set the initially displayed slide, use the `initialSlide` prop instead.

In this example, the callback updates the current page in the `Pagination` component based on the active slide.

.. exec::docs.carousel.active

### Example Image Carousel

.. exec::docs.carousel.images


### Example Card Carousel

.. exec::docs.carousel.cards

### Limitation: Carousel in Tabs

When a Carousel is placed inside a tab, it may not render correctly. For more details, refer to [GitHub Issue #299]((https://github.com/snehilvj/dash-mantine-components/issues/299). 
As a workaround, you can update the carousel within the tabs using a callback.

Be sure to give a unique id to each carousel in the app.


.. exec::docs.carousel.tabs

### Styles API

#### Carousel selectors

| Selector   | Static selector              | Description                                              |
|------------|------------------------------|----------------------------------------------------------|
| root       | .mantine-Carousel-root       | Root element                                             |
| slide      | .mantine-Carousel-slide      | Carousel.Slide root element                              |
| container  | .mantine-Carousel-container  | Slides container                                         |
| viewport   | .mantine-Carousel-viewport   | Main element, contains slides container and all controls |
| controls   | .mantine-Carousel-controls   | Next/previous controls container                         |
| control    | .mantine-Carousel-control    | Next/previous control                                    |
| indicators | .mantine-Carousel-indicators | Indicators container                                     |
| indicator  | .mantine-Carousel-indicator  | Indicator button                                         |

#### Carousel CSS variables

| Selector | Variable                   | Description                                                |
|----------|----------------------------|------------------------------------------------------------|
| root     | --carousel-control-size    | Controls `width` and `height` of the next/previous buttons |
| root     | --carousel-controls-offset | Controls offsets of the next/previous buttons              |
| root     | --carousel-height          | Controls height of the carousel                            |

#### Carousel data attributes

| Selector   | Attribute                    | Condition                                | Value                        |
|------------|------------------------------|------------------------------------------|------------------------------|
| root       | data-orientation             | –                                        | Value of `orientation` prop  |
| root       | data-include-gap-in-size     | `includeGapInSize` prop is set           | –                            |
| control    | data-inactive                | No previous/next slides are available    | –                            |
| indicator  | data-active                  | Associated slide is active               | –                            |



### Keyword Arguments

#### Carousel

.. kwargs::Carousel


#### CarouselSlide

.. kwargs::CarouselSlide

