---
name: LLMs.txt
endpoint: /llms
description: Dash Mantine Components provides LLM-friendly documentation to help AI tools like Cursor, Windsurf, GitHub Copilot, ChatGPT, and Claude understand and work with the DMC library.
dmc: false
---
.. toc::


### Complete Documentation

Full DMC documentation following the [LLMs.txt](https://llmstxt.org/) standard (~1.6MB)

* [View DMC llms.txt online](/assets/llms.txt)
* [View Mantine llms.txt online](https://mantine.dev/llms.txt) (upstream Mantine documentation)


### Customized llms.txt

While the full `llms.txt` file contains everything, customizing it for your project can significantly improve both accuracy and efficiency when working with AI tools.

Benefits of a Customized File:
* Faster and more relevant AI responses— smaller, focused documentation files help tools like ChatGPT or Cursor zero in on exactly the components and props you’re using.
* Reduced context noise — by stripping out unrelated sections, large component sets, or advanced examples you don’t use, AI tools spend their context window entirely on your project-relevant APIs.
* Improved compatibility with code assistants that have input size limits (like GitHub Copilot or Claude).

You’ll find detailed options for generating your own `llms.txt` at the bottom of this page.

### Usage with AI Tools

#### Cursor
1. Type `@Docs` in your prompt
2. Reference the DMC documentation URL: `https://www.dash-mantine-components.com/assets/llms.txt`
3. Ask questions about DMC components, styling, or implementation

Tip: You’ll get even better results if you upload your customized `llms.txt` file directly or reference it locally instead of the full version.

#### Windsurf
1. Reference the documentation using `@https://www.dash-mantine-components.com/assets/llms.txt`
2. Or add your custom file path to your `.windsurfrules` file for persistent access
3. Smaller, project-specific files make Windsurf faster to index and query.

#### ChatGPT & Claude
1. Mention that you're using Dash Mantine Components v2.
2. Reference the documentation URL: `https://www.dash-mantine-components.com/assets/llms.txt`
3. For best results, upload your customized llms.txt (containing only the components used in your app). This improves
the model’s ability to generate correct code using DMC props.

#### GitHub Copilot

While Copilot doesn't directly support external documentation, you can:

1. Include relevant documentation snippets or short versions of `llms.txt` in your project.
2. Reference component names and props accurately in comments for better inline completions.



### Example Prompts

Here are some example prompts you can use with AI tools:

* "Using Dash Mantine Components v2, how do I create a dark mode toggle?"
* "Show me how to use the AppShell component with a collapsible navbar"
* "How can I customize the theme colors in MantineProvider?"
* "How to align input with a button in a flex container?"
* "Refer only to my custom llms.txt file (layout and feedback components) for examples."



### Documentation Generation

The LLM documentation is automatically generated from our source files.  To ensure you have the latest documentation, 
we regenerate the `llms.txt` file with each release.  The file follows the [LLMs.txt](https://llmstxt.org/) standard
for better compatibility with AI tools.

### Creating a Custom llms.txt File

You’ll get the best results by using  only the sections of the documentation that you need. 


#### Option 1 — Download using customization app
Use the interactive tool below to select specific component categories (for example, layout, inputs, feedback) or individual components (like `AppShell`, `Card`, or `Button`), then download your file.

.. exec::docs.llms.llms_download
    :code: false



#### Option 2 — Build your own from llms.json

You can also manually create your own `llms.txt` file using the structured data in  [llms.json](/assets/llms.json).

Each entry in `llms.json` represents one documentation page, including fields like `name`, `description`, `category`,
and full `content`.  You can filter and combine only the components you need — for example, by category or name.

#### Option 3 — Use the “Copy for LLMs” feature

Each documentation page includes a “Copy for LLMs” button that copies that page’s content in LLM-friendly format.
Use this when you want to paste a few pages directly into a chat session (e.g. ChatGPT or Cursor) without downloading the entire documentation.

Use this for quick one-off conversations, when you only need to reference one or two components.

### Contributing

If you find any issues with the LLM documentation or have suggestions for improvement, please [open an issue](https://github.com/snehilvj/dmc-docs/issues) on our documentation GitHub repository.
