from markdown2dash import SourceCode
from dash.development.base_component import Component
from dash import html

class SC(SourceCode):
    NAME = "source_llms"

    def render(self, renderer, title: str, content: str, **options) -> Component:
        #sample usage

        # sample_option1 = options.pop("sample_option1", "false")
        # sample_option2 = options.pop("sample_option2", "true")
        # files = title.split(", ")
        #
        return html.Div()


"""
This directive shows nothing in the docs, but can be used in the llm/generate_llms_text.py to
add content to llms.txt file.  

sample usage:

.. source_llms::docs/alert/auto.py, assets/styles.css
    :sample_option1: false
    :sample_option2: true

"""
