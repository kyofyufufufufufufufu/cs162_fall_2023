"""
Testing Gui

Attempt to create a few PyTests that will work with the data behind the scenes
(maybe a test that checks the default value in your text box, label, or that some
variables has an expected value)

"""

#testing gui output

import tkinter as tk

from module_4pt2 import GuiBasics


# Test finding the smallest number
def test_find_smallest_number():
    gui = GuiBasics()
    gui.root, gui.label1, gui.entry_list, gui.find_small_button, gui.next_smallest = create_test_gui()
    for i, gui.entry_line in enumerate(gui.entry_list):
        gui.entry_line.insert(0, str(i + 1))
    gui.find_small_button.invoke()
    assert gui.label1.cget("text") == "1"