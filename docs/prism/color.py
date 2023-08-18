import dash_mantine_components as dmc

component = dmc.Prism(
    """@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1 + 0b10l) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''""",
    language="python",
    colorScheme="dark",
)
