---
name: Date Pickers Overview
endpoint: /datepickers-overview
description: This guide gives an overview of Date and Time components available in Dash Mantine components.
package: dash_mantine_components
category: Date Pickers
order: 1  # sets order in navbar section
---

.. toc::


The Mantine Date pickers  makes it easy for users to jump several months or years into the future or past:

.. image::https://raw.githubusercontent.com/snehilvj/dash-mantine-components/master/assets/datepicker.gif
    :w: 200px


### Date Pickers


#### DatePicker

[DatePicker](/components/datepicker)
This is a date picker with a calendar only and it does not have an input field.  
Note: Many `DatePicker` props (for example,  `minDate`, `maxDate`, `excludeDates`, `allowLevelChange`, `firstDayOfWeek`,
`dropdownType`) apply across other Mantine date and time picker components. Refer to this page for a comprehensive list
and detailed explanations of these shared props.


#### DatePickerInput

[DatePickerInput](/components/datepickerinput): Select single dates, multiple dates (`type="multiple"`), or date ranges (`type="range"`). This option does not allow free text input directly within the component itself.

#### DateInput

[DateInput](/components/datepickerinput): Allows typing dates as text, with a calendar for date  selection. It's a good choice when you want the flexibility of keyboard input alongside the option of a graphical date picker.

#### MonthPickerInput

[MonthPickerInput](/components/monthpickerinput): Use when only the month value is needed.

#### YearPickerInput
[YearPickerInput](/components/yearpickerinput): Use when only the year value is needed.



### Time Pickers
#### TimeInput
[TimeInput](/components/timeinput): Basic text input for time. Simple for entering times like "12:30".

#### TimePicker
[TimePicker](/components/timepicker): Advanced time selection with features like dropdowns for hours, minutes, seconds, and 12-hour/24-hour formats. Use it when more robust and interactive time input is needed. 

### TimeGrid
[TimeGrid](/components/timegrid)

### Combined Date & Time Pickers

#### DateTimePicker
DateTimePicker: Selects both date and time using a combined interface. Ideal for scheduling and events requiring specific date and time information. 
