---
name: MediaQuery
section: Layout
head: Apply styles to children if media query matches.
description: Use MediaQuery component to apply styles to your components if media query matches. It can be used to make responsive apps easily.
component: MediaQuery
props: false
---

##### Simple

MediaQuery component adds styles to child element if given media query matches.

.. exec::docs.mediaquery.query

##### LargerThan, SmallerThan

`largerThan` and `smallerThan` props lets you use Mantine's theme.breakpoints. Change the width of your browser window 
to see this component in action.

.. exec::docs.mediaquery.breakpoints

These docs are made responsive by using MediaQuery wherever possible.
