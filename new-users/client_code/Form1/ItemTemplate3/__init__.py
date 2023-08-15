from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_hide(self, **event_args):
    """This method is called when the column panel is removed from the screen"""
    pass

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pass



