from tkinter import *
import hot_topic_bot
from tkinter import filedialog
from site_gui import site_gui
from funkobot import funkobot

class funko_gui(site_gui):
    
    def __init__(self):
        site_gui.__init__(self,"Funko bot","Sam's Automatic Funko Item Buyer")
    
    def start(self):
        self.userInfo(self.input_file)
        self.bot = funkobot(self.webpage, self.username, self.password)
        self.bot.login()
        self.bot.get_funko()
        self.bot.checkout_quick()
        self.window.mainloop()