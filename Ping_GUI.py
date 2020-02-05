# A GUI using tkinter to create a text box.  User can type an IP address and a
#response based on its availibility will be printed back to the screen

from tkinter import *
import os


class Application(Frame):
    """ A GUI application with three buttons. """

    def __init__(self, master):
        """ Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create button, text, and entry widgets"""
        self.instruction= Label(self, text = "Enter the IP Address: ")
        self.instruction.grid(row = 0, column = 0, columnspan = 1, sticky = W)

        self.IP = Entry(self)
        self.IP.grid(row =0, column = 1, sticky = W)

        self.submit_button = Button(self, text ="submit", command = self.reveal)
        self.submit_button.grid(row=2, column = 0, sticky =W)

        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row =3, column= 0, columnspan = 2, sticky = W)
       
    def reveal(self):
        """Display message based on the password typed in"""
        hostname = self.IP.get()
    
        response = os.system("ping -n 1 " + hostname)

          #and then check the response...
        if response == 0:
            message= hostname, " is up!"
            self.text.delete(0.0, END)
            self.text.insert(0.0, message)
        else:
            message= hostname + " is down!"
            self.text.delete(0.0, END)
            self.text.insert(0.0, message)

root=Tk()
root.title("Ping Test")
root.geometry("350x250")
app = Application(root)

root.mainloop()

