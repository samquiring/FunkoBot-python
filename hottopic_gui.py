from tkinter import *
import hot_topic_bot
from tkinter import filedialog
from site_gui import site_gui

class hottopic_gui(site_gui):
    
    def __init__(self):
        site_gui.__init__(self,"Hottopic bot","Sam's Automatic Hottopic Item Buyer")
    
    def start(self):
        self.userInfo(self.input_file)
        self.bot = hot_topic_bot.hot_topic_bot(self.username,self.password,self.webpage,self.name,self.credit_card,self.expr,self.sec_code)
        self.bot.popup_closer()
        self.bot.user_login()
        self.bot.goto_page()
        self.bot.check_availablity()
        self.bot.bag()
        self.bot.checkout()
        self.bot.billing()
        self.window.mainloop()
