"""
copy and paste printed table to .md files

create_styles_api_table(category, component)

Scrapes the styles table at: f"https://v6.mantine.dev/{category}/{component}/?t=styles-api"
"""


from utils import create_styles_api_table

print(create_styles_api_table("core", "scroll-area"))

