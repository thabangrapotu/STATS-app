from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
from anvil.js.window import jQuery
from anvil.js import get_dom_node


class Form2(Form2Template):
  def __init__(self, **properties):
  
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.html_component = HtmlTemplate()
    # self.html_component.foreground = 'black'
    # self.html_component.visible = True
    # self.html_component.background = 'indigo'
    # self.html_component.border ='black'
    # self.add_component(self.html_component
    
    iframe = jQuery("<iframe width='1500px' height='400px'>").attr("src","_/theme/new_file.html")
        
    # # # # Append the iframe to a container in our form
    iframe.appendTo(get_dom_node(self.column_panel_1))
  
    
    

    # Any code you write here will run before the form opens.

  # def youtube_video_1_show(self, **event_args):
  #   """This method is called when this video is shown on the screen (or it is added to a visible form)"""
  #   pass



     
