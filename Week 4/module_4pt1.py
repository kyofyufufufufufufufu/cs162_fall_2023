"""
Tabitha Geiger
CS 162
Module 04, part 1

-Prototype a GUI with a button, a text box, and a label.
-Show how event listeners work by having a button that
when pressed will copy the text from the text box and place
it on the label.
-Attempt to create a few PyTests that will work with the data behind the scenes
(maybe a test that checks the default value in your text box, label, or that
some variables has an expected value)

"""
import tkinter as tk

class GuiBasics:
    """
    Gui class for basic understanding for main file
    """
    def __init__(self):
        """
        Initializes all of our basic GUI components.

        Defines widgets for GUI window.
        """
        
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("600x600")
        self.root.config(bg="light grey")

        self.label1 = tk.Label(self.root, text="Untitled")
        self.label1.pack()

        self.entry_var = tk.StringVar(self.root, "Enter here...")
        self.entry_line = tk.Entry(self.root,bg="white",textvariable=self.entry_var,width=25)
        self.entry_line.pack()
        
        #creates button with command using button_cpy entry function
        self.button_cpy_entry = tk.Button(self.root, text="Enter", command=self.button_cpy_entry)
        self.button_cpy_entry.pack()

    #gets value of entry and configures into label
    def button_cpy_entry(self):
        self.label1.config(text=self.entry_var.get())
    
    def main_loop(self):
        """
        starts this GUI window
        """
        self.root.mainloop()