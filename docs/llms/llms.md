---
name: LLMs.txt
endpoint: /llms
description: Dash Mantine Components provides LLM-friendly documentation to help AI tools like Cursor, Windsurf, GitHub Copilot, ChatGPT, and Claude understand and work with the DMC library.
dmc: false
---
.. toc::


### Documentation

The complete DMC documentation is available in an LLM-friendly format.

- [View DMC llms.txt](https://www.dash-mantine-components.com/assets/llms.txt)
- [View DMC llms.json](https://www.dash-mantine-components.com/assets/llms.json)
- [View Mantine v9 llms.txt](https://mantine.dev/llms.txt)

DMC v3 is based on Mantine v9. Mantine's documentation, MCP server, and skills can help AI tools understand component APIs and behavior. See the [Mantine guide for LLMs](https://mantine.dev/llms.txt) for details.

### Getting Documentation for AI Tools

You can provide documentation to AI tools in several ways.

#### Complete documentation

Reference the [DMC llms.txt](https://www.dash-mantine-components.com/assets/llms.txt) URL in your prompt or add it to your coding tool's documentation sources.

For best results, specify that you are using DMC v3 and ask the AI to use DMC's Python API rather than Mantine's React API. Mantine documentation can help explain component behavior, but check the DMC documentation for supported props and Dash-specific usage.

#### Individual documentation pages

You can get a text version of any DMC documentation page by adding `.txt` to its URL.

For example, the text version of the Chip documentation is available at [components/chip.txt](https://www.dash-mantine-components.com/components/chip.txt).

Each documentation page also includes a **Copy for LLMs** button that copies the page content in a format suitable for AI tools. Use this when you only need to provide documentation for a few components.

#### Customized documentation

You can create a smaller `llms.txt` file containing only the components and categories relevant to your project. This can reduce unrelated content and help AI tools focus on the APIs you use.

Options for creating a custom file are provided below.


.. exec::docs.llms.llms_download
    :code: false

### Example Prompts

- "Using DMC v3, create a dark mode toggle with MantineProvider."
- "Build a responsive layout using DMC v3. Use Mantine v9 documentation for component behavior and the DMC docs for Python props and examples."
- "Show me how to use AppShell with a collapsible navbar in DMC."
- "Use DMC components to align an input and a button in a flex container."
- "Refer only to these DMC documentation pages when generating examples: [paste documentation URLs]."

### Documentation Generation

The LLM documentation is generated from the DMC documentation source and updated with each release.

### Creating a Custom llms.txt File

Using only the documentation you need can make AI responses more focused.

#### Option 1: Use the customization app

Use the interactive tool below to select component categories, such as layout, inputs, or feedback, or individual components such as `AppShell`, `Card`, or `Button`. Then download your customized file.

#### Option 2: Build your own from llms.json

Use the structured data in [llms.json](https://www.dash-mantine-components.com/assets/llms.json) to create a custom file.

Each entry represents a documentation page and includes fields such as `name`, `description`, `category`, and `content`. You can filter and combine entries based on the components or categories relevant to your project.

#### Option 3: Copy individual pages

Use the **Copy for LLMs** button on a documentation page to copy its content directly into an AI conversation. This is useful when you only need information about one or two components.

### Contributing

If you find issues with the LLM documentation or have suggestions for improvement, please [open an issue](https://github.com/snehilvj/dmc-docs/issues) in the documentation repository.