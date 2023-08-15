from ._anvil_designer import text2speechTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
class text2speech(text2speechTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.speech = anvil.js.window.SpeechSynthesisUtterance()
    self.speechsynthesis= anvil.js.window.speechSynthesis
    #Set the Defaults
    self.speech.lang = "en"
    self.speech.rate = 1
    self.speech.pitch=1
    self.speech.volume=1
    self.speech.text='test'
    self.voice_selected = ''
    self.visible=False
    # self.speech=self.endevent
    self.speechsynthesis.onvoiceschanged=self.populatevoices
    self.init_components()

  def populatevoices(self,e):
        self.list_of_voices=self.speechsynthesis.getVoices()
        self.list_of_voices_name=[i.name for i in self.list_of_voices]
        # print(self.list_of_voices_name)
  
  @property
  def text(self):
    return self.speech.text

  @text.setter
  def text(self, value):
    self.speech.text=value
    
  @property
  def language(self):
    return self.speech.lang

  @language.setter
  def language(self,language):
    self.speech.lang=str(language)



  def start(self, message):
    '''Set the voice for speech. You can pass either the Name of the voice or the Voice object itself'''
    if type(self.voice_selected)!=str:
      self.speech.voice=self.voice_selected
    else:
      if self.voice_selected in self.list_of_voices_name:
        index=self.list_of_voices_name.index(self.voice_selected)
        self.speech.voice=self.list_of_voices[index]
    self.speech.text = message
    # pass
    # self.text(self.speech.text)
    # '''Set the voice for speech. You can pass either the Name of the voice or the Voice object itself'''
    # if type(self.voice_selected)!=str:
    #   self.speech.voice=self.voice_selected
    
    
    '''Start speaking the text'''
    self.speechsynthesis.speak(self.speech)