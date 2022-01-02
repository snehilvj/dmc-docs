components = [
    "Accordion",
    "Affix",
    "Alert",
    "Badge",
    "Button",
    "Checkbox",
    "Chips",
    "DatePicker",
    "DateRangePicker",
    "Divider",
    "Drawer",
    # "Image",
    "Modal",
    # "MultiSelect",
    "Notifications",
    # "Paper",
    # "Prism",
    # "Progress",
    # "RadioGroup",
    # "SegmentedControl",
    # "Select",
    # "Slider",
    # "Spoiler",
    # "Switch",
    # "Table",
    # "Tabs",
    # "Text",
    # "TextInput",
    # "Title",
    # "Tooltip",
]


def parse_apidocs(docs):
    header, api = docs.split("Keyword arguments:")
    desc = "\n".join(header.split("\n")[1:])
    return desc, api.strip()
