from pathlib import Path
import frontmatter

from replace_exec import replace_exec_directives
from replace_sourcetabs import replace_sourcetabs
from replace_kwargs import replace_kwargs
from replace_functions_as_props import replace_functions_as_props
from replace_styles_api_text import replace_styles_api_text
from replace_other_directives import replace_other_directives
from add_title_from_metadata import add_title_from_metadata

MANTINE_VERSION = "v8"
DMC_VERSION = "v2.3.0"

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
    if metadata.get("category") != "Releases":
        metadata["content"] = content
        pages.append(metadata)

pages.sort(key=lambda x: (x.get("category", ""), x["name"]))

# Apply transformations
llm_text = ""
for page in pages:
    md_output = add_title_from_metadata(page)
    for transform in TRANSFORMS:
        md_output = transform(md_output)
    llm_text += md_output

# add intro
intro = f"""
# Dash Mantine Components Library - Complete Documentation  

Dash Mantine Components (DMC) is a component library for building modern web applications with [Dash](https://dash.plotly.com/).  
It provides a wide range of accessible, themeable, and performant UI components built on top of the [Mantine](https://mantine.dev/) React library.

This documentation applies to **DMC {DMC_VERSION}**, which wraps **Mantine {MANTINE_VERSION}**.  
For additional details about underlying component behavior and styling, refer to the Mantine documentation: https://mantine.dev/

The following sections describe DMC components, their props, usage examples in Python Dash, and relevant style and theme APIs.  
All examples use Python Dash syntax. JavaScript or CSS examples may also be included where appropriate.

Assume the reader is a Dash developer familiar with callbacks and layout, but not necessarily with Mantine.

================================================================================

"""
llm_text = intro + llm_text


output_file = Path("../assets/llm.txt")
output_file.write_text(llm_text, encoding="utf-8")
print(f"Wrote {output_file.resolve()}")



## test string
md_input = """
### Simple Example

.. exec::docs.burger.simple

Some text after.

.. exec::docs.dashprops.slider_label
    :code: false

More text.

.. functions_as_props::


.. exec::docs.compositechart.line-color-light-dark
    :code: false


### Example
.. functions_as_props::

.. sourcetabs::docs/dashprops/slider_label.py, assets/examples-js/celcius_label.js
    :defaultExpanded: true
    :withExpandedButton: true

.. kwargs::Burger
"""
