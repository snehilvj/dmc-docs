---
name: Schedule
description: Schedule component with day, week, month and year views
endpoint: /components/schedule
package: dash_mantine_components
category: Miscellaneous
---

.. toc::
.. llms_copy::Schedule


### Usage

Schedule is a unified component that combines all schedule views (Day, Week, Month, Year) with automatic
view switching. Use the view selector in the header to switch between different views.

.. exec::docs.schedule.usage


.. sourcetabs::docs/schedule/data.py, docs/schedule/usage.py
    :defaultExpanded: true
    :withExpandedButton: true

###  Date and View

Use the `date` and `view` prop to set the initial date and view, or update it in a callback.

.. exec::docs.schedule.date_view

### Event click data
Use the `eventClickData` prop to access the event data when a user clicks an event in the Schedule. 

This example displays the complete event data in a modal.


.. exec::docs.schedule.eventclickdata


### View-specific props

Use `dayViewProps`, `weekViewProps`, `monthViewProps` and `yearViewProps` to pass props
to the corresponding view component, for example to set different time ranges for Day and Week views.

For more information on the props available, see the Mantine docs for each view component:

* [DayView](https://mantine.dev/schedule/day-view/) - Single day with time slots
* [WeekView](https://mantine.dev/schedule/week-view/) - Full week with time slots
* [MonthView](https://mantine.dev/schedule/month-view/) - Calendar month grid
* [YearView](https://mantine.dev/schedule/year-view/) - Full year overview


.. exec::docs.schedule.view_props


### Agenda view

Set `withAgenda` prop to display an "Agenda" button in the header of DayView, WeekView
and MonthView. When clicked, it opens an `AgendaView` showing events for the currently
visible date range.


.. exec::docs.schedule.agenda


### Recurring events

Schedule automatically expands recurring events for the visible date range in each view.
See [Recurring events guide](https://mantine.dev/schedule/recurring-events/) for full documentation.

.. exec::docs.schedule.recurring_events



### Background events

Set `display="background"` on an event to render it as a full-width, non-interactive
block behind regular events. Background events work in Day, Week, and Month views.

.. exec::docs.schedule.background


### Responsive layout

Schedule supports `layout="responsive"` prop that automatically switches between views
based on the container width. Resize the container below to see the view change.
On small screens, the month view is replaced with [MobileMonthView](https://mantine.dev/llms/schedule-mobile-month-view.md).
It takes `weekendDays` and `withWeekendDays` from `monthViewProps`, use `mobileMonthViewProps`
to override them or to set other mobile-specific options.


.. exec::docs.schedule.responsive

### Labels and Locale

Use [DatesProvider](/components/datesprovider) to set the locale and regional date settings for the calendar.

Use the labels prop to customize the text displayed in the Schedule component. You can provide only the labels you want to change. Any labels not specified will use their default values.

The following are the default labels used by Mantine:

```python
default_schedule_labels = {
    "today": "Today",
    "next": "Next",
    "previous": "Previous",
    "more": "More",
    "day": "Day",
    "week": "Week",
    "month": "Month",
    "year": "Year",
    "allDay": "All day",
    "weekday": "Weekday",
    "timeSlot": "Time slot",
    "selectMonth": "Select month",
    "selectYear": "Select year",
    "switchToDayView": "Switch to day view",
    "switchToWeekView": "Switch to week view",
    "switchToMonthView": "Switch to month view",
    "switchToYearView": "Switch to year view",
    "viewSelectLabel": "Calendar view",
    "noEvents": "No events",    
    "resource": "Resource",
    "resources": "Resources",
    "resourceSlot": "Resource time slot",
    "agenda": "Agenda",
}
```


.. exec::docs.schedule.locale


### Date and time considerations
When using `datetime.now()`, Python uses the server's date and time, not the user's browser time. The server may be in
a different timezone, and in some hosting environments the app may restart infrequently, meaning the date is not updated
until the next restart.

This can cause events to appear on the wrong date or at the wrong time.

If dates need to reflect the user's local time or update automatically, consider generating them in the browser using JavaScript.


### Styles API

.. styles_api_text::


**Schedule selectors**

| Selector | Static selector | Description |
|----------|----------------|-------------|
| root | .mantine-Schedule-root | Root element |
| desktopView | .mantine-Schedule-desktopView | Desktop view container (visible on large screens when layout="responsive") |
| mobileView | .mantine-Schedule-mobileView | Mobile view container (visible on small screens when layout="responsive") |
| dayView | .mantine-Schedule-dayView | DayView root element |
| dayViewInner | .mantine-Schedule-dayViewInner | DayView inner container |
| dayViewScrollArea | .mantine-Schedule-dayViewScrollArea | DayView scroll area component |
| dayViewAllDay | .mantine-Schedule-dayViewAllDay | DayView all-day events container |
| dayViewAllDayEvents | .mantine-Schedule-dayViewAllDayEvents | DayView all-day events wrapper |
| dayViewSlot | .mantine-Schedule-dayViewSlot | DayView individual time slot |
| dayViewSlots | .mantine-Schedule-dayViewSlots | DayView slots container |
| dayViewTimeSlots | .mantine-Schedule-dayViewTimeSlots | DayView time slots container |
| dayViewSlotLabel | .mantine-Schedule-dayViewSlotLabel | DayView time slot label |
| dayViewSlotLabels | .mantine-Schedule-dayViewSlotLabels | DayView slot labels container |
| dayViewBackgroundEvent | .mantine-Schedule-dayViewBackgroundEvent | DayView background event element |
| dayViewBackgroundEventResizeHandle | .mantine-Schedule-dayViewBackgroundEventResizeHandle | DayView resize handle of an interactive background event |
| dayViewDragPreview | .mantine-Schedule-dayViewDragPreview | DayView drag preview ghost element |
| weekView | .mantine-Schedule-weekView | WeekView root element |
| weekViewRoot | .mantine-Schedule-weekViewRoot | WeekView root container |
| weekViewHeader | .mantine-Schedule-weekViewHeader | WeekView header row |
| weekViewInner | .mantine-Schedule-weekViewInner | WeekView inner container |
| weekViewAllDaySlotsEvents | .mantine-Schedule-weekViewAllDaySlotsEvents | WeekView all-day events container |
| weekViewAllDaySlots | .mantine-Schedule-weekViewAllDaySlots | WeekView all-day slots container |
| weekViewAllDaySlotsList | .mantine-Schedule-weekViewAllDaySlotsList | WeekView all-day slots list |
| weekViewAllDaySlot | .mantine-Schedule-weekViewAllDaySlot | WeekView individual all-day slot |
| weekViewAllDaySlotsLabel | .mantine-Schedule-weekViewAllDaySlotsLabel | WeekView all-day slots label |
| weekViewScrollArea | .mantine-Schedule-weekViewScrollArea | WeekView scroll area |
| weekViewCorner | .mantine-Schedule-weekViewCorner | WeekView top-left corner |
| weekViewSlotLabels | .mantine-Schedule-weekViewSlotLabels | WeekView slot labels container |
| weekViewSlotLabel | .mantine-Schedule-weekViewSlotLabel | WeekView individual slot label |
| weekViewDayLabel | .mantine-Schedule-weekViewDayLabel | WeekView day label |
| weekViewDayWeekday | .mantine-Schedule-weekViewDayWeekday | WeekView weekday label |
| weekViewDay | .mantine-Schedule-weekViewDay | WeekView day column |
| weekViewDayNumber | .mantine-Schedule-weekViewDayNumber | WeekView day number |
| weekViewDaySlot | .mantine-Schedule-weekViewDaySlot | WeekView individual day slot |
| weekViewDaySlots | .mantine-Schedule-weekViewDaySlots | WeekView day slots container |
| weekViewWeekLabel | .mantine-Schedule-weekViewWeekLabel | WeekView week label |
| weekViewWeekNumber | .mantine-Schedule-weekViewWeekNumber | WeekView week number |
| weekViewBackgroundEvent | .mantine-Schedule-weekViewBackgroundEvent | WeekView background event element |
| weekViewDragPreview | .mantine-Schedule-weekViewDragPreview | WeekView drag preview ghost element |
| monthView | .mantine-Schedule-monthView | MonthView root element |
| monthViewScrollArea | .mantine-Schedule-monthViewScrollArea | MonthView scroll area wrapper |
| monthViewInner | .mantine-Schedule-monthViewInner | MonthView inner container |
| monthViewWeek | .mantine-Schedule-monthViewWeek | MonthView week row |
| monthViewDay | .mantine-Schedule-monthViewDay | MonthView day cell |
| monthViewDayLabel | .mantine-Schedule-monthViewDayLabel | MonthView day number label |
| monthViewWeekNumber | .mantine-Schedule-monthViewWeekNumber | MonthView week number |
| monthViewWeekday | .mantine-Schedule-monthViewWeekday | MonthView weekday name |
| monthViewWeekdays | .mantine-Schedule-monthViewWeekdays | MonthView weekdays row |
| monthViewWeekdaysCorner | .mantine-Schedule-monthViewWeekdaysCorner | MonthView top-left corner |
| monthViewEvents | .mantine-Schedule-monthViewEvents | MonthView events container |
| monthViewBackgroundEvent | .mantine-Schedule-monthViewBackgroundEvent | MonthView background event element |
| yearView | .mantine-Schedule-yearView | YearView root element |
| yearViewMonths | .mantine-Schedule-yearViewMonths | YearView months container |
| yearViewMonth | .mantine-Schedule-yearViewMonth | YearView individual month |
| yearViewWeekday | .mantine-Schedule-yearViewWeekday | YearView weekday name |
| yearViewDay | .mantine-Schedule-yearViewDay | YearView day cell |
| yearViewWeek | .mantine-Schedule-yearViewWeek | YearView week row |
| yearViewWeekNumber | .mantine-Schedule-yearViewWeekNumber | YearView week number |
| yearViewWeekdays | .mantine-Schedule-yearViewWeekdays | YearView weekdays row |
| yearViewWeekdaysCorner | .mantine-Schedule-yearViewWeekdaysCorner | YearView top-left corner |
| yearViewMonthCaption | .mantine-Schedule-yearViewMonthCaption | YearView month caption |
| yearViewDayIndicators | .mantine-Schedule-yearViewDayIndicators | YearView day indicators container |
| yearViewDayIndicator | .mantine-Schedule-yearViewDayIndicator | YearView individual day indicator |
| mobileMonthView | .mantine-Schedule-mobileMonthView | MobileMonthView root element |
| mobileMonthViewCalendar | .mantine-Schedule-mobileMonthViewCalendar | MobileMonthView calendar grid |
| mobileMonthViewWeekdays | .mantine-Schedule-mobileMonthViewWeekdays | MobileMonthView weekdays row |
| mobileMonthViewWeekday | .mantine-Schedule-mobileMonthViewWeekday | MobileMonthView individual weekday |
| mobileMonthViewWeekdaysCorner | .mantine-Schedule-mobileMonthViewWeekdaysCorner | MobileMonthView weekdays corner (for week numbers) |
| mobileMonthViewWeek | .mantine-Schedule-mobileMonthViewWeek | MobileMonthView week row |
| mobileMonthViewWeekNumber | .mantine-Schedule-mobileMonthViewWeekNumber | MobileMonthView week number |
| mobileMonthViewDay | .mantine-Schedule-mobileMonthViewDay | MobileMonthView day cell |
| mobileMonthViewDayIndicators | .mantine-Schedule-mobileMonthViewDayIndicators | MobileMonthView day indicators container |
| mobileMonthViewDayIndicator | .mantine-Schedule-mobileMonthViewDayIndicator | MobileMonthView individual day indicator |
| mobileMonthViewEventsList | .mantine-Schedule-mobileMonthViewEventsList | MobileMonthView events list container |
| mobileMonthViewEventsHeader | .mantine-Schedule-mobileMonthViewEventsHeader | MobileMonthView events list header |
| mobileMonthViewHeader | .mantine-Schedule-mobileMonthViewHeader | MobileMonthView header with back button and label |
| mobileMonthViewHeaderBackButton | .mantine-Schedule-mobileMonthViewHeaderBackButton | MobileMonthView header back button |
| mobileMonthViewHeaderLabel | .mantine-Schedule-mobileMonthViewHeaderLabel | MobileMonthView header month/year label |
| mobileMonthViewEvent | .mantine-Schedule-mobileMonthViewEvent | MobileMonthView event item |
| mobileMonthViewEventBody | .mantine-Schedule-mobileMonthViewEventBody | MobileMonthView event body button |
| mobileMonthViewEventTitle | .mantine-Schedule-mobileMonthViewEventTitle | MobileMonthView event title |
| mobileMonthViewEventTime | .mantine-Schedule-mobileMonthViewEventTime | MobileMonthView event time label |
| mobileMonthViewEventColor | .mantine-Schedule-mobileMonthViewEventColor | MobileMonthView event color indicator |
| mobileMonthViewNoEvents | .mantine-Schedule-mobileMonthViewNoEvents | MobileMonthView no events message |
| header | .mantine-Schedule-header | ScheduleHeader container |
| headerControl | .mantine-Schedule-headerControl | ScheduleHeader control element |
| viewSelect | .mantine-Schedule-viewSelect | ViewSelect element |
| monthYearSelectTarget | .mantine-Schedule-monthYearSelectTarget | MonthYearSelect target button |
| monthYearSelectDropdown | .mantine-Schedule-monthYearSelectDropdown | MonthYearSelect dropdown |
| monthYearSelectControl | .mantine-Schedule-monthYearSelectControl | MonthYearSelect control |
| monthYearSelectList | .mantine-Schedule-monthYearSelectList | MonthYearSelect list |
| monthYearSelectLabel | .mantine-Schedule-monthYearSelectLabel | MonthYearSelect label |
| event | .mantine-Schedule-event | ScheduleEvent element |
| eventInner | .mantine-Schedule-eventInner | ScheduleEvent inner element |
| eventResizeHandle | .mantine-Schedule-eventResizeHandle | ScheduleEvent resize handle element |
| moreEventsButton | .mantine-Schedule-moreEventsButton | MoreEvents button |
| moreEventsList | .mantine-Schedule-moreEventsList | MoreEvents list |
| moreEventsDropdown | .mantine-Schedule-moreEventsDropdown | MoreEvents dropdown |
| currentTimeIndicator | .mantine-Schedule-currentTimeIndicator | CurrentTimeIndicator container |
| currentTimeIndicatorLine | .mantine-Schedule-currentTimeIndicatorLine | CurrentTimeIndicator line |
| currentTimeIndicatorThumb | .mantine-Schedule-currentTimeIndicatorThumb | CurrentTimeIndicator thumb |
| currentTimeIndicatorTimeBubble | .mantine-Schedule-currentTimeIndicatorTimeBubble | CurrentTimeIndicator time bubble |
| agendaView | .mantine-Schedule-agendaView | AgendaView root element, shown when agenda is open |
| agendaViewHeader | .mantine-Schedule-agendaViewHeader | AgendaView header container |
| agendaViewHeaderLabel | .mantine-Schedule-agendaViewHeaderLabel | AgendaView date range label |
| agendaViewBody | .mantine-Schedule-agendaViewBody | AgendaView body container |
| agendaViewDateGroup | .mantine-Schedule-agendaViewDateGroup | AgendaView date group container |
| agendaViewDateHeader | .mantine-Schedule-agendaViewDateHeader | AgendaView date header text |
| agendaViewEvent | .mantine-Schedule-agendaViewEvent | AgendaView event item button |
| agendaViewEventBody | .mantine-Schedule-agendaViewEventBody | AgendaView event body container |
| agendaViewEventColor | .mantine-Schedule-agendaViewEventColor | AgendaView event color indicator |
| agendaViewEventTitle | .mantine-Schedule-agendaViewEventTitle | AgendaView event title text |
| agendaViewEventTime | .mantine-Schedule-agendaViewEventTime | AgendaView event time label |
| agendaViewNoEvents | .mantine-Schedule-agendaViewNoEvents | AgendaView no events message |


### Keyword Arguments
.. style_props_text::

#### Schedule

.. kwargs::Schedule
