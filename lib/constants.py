import json

DMC_VERSION = "2.3.0"
MANTINE_VERSION = "8.3.1"
LATEST_RELEASE_ENDPOINT = "/release-2-3-0"


PAGE_TITLE_PREFIX = "Dash Mantine Components | "
PRIMARY_COLOR = "blue"
PROPS_TO_EXCLUDE = [
    "bd",
    "unstyled",
    "m",
    "my",
    "mx",
    "mt",
    "mb",
    "ms",
    "me",
    "ml",
    "mr",
    "p",
    "py",
    "px",
    "pt",
    "pb",
    "ps",
    "pe",
    "pl",
    "pr",
    "bg",
    "c",
    "opacity",
    "ff",
    "fz",
    "fw",
    "lts",
    "ta",
    "lh",
    "fs",
    "tt",
    "td",
    "w",
    "miw",
    "maw",
    "h",
    "mih",
    "mah",
    "bgsz",
    "bgp",
    "bgr",
    "bga",
    "pos",
    "top",
    "left",
    "bottom",
    "right",
    "inset",
    "display",
    "flex",
    "bdrs"
]

ALIGN_ITEMS_CSS_PROPERTY = ["stretch", "center", "flex-end", "flex-start"]
JUSTIFY_CONTENT_CSS_PROPERTY = ["flex-start", "center", "flex-end", "space-around", "space-between"]
FLEX_DIRECTION_CSS_PROPERTY = ["row", "column", "row-reverse", "column-reverse"]
FLEX_WRAP_CSS_PROPERTY = ["wrap", "nowrap", "wrap-reverse"]

with open('assets/llms.json', encoding='utf-8') as f:
    LLMS = json.load(f)
