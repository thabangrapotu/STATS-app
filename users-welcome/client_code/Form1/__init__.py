from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.js
import re
from anvil.js import window
from anvil.js.window import alert
# from anvil.js.window import js_eval

# import anvil.html as ahtml

class Form1(Form1Template):
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.call_js('pageScroll')
    
    

    # Any code you write here will run before the form opens.
  
 
  def first_name_pressed_enter(self, **event_args):
    # first_name = self.first_name.text
    # self.first_name.bold = true
    

    
    # self.first_name.type = "number"
    # self.first_name.type = "number"
    pass
    
    # Do something with the entered text
    # return(first_name)
   

  def last_name_pressed_enter(self, **event_args):
   pass

    
  def cell_number_pressed_enter(self, **event_args):
   # cell_number = self.cell_number.text
   # return(cell_number)
    pass

  def Church_Member(self, **event_args):
   # church_member = self.church_member.text
   # return(church_member)
    pass

  def Church_Visitor(self, **event_args):
   # church_visitor = self.church_visitor.text
   # return(church_visitor)
    pass

  def Membership_question_drop_down(self, **event_args):
   # member_status = self.member_status.selected_value
   # return(member_status)
   """"
  def Submit_button_click(sit_number):
   

   first_name = self.first_name_pressed_enter()
   print("First Name entered:", first_name)
   last_name = self.last_name_pressed_enter()
   print("Last Name entered:", last_name)
   id_number = self.id_number_pressed_enter()
   print("ID number entered:", id_number)
   cell_number = self.cell_number_pressed_enter()
   print("Cell number entered:", cell_number)
   church_member = self.Church_Member()
   print("Church member entered:", church_member)
   church_visitor = self.Church_Visitor()
   print("Church visitor entered:", church_visitor)
   member_status = self.drop_down_1_change()
   print("Member state status:", member_status)
 
   # Call the Submitting_Button function
    
   # Call the Sit_Number_Print function
   Sit_Number_Print(sit_number)   
  """"  
  def Submit_button_(self, **events_args):
    
    # Call the google colab function and pass it the iris measurements
    church_ref = anvil.server.call('generate_sit_number', 
                                self.first_name.text,
                                self.last_name.text,
                                self.nearby_area_dropdown.selected_value,
                                self.cell_number.text,
                                self.ext_num.text,
                                self.gender_dropdown.selected_value,                               
                                self.member_status.selected_value
                                )
      # If a category is returned set our species 
    if church_ref:
     # Sit__Number_Print(self.sit_number)
     print('Successfully submitted. Please confirm your submitted details below while we process your Reference number', str(church_ref))
     if "null" not in church_ref: 
      message_to_print =  f"Thank you for holding {self.first_name.text.capitalize()} {self.last_name.text.capitalize()}, your reference number:  {church_ref}"
     else:
      message_to_print =  f"Thank you for holding {self.first_name.text.capitalize()} {self.last_name.text.capitalize()}, unfortunately reference number are only allocated to new church members"
     self.church_ref.visible = True
     self.church_ref.text = message_to_print
     alert(message_to_print) 
     self.clear_fields()
      
  # def close_page(self):   
  #    js.call("window.close()")
  
  def clear_fields(self):
     self.first_name.text = ''
     self.last_name.text = ''
     self.nearby_area_dropdown.selected_value = 'Windmill Park'
     self.cell_number.text = ''
     self.ext_num.text = ''
     self.gender_dropdown.selected_value= 'Male'
     self.member_status.selected_value = 'Yes'
     self.church_ref.text = ''
     # close_page()
    
  # @anvil.server.callable

    
    
  # def Sit__Number_Print(self, **event_args):
  #  print('Successfully submitted. Please confirm your submitted details below while we process your sit number')
  #  message_to_print =  "Thank you for holding, your sit number:\n"+self.sit_number.text
  #  self.sit__number.visible = True
  #  self.sit__number = message_to_print

  def Membership_question_drop_down_(self, **event_args):
   pass


  def first_name_focus(self, **event_args):
    self.first_name.type ='text'

  # def id_number_lost_focus(self, **event_args):
    # input_text_value = self.id_number.text
    # err_message = ''
    # n = input("Enter")
    # if not re.match("^[a-zA-Z]+$", input_text_value):
     # print(input_text_value)
     # err_message =  "Only alphabets are allowed"
    # err_message = '<div style="display:flex; align-items: center;"><i class="fa fa-exclamation-circle" style="color: red; margin-right: 5px;"></i>Error occurred!</div>'
     # self.id_number.validation_error = err_message
     # self.id_number.show_error = True
     # self.id_number.role = 'input-error'
     # alert(err_message)

     
     # self.id_number.text = ''
    
     
     # self.id_number = user_var
     
     
     # self.id_number_pressed_enter()
     
     # self.id_number.select_range(0, len(self.id_number.text))
     # self.call_js("document.getElementById('{id_number}').focus();".format(self.id_number))

     
      
    # else:
     # self.id_number.validation_error = None
     # self.id_number.show_error = True
     # self.id_number.role = 'outlined'
     # err_message = 'none'
     # print(err_message)
      
      # event_args.preventDefault()
  
      # regex = re.compile("^[a-zA-Z]+$")
      # key = chr(event_args['which'])
      # if not regex.match(key):
      #   event_args.preventDefault()
      #   return False
      
    # Valid input: continue with the desired logic
    # ...

  def ext_num_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def nearby_area_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_2_click(self, **event_args):
    js.window.open("https://gwra-church-member-sunday-stats-0q123rtxzdfr01.anvil.app")
    # window.close()
    # js.window.close("https://gwra-church-member-sunday-stats-0q123rtxzdfr01.anvil.app")
    # app_url = anvil.server.get_app_origin("https://gwra-church-member-sunday-stats-0q123rtxzdfr01.anvil.app")
    # js.call_js(f'window.location.href = "{app_url}"')

  def visitor_button_click(self, **event_args):
    js.window.open("https://gwra-church-visitors-sunday-stats-0q123rtxzdfr01.anvil.app")







   









