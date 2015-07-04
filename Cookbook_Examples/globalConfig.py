"""
The canonical way to share information across modules within a single program is to create a special
configuration module (often called config or cfg). Just import the configuration module in all modules
of your application; the module then becomes available as a global name. Because there is only one
instance of each module, any changes made to the module object get reflected everywhere.
"""
xglobal = 'init - ' + __name__

# block
