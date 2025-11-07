---
name: MiniCalendar
description: Compact calendar to display a small number of days in a row
endpoint: /components/mini-calendar
package: dash_mantine_components
category: Date Pickers
---

.. toc::
.. llms_copy::MiniCalendar

### Simple Example

.. exec::docs.minicalendar.simple

### Number of days

Use numberOfDays prop to control how many days are displayed at once. The default value is 7.


.. exec::docs.minicalendar.numberofdays

### getDayProps

.. functions_as_props::  

Use `getDayProps` to add custom props to days, for example, assign styles to weekends:


.. exec::docs.minicalendar.getdayprops
    :code: false

.. sourcetabs::docs/minicalendar/getdayprops.py, assets/examples-js/getdayprops.js
    :defaultExpanded: true
    :withExpandedButton: true


### Min and max dates
Use `minDate` and `maxDate` props to limit date selection:


.. exec::docs.minicalendar.minmax

### Localization
You can change localization both on component level with locale prop and globally with [DatesProvider](/components/datesprovider).


.. exec::docs.minicalendar.locale








### Styles API

.. styles_api_text::

Here’s your content reformatted as Markdown tables:

#### MiniCalendar selectors

| Selector  | Static selector                   | Description                                                                |
| --------- | --------------------------------- | -------------------------------------------------------------------------- |
| root      | `.mantine-MiniCalendar-root`      | Root element                                                               |
| control   | `.mantine-MiniCalendar-control`   | Button in the dropdown which is used to select hours/minutes/seconds/am-pm |
| days      | `.mantine-MiniCalendar-days`      | Days container                                                             |
| day       | `.mantine-MiniCalendar-day`       | Single day element                                                         |
| dayMonth  | `.mantine-MiniCalendar-dayMonth`  | Day element in month view                                                  |
| dayNumber | `.mantine-MiniCalendar-dayNumber` | Day number element                                                         |

---

#### MiniCalendar CSS variables

| Selector | Variable                    | Description                                       |
| -------- | --------------------------- | ------------------------------------------------- |
| root     | `--mini-calendar-font-size` | Controls size of all elements (based on em units) |

---

#### MiniCalendar data attributes

| Selector | Attribute | Condition                                              | Value                |
| -------- | --------- | ------------------------------------------------------ | -------------------- |
| control  | disabled  | Next/previous range is after maxDate or before minDate | –                    |
| control  | direction | –                                                      | `previous` or `next` |
| day      | selected  | The day matches the value                              | –                    |
| day      | disabled  | The day is before minDate or after maxDate             | –                    |

---


### Keyword Arguments
.. style_props_text::

#### MiniCalendar

.. kwargs::MiniCalendar

