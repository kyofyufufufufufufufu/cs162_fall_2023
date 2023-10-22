"""
    Create another program (yes you can start with your old code!) to now 
    include 9 more text boxes (all 10 held within some kind of collection, 
    such as a list) and change the listener to find the smallest number 
    from the self.entry_list and display it in the label

    Now that that is working, let’s change the button one more time;
    have the button, when clicked, change the label's text to match that
    of the next smaller number in the list of self.entry_list.
    
    (so if you had the numbers 1, 5, 3, 7, 8, 3, 6, 9, 0, 12 
    in the text boxes, then the first click would display a 0, 
    the second click would display a 1, the next a 3, the next a 3 
    (since there is another 3 in the list), and so on)

    Attempt to create a few PyTests similar to before.
"""

import tkinter as tk
from itertools import cycle

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
        self.root.title("Find Smallest Number")
        self.root.geometry("600x600")
        self.root.config(bg="light grey")

        self.label1 = tk.Label(self.root, text="Untitled")
        self.label1.pack()
        #empty list to append entries
        self.entry_list = []

        for self.entry_line in range(10):
            self.entry_line = tk.Entry(self.root)
            self.entry_list.append(self.entry_line)
            self.entry_line.pack()

        #buttons with commands using defined functions: find_smallest and next_smallest
        self.find_small_button = tk.Button(self.root, text="Find Smallest", command=self.find_smallest)
        self.find_small_button.pack(pady=3)
        self.next_smallest = tk.Button(self.root, text="Next Smallest", command=self.next_smallest)
        self.next_smallest.pack(pady=3)

    #find smallest value in list of entries and removes that value after configuration
    def find_smallest(self):
        self.values = [int(self.entry_list[i].get()) for i in range(10)]
        smallest_num= min(self.values)
        self.label1.config(text=str(smallest_num))
        self.values.remove(smallest_num)

    #finds next smallest value in list and removes that value after configuration
    def next_smallest(self):
        if self.entry_list:
            next_smallest = min(self.entry_list, key=lambda x: int(x.get()))
            self.label1.config(text=next_smallest.get())
            self.entry_list.remove(next_smallest)
        else:
            self.label1.config(text="Finished.")


    def main_loop(self):
        """
        starts this GUI window
        """
        self.root.mainloop() 