# import things
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
items = [Item('Name1', 'Description1'),
         Item('Name2', 'Description2'),
         Item('Name3', 'Description3')]
# Or, equivalently, some dicts
items = [dict(name='Licencia', description='Tipo de licencia BSD python'),
         dict(name='Monetizacion', description='Es financiacion publica'),
         dict(name='Codigo fuente', description='Disponible en https://github.com/1Lopez/examrem')]

# Or, more likely, load items from your database with something like
items = ItemModel.query.all()

# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template

