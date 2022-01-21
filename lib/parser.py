from pathlib import Path

NO_PRISM = " # no-prism"
NO_RUN = " # no-run"


# inspired by official dash docs
def load_example(file, run=True):
    path = Path.cwd().joinpath("pages", file)
    example = path.read_text()
    scope = {}
    source = example.replace("component = ", "", 1)
    source = source.replace("@callback", "@app.callback")
    example = example.replace("app.layout = ", "component = ", 1)

    # remove lines from source that should not be displayed in the docs
    if NO_PRISM in source:
        source = "\n".join(
            [line for line in source.splitlines() if NO_PRISM not in line]
        )

    # remove lines from example that should not be executed
    if NO_RUN in example:
        example = "\n".join(
            [line for line in example.splitlines() if NO_RUN not in line]
        )

    # remove tags
    source = source.replace(f" {NO_RUN}", "")

    if run:
        try:
            exec(example, scope)
        except Exception as e:
            print("=============================================")
            print(f"Error running: \n{example}")
            raise e

    return [(scope["component"] if run else None), source]
