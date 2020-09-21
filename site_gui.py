from tkinter import *
from tkinter import filedialog

class site_gui():
    def __init__(self, bot_name, bot_title):
        self.window = Tk()
        self.window.title(bot_name)
        self.title = Label(text = bot_title)
        self.title.pack()
        self.label_output = Label(text = "input file path to your user_information file")
        input = Button(text = "browse files", command = self.browseFiles)
        run_button = Button(text = "Run", command = self.start)
        self.label_output.pack()
        input.pack()
        run_button.pack()
        self.window.mainloop()

    def start(self):
        pass
    
    def userInfo(self,file):
        f = open(file, 'r')
        counter = 0
        lines = f.readlines()
        for line in lines:
            r = line.split('=')
            print(r[1].strip())
            if(counter == 0):
                self.username = r[1].strip()
            elif(counter == 1):
                self.password = r[1].strip()
            elif(counter == 2):
                self.webpage = r[1].strip()
            elif(counter == 3):
                self.name = r[1].strip()
            elif(counter == 4):
                self.credit_card = r[1].strip()
            elif(counter == 5):
                self.expr = r[1].strip()
            elif(counter == 6):
                self.sec_code = r[1].strip()
            counter += 1

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = [("Text Files", '*.txt')])  
        self.label_output.configure(text="File Opened: "+filename)    
    # Change label contents 
        self.input_file = str(filename) 
