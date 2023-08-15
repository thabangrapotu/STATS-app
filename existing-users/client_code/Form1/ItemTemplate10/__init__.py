from ._anvil_designer import ItemTemplate10Template
from anvil import *
import anvil.server

class ItemTemplate10(ItemTemplate10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
