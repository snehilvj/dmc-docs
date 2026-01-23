import json
import os

DMC_VERSION = "2.5.0"
MANTINE_VERSION = "8.3.13"
LATEST_RELEASE_ENDPOINT = "/release-2-5-0"


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

# Get path to assets/llms.json relative to this file
constants_dir = os.path.dirname(os.path.abspath(__file__))
llms_path = os.path.join(constants_dir, '../assets/llms.json')

with open(llms_path, encoding='utf-8') as f:
    LLMS = json.load(f)
    NAME_CONTENT_MAP = {item["name"]: item["content"] for item in LLMS}
