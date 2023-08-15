from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.js

from anvil.js import window
import anvil.media
import time

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil.js.window import document as _document
from anvil.js.window import jQuery
from alert2.alert2 import alert2 
from ..text2speech import text2speech
from ..Form3 import Form3
from .Form2 import Form2
from ..Form3_copy import Form3_copy
from anvil.js import get_dom_node

from datetime import datetime




class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text2speech = text2speech()
    self.form3 = Form3()
    self.form2 = Form2()
    self.form3_c = Form3_copy()
    self.cont_status = True
    


  def first_name_pressed_enter(self, **event_args):      
    
    pass
  


  def cell_number_pressed_enter(self, **event_args):\
    self.cell_number.type='number'


  def Church_Member(self, **event_args):
    pass

  def Church_Visitor(self, **event_args):
    pass


  
  def Submit_button_(self, **events_args):
    continue_execution = True;
    if not self.member_status.selected_value == 'Yes' and not self.member_status.selected_value == 'Not Yet':  
      self.member_status.role = 'outlined-error'
      alert2() #This alert2() is just added to fix bug in last drop down change or where a alert fails to popup
      self.show_alert_message('Would You like To Be A Member Error: ','Member option must be selected','61vh')
      continue_execution = False
      
    else:
      self.member_status.role="outlined"
    if self.first_name.role == 'outlined-error' or self.last_name.role == 'outlined-error' or self.nearby_area_dropdown.role == 'outlined-error' or self.cell_number.role == 'outlined-error' or self.ext_num.role == 'outlined-error' or self.member_status.role == 'outlined-error':
      continue_execution = False
      self.show_alert_message('Fail To Proceed Error','Please fill in all the mandatory fields first to continue.', '70vh')
      
    if continue_execution == True:
      self.ext_num.text = str(self.ext_num.text).replace('-','')
      self.cell_number.text = str(self.cell_number.text).replace('-','')
      
      self.church_ref = ''
      c = Notification('Please wait while we process your church ID number', title='Church ID number processing...',timeout='10')
      with c:
        try:    
          self.church_ref = anvil.server.call('generate_church_ref_number',
                                self.first_name.text.capitalize(),
                                self.last_name.text.capitalize(),
                                self.nearby_area_dropdown.selected_value,
                                '+27'+self.cell_number.text,
                                self.ext_num.text,
                                self.gender_dropdown.selected_value,
                                self.member_status.selected_value
                                ) 
        except anvil.server.RuntimeUnavailableError:
           # Handle the error here, for example, by logging it
           c.hide()
           response = alert("Server resources not available. Please contact support if the issue persists. or Click the Exit button to close the page", title="Server Unreachable", dismissible=False, role='unsuccess-alert',  buttons=[("OK", None),("Exit",True)])
           if response:
             self.clear_fields()
             return()
      if self.church_ref:     
          if "null" not in self.church_ref and "limit reached" not in self.church_ref and "user exist" not in self.church_ref:
            self.new_user_Id_message()
            self.clear_fields()            
            return()
          else:
            if "null" in self.church_ref:
              self.not_yet_user_message() 
              self.clear_fields()        
              return()
            if "limit reached" in self.church_ref:
              self.response = alert('Your daily cap has been reached. You can only move forward if you want to click the Change Status option to alter your membership status. Click the Exit button to leave.',title="Daily Limit Reached",dismissible=False, buttons=[("Change Status", True),("Exit",False)], role = 'warning-alert')
              if self.response:
                self.message_limit('change status')
              else:
                self.message_limit('exit')

              self.clear_fields()
              return()

            if "user exist" in self.church_ref:
              alert('The user already exist. Please contact the admin here 0## $$$ %%%% to reset or recover your church ID number. Click the Exit button to leave.',title="Daily Limit Reached",dismissible=False, buttons=[("Exit",None)], role = 'warning-alert')
              self.clear_fields()
              return
              


  def message_limit(self, button_clicked):   
      self.member_status.selected_value = 'Yes'
      self.Submit_button_()
    
    
      
    
  def new_user_Id_message(self):
    message_to_print =  f"Thank you for holding {self.first_name.text.capitalize()} {self.last_name.text.capitalize()}, your church ID number is <u>{self.church_ref}</u>.<br><br>Please make note of your church ID number, as it will be required next time you use the system"
    alert2(header= 'ID Processed Successfully',footer_buttons_align='right' , content= message_to_print,close_button_color= 'green',foreground='green', footer_color='#E6E6FA',header_color='#E6E6FA',background='#F0F0F0',padding_top='30vh')
     
  def not_yet_user_message(self):
    message_to_print =  f"Thank you for holding {self.first_name.text.capitalize()} {self.last_name.text.capitalize()}, unfortunately church ID number are only allocated to new church members.<br><br>To be a church member, click the Yes button or click the Not Yet button to exit"
    b=Button(text='Yes', role='elevated-button')
    b.set_event_handler('click',self.change_member_function)
    alert2(width='0', dismissable= True, block_script=False).close()
    a = alert2(dismissable=False,footer_buttons_align='center',footer_buttons= [b, Button(text='Not Yet', role='elevated-button')],header= 'ID Processed Unsuccessfully', content= message_to_print, footer_color='#E6E6FA',header_color='#E6E6FA',background='#F0F0F0',foreground='red',padding_top='30vh')
     
  
  def clear_fields(self):
    self.column_panel_2.clear()

    self.temp_label_outline = Label(text='Disclaimer: Please note that the information captured on the next page will be used or processed solely for church purposes and in accordance with the POPI Act. You are entitled to request the retention or destruction of your personal information from the system. For any inquiries, please contact the admin at 0## $$$ ##$$.', spacing_above='large',spacing_below='none', align='Center', font_size='14', foreground='red' , bold='True', underline='True', visible='True')
    self.outlined_card_2.clear()
    self.outlined_card_2.add_component(self.temp_label_outline)
    if self.member_change_status == False:
      self.gender_called = 'Mr.'
      if self.gender_dropdown.selected_value == 'Female':
        self.gender_called = 'Miss or Mrs.'

      self.title_content_write ='Good Bye '+ self.gender_called.replace(' or ','/')+' '+self.first_name.text[0:1].capitalize()+' '+self.last_name.text[0:1].capitalize()+','
      self.title_content_speech ='Good Bye '+ self.gender_called+' '+self.first_name.text[0:1].capitalize()+' '+self.last_name.text[0:1].capitalize()+','
      speak_time =  len(self.last_name.text+self.first_name.text) + 4000
      self.a = 'You are now done. Have a blessed day!'
      self.n = Notification(self.a,title=self.title_content_write, timeout=speak_time, style='info') 
      self.n.show()
      self.outlined_card_1.clear()
      iframe = jQuery("<iframe width='1500px' height='300px'>").attr("src","_/theme/new_file.html")
        
    # # # # Append the iframe to a container in our form
      iframe.appendTo(get_dom_node(self.outlined_card_1))
      self.speech_message = self.title_content_speech+', You are now done. Have a blessed day.  Next person please. Good day: please wait for the next page to proceed. It will only take 1 to 3 minutes of your time to complete the registration.'
      
      self.read_message()
      Notification('Please wait for the next ''welcome'' page to proceed. It will only take 1 to 3 minutes of your time to complete the registration. ', title='Good day,', timeout= 90).show()
      time.sleep(7)
      window.setTimeout(window.close, speak_time+3500);

      

  def read_message(self, **event_args):
     self.text2speech.start(self.speech_message)
     time.sleep(6)
     self.n.__exit__()
     

  def clear_text_field_content(self):
 
    time.sleep(1)

  member_change_status = False
  def change_member_function(self, **event_args):
    self.member_status.selected_value = 'Yes'
    self.Submit_button_()
    self.member_change_status = True
    

  def Membership_question_drop_down_(self, **event_args):
    pass


  def first_name_focus(self, **event_args):
    self.first_name.type ='text'

  def add_bye_content(self):
    time.sleep(3)
    self.outlined_card_1.clear()
    

  def ext_num_pressed_enter(self, **event_args):
    pass
    
  dropdown_show_status = False
  dropdown_change_status =False
  def nearby_area_dropdown_change(self, **event_args):
    self.dropdown_change_status = True
    self.nearby_area_dropdown.role="outlined"

  def nearby_area_dropdown_hide(self, **event_args):    
    pass
    
  def nearby_area_dropdown_show(self, **event_args):
    
    self.dropdown_show_status = True

  
  def outlined_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def first_name_lost_focus(self, **event_args):
    if not self.first_name.text.isalpha(): 
      
      self.first_name.role = 'outlined-error'
      self.show_alert_message('First Name Error Message: ','Name must only contain alphabets','34vh')
    
    else:
      self.first_name.role="outlined"
  
 
  def last_name_lost_focus(self, **event_args):
    if not self.last_name.text.isalpha(): 
      
      self.last_name.role = 'outlined-error'
      self.show_alert_message('Last Name Error Message: ','Last name must only contain alphabets','34vh')
    
    else:
      self.last_name.role="outlined"

  
  def cell_number_lost_focus(self, **event_args):
    self.arear_error()
    self.cell_number_change()
    numeric_text = ''.join(filter(str.isdigit, str(self.cell_number.text))) 


    errStatus = False
    p = numeric_text
    if not p.isalnum() or 'None' in p:
      
      self.cell_number.role =  'outlined-error'
      self.show_alert_message('Contact Number Error1: ','Contact number must only contain numbers','43vh')
    
    else:
      if not errStatus:
        self.cell_number.role="outlined" 

    if not p[0] == '0': 
      
      self.cell_number.role =  'outlined-error'
      self.show_alert_message('Contact Number Error2: ','Contact number must start with zero "0"','43vh')
    
    else:
      if not errStatus:
        self.cell_number.role="outlined"
      
    if not len(p) == 10: 
      
      self.cell_number.role =  'outlined-error'
      self.show_alert_message('Contact Number Error3: ','Contact number length must be 10','43vh')
    
    else:
      if not errStatus:
        self.cell_number.role="outlined"
    try:
         
      if p[1] not in {'6', '7', '8'}:
             
        self.cell_number.role =  'outlined-error'
        self.show_alert_message('Contact Number Error4: ','Contact number digit after 0 must be 6, 7 or 8 ','43vh')
    
      else:
        if not errStatus:
          self.cell_number.role="outlined"
    except IndexError:
      self.cell_number.text='--'
      
      
 
    
  
  def ext_num_lost_focus(self, **event_args):
    if len(str(self.ext_num.text)) == 13:
      birth_date_id = str(self.ext_num.text)[:6]
      birth_date_obj = datetime.strptime(birth_date_id, '%y%m%d')
      self.date_of_birth.date = birth_date_obj.strftime('%d %B %Y')

    self.arear_error()

    self.ext_num_change()
    
    numeric_text = ''.join(filter(str.isdigit, str(self.ext_num.text))).replace('-','')
    errStatus = False
    p = str(numeric_text)  
    if not p.isalnum() or 'None' in p:
      
      self.ext_num.role =  'outlined-error'
      self.show_alert_message('ID / Passport number Error1: ','ID / Passport number must only contain numbers','50vh')
    
    else:
      if not errStatus:
        self.ext_num.role="outlined" 

    if not len(p) == 13: 
      
      self.ext_num.role =  'outlined-error'
      self.show_alert_message('ID / Passport number Error2: ','ID 0r Passport must contain 13 numbers','50vh')
    
    else:
      if not errStatus:
        self.ext_num.role="outlined"
    if self.ext_num.role == 'outlined':
      ext_num_text_str = str(self.ext_num.text)
      gender_str = ext_num_text_str[6:11]      
      gender_num = int((gender_str).replace('-',''))
      if gender_num >= 0 and gender_num <= 4999:
        self.gender_dropdown.selected_value = 'Female'
      else:
        self.gender_dropdown.selected_value = 'Male'
    
  def gender_dropdown_hide(self, **event_args):
    pass

  def member_status_hide(self, **event_args):
    """This method is called when the DropDown is removed from the screen"""
    pass


  def last_name_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


  def member_status_change(self, **event_args):
    self.arear_error()


  def show_alert_message(self, field, messg, pad_value):
    alert2(header=field, close_button_color= 'red',foreground='red', content=messg, width=60,drag=False, block_script=True, role='outlined-error', padding_top=pad_value, footer_color='#E6E6FA',header_color='#E6E6FA',background='#F0F0F0')

  def arear_error(self, **event_args):
    if self.dropdown_change_status == False:
      self.nearby_area_dropdown.role = 'outlined-error'
      if self.member_status.selected_value == 'YES' or self.member_status.selected_value == 'NO': 
        alert2() #This alert2() is just added to fix bug in last drop down change or where a alert fails to popup
      self.show_alert_message('Area Name Error1: ','Area name must not be empty','43vh')
      
    else:
      
      self.nearby_area_dropdown.role="outlined"

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    pass

  def cell_number_change(self, **event_args):
    input_text = self.cell_number.text
    # Remove all non-numeric characters
    numeric_text = ''.join(filter(str.isdigit, str(input_text)))

    # Format the numeric_text as "+27 XX XXX"   
    formatted_text = f"{numeric_text[:2]}-{numeric_text[2:5]}-{numeric_text[5:10]}"  
        # Set the formatted text back to the text box
    self.cell_number.type = 'tel'
    if not formatted_text[0] == '0':
      self.cell_number.text = '0'+formatted_text

  def cell_number_focus(self, **event_args):
    tmp_cell_num = str(self.cell_number.text).replace('-','')
    self.cell_number.type = 'number'
    self.cell_number.text=tmp_cell_num

  def ext_num_focus(self, **event_args):
    tmp_id_num = str(self.ext_num.text).replace('-','')
    self.ext_num.type = 'number'
    self.ext_num.text=tmp_id_num

  def ext_num_change(self):
    input_text = str(self.ext_num.text)
    numeric_text = ''.join(filter(str.isdigit, str(input_text)))

    # Format the numeric_text as "+27 XX XXX"
    formatted_text = f"{numeric_text[:6]}-{numeric_text[6:10]}-{numeric_text[10:13]}"
        # Set the formatted text back to the text box
    self.ext_num.type = 'text'
    # if not formatted_text[0] == '0':
    self.ext_num.text = formatted_text

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass







   

  
      
    



   





  






