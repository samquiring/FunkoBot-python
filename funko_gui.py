from tkinter import *
from tkinter import filedialog
import funkobot

class funko_gui():
    def __init__(self):
        self.window = Tk()
        self.window.title("Hottopic bot")
        self.title = Label(text = "Sam's Automatic Hottopic Item Buyer")
        self.title.pack()
        self.label_output = Label(text = "input file path to your user_information file")
        input = Button(text = "browse files", command = self.browseFiles)
        run_button = Button(text = "Run", command = self.start)
        self.label_output.pack()
        input.pack()
        run_button.pack()
        self.window.mainloop()