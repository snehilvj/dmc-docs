---
name: Lightbox
description: Full-screen photo and image viewer  with carousel navigation.
endpoint: /components/lightbox
package: dash_mantine_components
category: Data Display
---

.. toc::
.. llms_copy::Lightbox


### Simple Example

`Lightbox` is a full-screen photo and image viewer built on [embla carousel](https://www.embla-carousel.com/).
Click any image to open the lightbox:

.. exec::docs.lightbox.usage

### Slide data

The `slides` prop accepts a list of dictionaries containing slide data. There are two slide types: image (default) and video.

```python 
slides = [
    # Image slide (default type)
    {
        "src": "image.png",  # Image URL
        "alt": "Mountain lake",  # Alt text, always set it for screen readers
        "caption": "Mountain lake at sunrise",  # Caption displayed below the slide
        "thumbSrc": "image-small.png",  # Custom thumbnail URL, src is used if not set        
        "srcSet": "image-2x.png 2x",  # Optional srcset for responsive images
        "sizes": "(max-width: 600px) 100vw, 50vw",  # Optional sizes attribute
        "loading": "lazy",  # Optional loading attribute
    },

    # Video slide
    {
        "type": "video",
        "src": "video.mp4",
        "label": "Product demo",  # Accessible video label
        "poster": "poster.png",  # Poster image, also used as thumbnail
        "thumbSrc": "poster-small.png",  # Custom thumbnail URL, poster is used if not set       
        "autoPlay": True,  # Auto-play when the slide becomes active
        "tracks": [
            {
                "src": "captions.vtt",
                "kind": "captions",
                "srcLang": "en",
                "label": "English",
            }
        ],
    },
]
```



### Video slides

Set `type: 'video'` on a slide to render a `<video>` element. Videos are paused
when the slide is changed. The `poster` image is used as the thumbnail.

.. exec::docs.lightbox.video

### All Features Example

This example sets `Zoom`, `thumbnails`, `fullscreen`, `download` and `loop` features.

#### Zoom

Enable image zoom with the `withZoom` prop. On desktop, click an image to zoom in, scroll wheel to
adjust zoom level, and drag or use arrow keys to pan when zoomed. On mobile, double-tap to zoom and
pinch to adjust. Use `zoomMaxScale` to change the maximum zoom scale (`3` by default).


#### Thumbnails

Set `withThumbnails` to display the thumbnail strip at the bottom. Users can hide it
with the `T` key or the toolbar button:

#### Download
Set `withDownload=True` to adds download button to toolbar.  Default is false

#### Fullscreen
Set `withFullscreen=True` to add a fullscreen toggle to toolbar.  Default is false

#### Loop navigation

Set `loop=True` to enable infinite wrapping at the ends of the slide list:


.. exec::docs.lightbox.allfeatures


### Image loading

By default, only the image of the active slide is loaded when the lightbox is opened, other images
and thumbnails are loaded lazily. Thumbnails use `src` if `thumbSrc` is not set, set `thumbSrc`
to a smaller image if the originals are large.

Set the `loading` property on an image slide to change this, for example to preload
the next slide:

```python
slides = [
  { 'src': 'image-1.png', 'alt': 'First' },
  { 'src': 'image-2.png', 'alt': 'Second', 'loading': 'eager' },
]
```

### Slide transition

By default, slides are changed instantly when arrow buttons or keyboard are used.
Set `withSlideTransition` to animate slide changes. Use `emblaOptions={{ duration: 40 }}`
to change the animation speed. Embla duration is not in milliseconds, values between 20 and 60
are recommended:


.. exec::docs.lightbox.transition



### Embla options

Use `emblaOptions` prop to pass [options](https://www.embla-carousel.com/api/options/) to
the embla carousel. `loop` and `startIndex` options cannot be set this way, use `loop` and
`currentIndex` props instead:

```python
dmc.Lightbox(
    slides=[],
    emblaOptions={'dragFree': False, 'duration': 30, 'align': 'center'}
)
```
###  z-index

`zIndex` controls the `z-index` of the overlay and the content elements, `400` by default:

```python
dmc.Lightbox(
    slides=[],
    zIndex=1000
)
```

### Open close transition


Use `transitionProps` to change the animation of the content, it accepts the same options
as the [Transition](https://mantine.dev/core/transition/) component. The overlay always fades. To change only
the duration (`200` by default), use `transitionDuration`:


.. exec::docs.lightbox.openclose_transition

### Disable animations
Set `transitionProps={ 'duration': 0 }` to open and close the lightbox without animation

### Swipe to close
On mobile, swiping down closes the lightbox. This is enabled by default. Set `closeOnSwipeDown=False` to disable.

```python
dmc.Lightbox(
    slides=[],
    closeOnSwipeDown=False
)
```

### Click outside to close
Set `closeOnClickOutside=True` to close the lightbox when the empty space around the slide content is clicked. It is
disabled by default to prevent accidental closing.


```python
dmc.Lightbox(
    slides=[],
    closeOnClickOutside=True
)
```


### Accessibility

* Always set the `alt` property on image slides and the `label` property on video slides and custom toolbar items
* The lightbox has `role="dialog"` and is labelled with `labels.lightboxLabel`, set `aria-label` to change the label of a single lightbox
* Focus is trapped inside the lightbox and is returned to the previously focused element when it is closed
* Slide changes are announced with `aria-live="polite"`
* Inactive slides are hidden from screen readers and removed from the tab order


### Labels for screen readers

Use `labels` prop to translate the lightbox. Labels that are not set fall back
to the default English values.

```python
labels = {
    "lightboxLabel": "Galerie",
    "slideLabel": {"function": "lightboxSlideLabel"},
    "slidesLabel": "Bilder",
    "thumbnailLabel": {"function": "lightboxThumbnailLabel"},
    "previousSlideLabel": "Vorheriges Bild",
    "nextSlideLabel": "Nächstes Bild",
    "enterFullscreenLabel": "Vollbild aktivieren",
    "exitFullscreenLabel": "Vollbild beenden",
    "showThumbnailsLabel": "Miniaturansichten anzeigen",
    "hideThumbnailsLabel": "Miniaturansichten ausblenden",
    "downloadLabel": "Herunterladen",
    "closeLabel": "Schließen",
}
```


.. functions_as_props::

```js
var dmcfuncs = window.dashMantineFunctions = window.dashMantineFunctions || {};

dmcfuncs.lightboxSlideLabel = function (index, total) {
    return `Bild ${index} von ${total}`;
}

dmcfuncs.lightboxThumbnailLabel = function (index) {
    return `Zu Bild ${index} wechseln`;
}
```


Here are the default labels set by Mantine:

```tsx
export const DEFAULT_LABELS: LightboxLabels = {
  lightboxLabel: 'Gallery',
  slideLabel: (index, total) => Slide ${index} of ${total},
  slidesLabel: 'Slides',
  previousSlideLabel: 'Previous slide',
  nextSlideLabel: 'Next slide',
  thumbnailLabel: (index) => Go to slide ${index},
  enterFullscreenLabel: 'Enter fullscreen',
  exitFullscreenLabel: 'Exit fullscreen',
  showThumbnailsLabel: 'Show thumbnails',
  hideThumbnailsLabel: 'Hide thumbnails',
  downloadLabel: 'Download',
  closeLabel: 'Close',
};
```


### Keyboard shortcuts

Set `withKeyboardEvents={false}` to disable all shortcuts except `Escape`. Shortcuts are ignored
while focus is inside an input, a video or an interactive element of a custom slide:
| Key          | Description                                   |
| ------------ | --------------------------------------------- |
| `Escape`     | Close lightbox                                |
| `ArrowLeft`  | Previous slide, pan left when zoomed          |
| `ArrowRight` | Next slide, pan right when zoomed             |
| `ArrowUp`    | Pan up when zoomed                            |
| `ArrowDown`  | Pan down when zoomed                          |
| `F`          | Toggle fullscreen (requires `withFullscreen`) |
| `T`          | Toggle thumbnails (requires `withThumbnails`) |
| `Z`          | Toggle zoom (requires `withZoom`)             |



### Styles API

.. styles_api_text::

#### Lightbox selectors

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-Lightbox-root | Root element – holds CSS variables, renders overlay and content |
| overlay | .mantine-Lightbox-overlay | Background overlay behind the lightbox |
| content | .mantine-Lightbox-content | Full-screen dialog container with all lightbox controls |
| toolbar | .mantine-Lightbox-toolbar | Top toolbar wrapper |
| toolbarGroup | .mantine-Lightbox-toolbarGroup | Left/right toolbar button group |
| toolbarButton | .mantine-Lightbox-toolbarButton | Individual toolbar action button |
| counter | .mantine-Lightbox-counter | Slide counter text (e.g. "2 / 5") |
| slides | .mantine-Lightbox-slides | Slides area wrapper |
| slidesViewport | .mantine-Lightbox-slidesViewport | Embla viewport (overflow hidden) |
| slidesContainer | .mantine-Lightbox-slidesContainer | Embla container (flex row of slides) |
| slide | .mantine-Lightbox-slide | Individual slide wrapper |
| slideImage | .mantine-Lightbox-slideImage | Image element inside a slide |
| slideVideo | .mantine-Lightbox-slideVideo | Video element inside a slide |
| thumbnails | .mantine-Lightbox-thumbnails | Thumbnails strip wrapper |
| thumbnailsViewport | .mantine-Lightbox-thumbnailsViewport | Thumbnails Embla viewport |
| thumbnailsContainer | .mantine-Lightbox-thumbnailsContainer | Thumbnails Embla container |
| thumbnail | .mantine-Lightbox-thumbnail | Individual thumbnail button |
| thumbnailImage | .mantine-Lightbox-thumbnailImage | Image inside a thumbnail |
| navigation | .mantine-Lightbox-navigation | Navigation arrows wrapper |
| navigationButton | .mantine-Lightbox-navigationButton | Previous/next navigation button |
| caption | .mantine-Lightbox-caption | Caption text below the active slide |
| closeButton | .mantine-Lightbox-closeButton | Close button |

#### Lightbox CSS variables

| Selector | Variable | Description |
|----------|----------|-------------|
| root | --lightbox-transition-duration | Controls transition duration of all animations |
| root | --lightbox-overlay-color | Controls background overlay color |
| root | --lightbox-z-index | Controls `z-index` of the overlay and content elements |
| root | --lightbox-toolbar-height | Controls toolbar height |
| root | --lightbox-thumbnails-height | Controls thumbnails strip height |

#### Lightbox data attributes

| Selector | Attribute | Condition | Value |
|----------|-----------|-----------|-------|
| thumbnail | data-active | Thumbnail corresponds to the currently active slide | - |
| navigationButton | data-inactive | Navigation button is disabled (first/last slide without loop) | - |
| slideImage | data-zoom-enabled | `withZoom` prop is set on the lightbox | - |
| slideImage | data-zoomed | Image is currently zoomed in | - |
| slideImage | data-dragging | Image is being dragged while zoomed | - |


### Keyword Arguments
.. style_props_text::

#### Lightbox

.. kwargs::Lightbox


