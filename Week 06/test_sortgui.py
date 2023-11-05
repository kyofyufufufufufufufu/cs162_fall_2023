"""pytest for sortgui.py"""

import tkinter as tk
from tkinter import messagebox
from sortgui import SortGui

def test_sort():
    """testing sorting method"""
    root = tk.Tk()
    test2 = SortGui()
    
    #negative test
    initial_order = test2.data.copy()
    test2.sort()
    assert test2.data != initial_order
    
    root.destroy()

def test_show_message():
    """testing message popup"""
    root = tk.Tk()
    test3 = SortGui()
    
    #positive test
    test3.show_message("test test test")
    assert messagebox._show.called
    assert messagebox._show.call_args[0][0] == "Sort Completed"
    assert messagebox._show.call_args[1]["message"] == "test test test"
    
    root.destroy()

if __name__ == "__main__":
    test_highlight_value()
    test_sort()
    test_show_message()
