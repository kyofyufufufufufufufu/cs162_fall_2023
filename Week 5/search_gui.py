"""
Tabitha Geiger
10/31/2023

Create GUI for searching values.
"""



import tkinter as tk
import random
from tkinter import messagebox

# Function to perform the search
def search():
    target = int(entry.get())
    for i, value in enumerate(data):
        #config canvas and highlight rectangles and update canvas
        canvas.itemconfig(rectangles[i], fill="white")
        canvas.update()  
        
        if value == target:
            canvas.itemconfig(rectangles[i], fill="green")  # Found the value
            status_label.config(text=f"Value {target} found at index {i}")
            return
        elif target < 1 or target > 100:
            messagebox.showinfo(title="ERROR",message=(f"'{target}' not found."))
            return
        else:
            canvas.itemconfig(rectangles[i], fill="hot pink")  #not a match
        
        canvas.after(100)  #use for 100ms
    messagebox.showinfo(title="ERROR",message=(f"'{target}' not found."))

############################################################################
# Create GUI
############################################################################

root = tk.Tk()
root.title("Search Linear Algorithm")
root.geometry("600x400")

#create a canvas to display the data
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

#setting a list of random numbers between 1-100
data = []
for i in range(100):
    data.append(random.randint(1,100))    
    
#dawring rectangules
rectangles = []
for index, value in enumerate(data):
    x1, y1 = index * 4, 300
    x2, y2 = (index + 1) * 4, 300 - value * 2
    rect = canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    rectangles.append(rect)

#create a label and an entry for the search value
search_label = tk.Label(root, text="Enter a value to search for: ")
search_label.pack()

entry = tk.Entry(root)
entry.pack()

#create the search button
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

#create a label to display the search status
status_label = tk.Label(root, text="")
status_label.pack()

#start the tkinter main loop
root.mainloop()
