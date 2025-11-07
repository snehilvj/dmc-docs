from pathlib import Path
import frontmatter
import json

from replace_exec import replace_exec_directives
from replace_sourcetabs import replace_sourcetabs
from replace_kwargs import replace_kwargs
from replace_functions_as_props import replace_functions_as_props
from replace_styles_api_text import replace_styles_api_text
from replace_other_directives import replace_other_directives
from add_title_from_metadata import add_title_from_metadata
from lib.constants import MANTINE_VERSION, DMC_VERSION

# Define transformation pipeline
TRANSFORMS = [
    replace_exec_directives,
    replace_sourcetabs,
    replace_kwargs,
    replace_functions_as_props,
    replace_styles_api_text,
    replace_other_directives,
]

# Read and parse all markdown pages in the docs folder
pages = []
for file in Path("../docs").glob("**/*.md"):
    metadata, content = frontmatter.parse(file.read_text())
    metadata["content"] = content
    pages.append(metadata)

pages.sort(key=lambda x: (x.get("category", ""), x["name"]))

# Apply transformations
llms_text = ""
for page in pages:
    md_output = add_title_from_metadata(page)
    for transform in TRANSFORMS:
        md_output = transform(md_output)
    page["content"] = md_output
    llms_text += md_output

# add intro
intro = f"""
# Dash Mantine Components Documentation  

> Dash Mantine Components (DMC) is a component library for building modern web applications with [Dash](https://dash.plotly.com/).  
> It provides a wide range of accessible, themeable, and performant UI components built on top of the [Mantine](https://mantine.dev/) React library.
>
> This documentation applies to **DMC {DMC_VERSION}**, which wraps **Mantine {MANTINE_VERSION}**.  
> For additional details about underlying component behavior and styling, refer to the Mantine documentation: https://mantine.dev/
> All relative links in this file should be resolved against https://www.dash-mantine-components.com
>
> Assume the reader is a Dash developer familiar with callbacks and layout, but not necessarily with Mantine.

================================================================================

"""
llms_text = intro + llms_text

# Write text file
output_file = Path("../assets/llms.txt")
output_file.write_text(llms_text, encoding="utf-8")
print(f"Wrote {output_file.resolve()}")

# Write the JSON file
json_file = Path("../assets/llms.json")  # Using Path for consistency
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)
print(f"Wrote {json_file.resolve()}")

