import Tkinter as tk
import thread
import commands
from PIL import Image, ImageTk
TITLE_FONT = ("Helvetica", 18, "bold")
# Tkinter initialisation class
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(width=666, height=666)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Login, Logged_In, Not_Logged_In, ALogged_In, Calendar, TroubleShooting, Raw_Data):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location; 
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Login)
    #This is the function that raises the frames so we can change the GUI
    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()
# These are the classes to define the frames
#This frame is the inital login frame
class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        self.controller = controller
        label = tk.Label(self, text="Tap your card to Login", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        x = Misc()
        button1 = tk.Button(self, text="Login", command=lambda: x.log(controller))
        button1.pack(expand=1)   
#This is the frame for a succesful login
class Logged_In(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="You're Logged in!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Check Your Calendar", command=lambda: controller.show_frame(Calendar))
        button1.pack()
#This is the frame for an unsuccesful login (Will probably be depricated by the next version)
class Not_Logged_In(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Authentication Failed", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame(Login))
        button.pack()
class ALogged_In(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="You're Logged in!", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        x = Misc()
        button1 = tk.Button(self, text="Check Your Calendar", command=lambda: controller.show_frame(Calendar))
        button2 = tk.Button(self, text="Acces Raw Student Data", command=lambda: controller.show_frame(Raw_Data))
        button3 = tk.Button(self, text="Trouble Shooting", command=lambda:controller.show_frame(TroubleShooting))
        button4 = tk.Button(self, text="Shutdown")
        button5 = tk.Button(self, text="Exit")
        button5.pack()
        button4.pack()
        button3.pack()
        button2.pack()
        button1.pack()
        
class TroubleShooting(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        image = Image.open("TS.png")
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(Logged_In))
        button.pack()
class Raw_Data(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Raw Data", font=TITLE_FONT)
        label.grid(row=0, column=1)
        data = [["Number of Logins", "4"], ["Users", "Nathan Cohen"]]
        # use black background so it "peeks through" to 
        # form grid lines
        rows  = 2
        columns = 2
        self._widgets = []
        
        for row in range(2):
            current_row = []
            for column in range(2):
                label = tk.Label(self, text="%s" % (data[row][column]), 
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)
        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)
        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(ALogged_In))
        button.grid(row=9, column=0)

    
    
class Calendar(tk.Frame):
    def __init__(self, parent, controller):
        # use black background so it "peeks through" to 
        # form grid lines
        rows  = 8
        columns = 3
        a = Misc()
        data = a.query_ed("Calendar")
        data = eval(data[1])
        tk.Frame.__init__(self, parent)
        self._widgets = []
        for row in range(8):
            current_row = []
            for column in range(3):
                label = tk.Label(self, text="%s" % (data[row][column]), 
                                 borderwidth=0, width=10)
                label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)
        button = tk.Button(self, text="Go Back", command=lambda: controller.show_frame(Logged_In))
        button.grid(row=9, column=0)
class Misc():
    def log(self, a):
        poll = commands.getstatusoutput('python ./Local_Login.py')
        out = poll[1]
        if out == "Hello World":
            a.show_frame(ALogged_In)
        else:
            a.show_frame(Not_Logged_In)
    def rawData(self):
        data = commands.getstatusoutput('python ./Local_Login.py')
        return data
    def query_ed(self, typ):
        edumateReply = commands.getstatusoutput('python ./Edumate.py')
        out = []
        if typ == 'Calendar':
            for i in range(len(edumateReply)):
                #In this case the assumption is made that the reply from edumate will be a 2d array structured as (Teacher, Room, Subject)
                out.append(edumateReply[i])
        return(out)
if __name__ == "__main__":
    app = SampleApp()      
    app.mainloop()