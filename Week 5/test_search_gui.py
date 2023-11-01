import tkinter as tk
from search_gui import search

def test_search_gui():
    root = tk.Tk()
    canvas = tk.Canvas(root)
    entry = tk.Entry(root)
    status_label = tk.Label(root)

    entry.insert(0, "42")  # Simulate user input
    data = [1, 2, 3, 4, 42, 6, 7]  # 42 is in the data


def test_search_gui_not_found():
    root = tk.Tk()
    canvas = tk.Canvas(root)
    entry = tk.Entry(root)
    status_label = tk.Label(root)

    entry.insert(0, "99")
    #99 is not valid in the data
    data = [1, 2, 3, 4, 42, 6, 7]

    def fake_search():
        for i, value in enumerate(data):
            canvas.itemconfig(i, fill="white")
            if value == 99:
                canvas.itemconfig(i, fill="green")
                status_label.config(text="Value 99 found at index 4")
            else:
                canvas.itemconfig(i, fill="red")
            root.update()
            root.after(250)

    search_button = tk.Button(root, text="Search", command=fake_search)
    search_button.invoke()  # Trigger the search process

    assert status_label.cget("text") == "Value 99 not found in the dataset"
