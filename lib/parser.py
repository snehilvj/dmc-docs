import dash_mantine_components as dmc

NO_DISPLAY = " # no-prism"
NO_EXEC = " # no-exec"


# inspired by official dash docs
def load_example(file, app, run):
    scope = {"app": app}
    with open(file, "r") as f:
        example = f.read()
        source = example.replace("component = ", "", 1)
        example = example.replace("app.layout = ", "component = ", 1)

        # remove lines from source that should not be displayed in the docs
        if NO_DISPLAY in source:
            source = "\n".join(
                [line for line in source.splitlines() if NO_DISPLAY not in line]
            )

        # remove lines from example that should not be executed
        if NO_EXEC in example:
            example = "\n".join(
                [line for line in example.splitlines() if NO_EXEC not in line]
            )

        # remove tags
        source = source.replace(f" {NO_EXEC}", "")

        if run:
            try:
                exec(example, scope)
            except Exception as e:
                print("=============================================")
                print(f"Error running: \n{example}")
                raise e

        return [(scope["component"] if run else None), source]


def get_component_reference(component_name):
    component = getattr(dmc, component_name)
    component_doc = component.__doc__
    docs = component_doc.split("Keyword arguments:")[-1]
    return docs.lstrip("\n\n")
