import dash_mantine_components as dmc

groceries = {
    "Apples": {
        "emoji": "🍎",
        "description": "Crisp and juicy snacking delight",
    },
    "Bread": {
        "emoji": "🍞",
        "description": "Freshly baked daily essential",
    },
    "Bananas": {
        "emoji": "🍌",
        "description": "Perfect for a healthy breakfast",
    },
    "Eggs": {
        "emoji": "🥚",
        "description": "Versatile protein source for cooking",
    },
    "Broccoli": {
        "emoji": "🥦",
        "description": "Nutrient-rich green vegetable",
    },
}

component = dmc.TagsInput(
    label="Groceries",
    placeholder="Pick tag from list or type to add new",
    data=list(groceries.keys()),
    maxDropdownHeight=300,
    renderOption={
        "function": "renderGroceryOption",
        "options": {"data": groceries},
    },
)
