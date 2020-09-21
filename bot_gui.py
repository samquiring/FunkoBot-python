from tkinter import *
from tkinter import filedialog
import hot_topic_bot
import hottopic_gui
import funko_gui

website = ''
window = Tk()
window.title("Item Purchase Bot")
mainframe = Frame(window)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
tkvar = StringVar(window)
choices = { 'Hottopic','Target','Funko'}
tkvar.set('Hottopic') # set the default option
popupMenu = OptionMenu(mainframe, tkvar, *choices)

Label(mainframe, text="What website would you like to bot?").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
    website = tkvar.get()

# link function to change dropdown
tkvar.trace('w', change_dropdown)

def changeGui ():
    website = tkvar.get()
    if(website == 'Hottopic'):
        window.destroy()
        hot = hottopic_gui.hottopic_gui()
    elif(website == 'Funko'):
        window.destroy()
        funko = funko_gui.funko_gui()
    else:
        print(website)

run_bot_button = Button(text = "Run", command = changeGui)
run_bot_button.pack()

window.mainloop()