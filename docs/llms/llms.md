---
name: LLMs.txt
endpoint: /llms
description: Dash Mantine Components provides LLM-friendly documentation to help AI tools like Cursor, Windsurf, GitHub Copilot, ChatGPT, and Claude understand and work with the DMC library.
dmc: false
---
.. toc::


`llms.txt` documentation is updated with every DMC release.


### Complete Documentation

Full DMC documentation following the [LLMs.txt](https://llmstxt.org/) standard (~1.6MB)

* [View online](https://www.dash-mantine-components.com/assets/llms.txt)
* [Download](https://www.dash-mantine-components.com/assets/llms.txt)

You can also find the upstream Mantine LLMs document:
* [View Mantine llms.txt online](https://mantine.dev/llms.txt)

### Usage with AI Tools

#### Cursor

In Cursor, you can reference the documentation using the `@Docs` feature:

1. Type `@Docs` in your prompt
2. Reference the DMC documentation URL: `https://www.dash-mantine-components.com/assets/llms.txt`
3. Ask questions about DMC components, styling, or implementation

#### Windsurf

For Windsurf users:

1. Reference the documentation using `@https://www.dash-mantine-components.com/assets/llms.txt`
2. Or add it to your `.windsurfrules` file for persistent access

#### ChatGPT & Claude

When using ChatGPT or Claude:

1. Mention that you're using Dash Mantine Components v2
2. Reference the documentation URL: `https://www.dash-mantine-components.com/assets/llms.txt`
3. The AI will fetch and use the documentation to provide accurate answers

#### GitHub Copilot

While Copilot doesn't directly support external documentation, you can:

1. Include relevant documentation snippets in your comments
2. Reference component names and props accurately for better suggestions

### Example Prompts

Here are some example prompts you can use with AI tools:

* "Using Dash Mantine Components v2, how do I create a dark mode toggle?"
* "Show me how to use the AppShell component with a collapsible navbar"
* "How can I customize the theme colors in MantineProvider?"
* "How to align input with a button in a flex container?"

### Documentation Generation

The LLM documentation is automatically generated from our source files.

To ensure you have the latest documentation, we regenerate the llms.txt file with each release. The file follows the [LLMs.txt](https://llmstxt.org/) standard for better compatibility with AI tools.

### Contributing

If you find any issues with the LLM documentation or have suggestions for improvement, please [open an issue](https://github.com/snehilvj/dmc-docs/issues) on our documentation GitHub repository.

