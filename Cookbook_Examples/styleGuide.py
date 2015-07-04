"""
Indentation - spaces preferred over tabs
    Python 2 - interpreter -t & -tt options
Line Length - 79 char, text blocks, doc strings - 72 char
Continuation - implied line continuation inside parentheses, brackets and braces.
    Long lines can be broken over multiple lines by wrapping expressions in parentheses.
    These should be used in preference to using a backslash for line continuation.
    The preferred place to break around a binary operator is after the operator.

Blank Lines
    Separate top-level function and class definitions with two blank lines.
    Method definitions inside a class are separated by a single blank line.

Imports:
    Imports one module per line.
    Group as below; put a blank line between each group of imports.

    1. standard library imports
    2. related third party imports
    3. local application/library specific imports

Class Names:  CapWords convention
Function Names: lowercase with underscores as necessary for readability??
    camelCase allowed in context of prevailing style.

Arguments:
   Functions in Classes:
        Always use 'cls' for the first argument to class methods.
        Always use self for the first argument to instance methods.

   To better support introspection, modules should explicitly declare the
    names in their public API using the __all__ attribute.
    Setting __all__ to an empty list indicates that the module has no public API.

Docstrings:
    Use r + 3x"    if you use any backslashes in your docstrings.
"""
