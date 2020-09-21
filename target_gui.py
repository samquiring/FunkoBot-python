from tkinter import *
import hot_topic_bot
from tkinter import filedialog
from site_gui import site_gui
from target_bot import target_bot

class target_gui(site_gui):
    
    def __init__(self):
        site_gui.__init__(self,"Target bot","Sam's Automatic Target Item Buyer")
    
    def start(self):
        self.userInfo(self.input_file)
        self.bot = target_bot(self.webpage, self.username, self.password)
        self.bot.get_item()
        self.bot.checkout()
        self.bot.login()
        self.window.mainloop()

tester = target_gui()