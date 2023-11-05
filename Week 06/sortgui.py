import tkinter as tk
import random
import time
from tkinter import messagebox

matched_value_highlight = "green"
unmatched_value = "hot pink"
unchecked_value = "purple"

class SortGui:
    def __init__(self):
        ############################################################################
        # Create GUI
        ############################################################################
        self.root = tk.Tk()
        self.root.title("Sorting Algorithm")
        self.root.geometry("600x400")

        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        #empty list to store rectangles coords
        self.rectangles = []

        #a collection of 10 random int values and rectangles
        self.data = [random.randint(1, 100) for i in range(10)]

        #enumerate through random data from list 'self.data' and creating rectangles
        #based on x and y coords
        for index, value in enumerate(self.data):
            x1, y1 = index * 30, 300
            x2, y2 = (index + 1) * 30, 300 - value * 3
            #creating rectangles on canvas
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=unchecked_value)
            #append to empty rectangle list
            self.rectangles.append(rect)

        self.sort_button = tk.Button(self.root, text="Start Sort", command=self.sort)
        self.sort_button.pack()
        

    def sort(self):
        """Sorting through the total length of our randomized set of 10 ints
        and creating a nested for loop that will then move the smallest index
        to the next space over and, if necessary, make that value the smallest
        value in the list and change its position."""
        #nested for loop and highlights current rectangle depending on whether its
        #smaller number or not
        for i in range(len(self.data)):
            initial_smallest_index = i
            self.highlight_value(initial_smallest_index, matched_value_highlight)
            self.root.after(100,self.root.update())

            #moves to next index
            for j in range(i + 1, len(self.data)):
                self.highlight_value(j, unmatched_value)
                #if current index is smaller than the inital smallest value, it will be updated
                if self.data[j] < self.data[initial_smallest_index]:
                    initial_smallest_index = j

                self.highlight_value(j, unchecked_value)
                self.root.after(100,self.root.update())

            #swapping
            self.data[i], self.data[initial_smallest_index] = self.data[initial_smallest_index], self.data[i]
           
            self.update_rectangles()
            self.canvas.after(0) 
            self.highlight_value(i, matched_value_highlight)
            #pause
            self.root.after(100,self.root.update())

        for rect in self.rectangles:
            self.canvas.itemconfig(rect, fill=matched_value_highlight)
        self.root.update()
        self.show_message("Sorting Completed")

    def highlight_value(self, index, color):
        """Takes in parameters for index and the color based on whether it's an unmatched or matched value."""
        self.canvas.itemconfig(self.rectangles[index], fill=color)
        self.root.update()
        self.root.after(100,self.root.update())

    def update_rectangles(self):
        """Helper method that updates the rectangles coordinates (x1, y1, x2, y2) when they need
        to be changed."""
        for i, value in enumerate(self.data):
            self.canvas.coords(self.rectangles[i], i * 30, 300, (i + 1) * 30, 300 - value * 3)

    def show_message(self, message):
        """Will display message once sorting is completed."""
        for rect in self.rectangles:
            self.canvas.itemconfig(rect, outline=matched_value_highlight)
        self.root.update()
        messagebox.showinfo("Sort Completed", message)

    ############################################################################
    # main loop
    ############################################################################
    def main_loop(self):
        self.root.mainloop()
