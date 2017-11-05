
#Created by: Nicholas Brean


import ui 

def procudure(tc):
    #converts. elsius to farenheit
    tf = 1.8*tc+32
	
    #output
    #showing the answer printed as a string
    view['answer_label'].text = 'the fareheit is: ' + str(tf)
   
def calculate_celsius_to_farenhiet(sender):
    #input
    #getting user input
    tc = int(view['farenhit_textfield'].text)
    procudure(tc)
view = ui.load_view()
view.present('sheet')
