from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
from anvil.js.window import jQuery
from anvil.js import get_dom_node


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # iframe = jQuery("<iframe width='1200px' height='400px'>").attr("src","_/theme/new_file.html")
        
    # # # # Append the iframe to a container in our form
    # iframe.appendTo(get_dom_node(self.content_panel))
    # self.content_panel.add_component()

    # Any code you write here will run before the form opens.
