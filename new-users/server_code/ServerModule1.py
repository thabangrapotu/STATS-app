import anvil.server
from alert2.alert2 import alert2 

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
# def www():
#   js.call_js('replaceH_2_WithNewLine')
def window_alerty():
  if alert2('Something',Button=['Church Member'])=='Church Member':
    # from anvil.js import window
    window.open("https://gwra-church-visitors-sunday-stats-0q123rtxzdfr01.anvil.app",'_blank')
# 'Church Member'
def handle_keypress_on_server():
  # Call the client-side JavaScript function using anvil.js
  anvil.js.call_js('element', 'some_event_data')
  anvil.js.call_js('handleKeyPress', 'some_event_data')


def handle_keypress_on_server2():
  # Call the client-side JavaScript function using anvil.js
  anvil.js.call_js('handleKeyPress2', 'some_event_data2')


def close_window_on_server():
  # Call the client-side JavaScript function using anvil.js
  anvil.js.call_js('closeWindow', 'some_event_data3')





  