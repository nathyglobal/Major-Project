import Tkinter
import commands

poll = commands.getstatusoutput('python ./Hello_World.py')
out = poll[1]
print poll



class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.minsize(width=666, height=666)
        self.initialize()

    def initialize(self):
        self.grid()
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=0,columnspan=1,sticky='EW')
        self.labelVariable.set(out)
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
    
    
    
    