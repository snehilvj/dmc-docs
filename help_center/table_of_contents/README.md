
## Examples of the TableOfContent component

### toc_multipage.py

This example shows how the `TableOfContents` is automatically updated when navigating to different pages of a multi page app.

This only works with multi-page apps using the Pages feature and in Dash>=3.0.0.  For other apps, use the `reinitialize` prop



### toc_multipage_appshell_header.py

This example shows how to handle scrolling when the app has a fixed header.

 - The `scrollMarginTop` CSS property is applied to headings so that when a TableOfContent item is clicked, the heading is not hidden behind the header.
 - The `offset` prop is passed to the `useScrollSpy` hook to track the correct heading when the app has a fixed header.
   It is set to the header height so the active item in the TableOfContents updates properly when scrolling.

### toc_tabs_reinitialize

Example showing how to refresh the `TableOfContents` when content is updated by
a callback using the `reinitialize` prop.

When using Dash >= 3.0.0, see the example using `target_id` for automatic updates instead.


### toc_tabs_target_id.py

Example showing how `target_id` automatically refreshes the table of contents
when content is updated by a callback.

Requires dash>=3.0.0

"""
