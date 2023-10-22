"""
Tabitha Geiger

main file for GUI

***this should be subbed out of the main file later. 
the main.py file will be used to call on the other files in this folder***
"""
import tkinter as tk
import module_4pt1

def main():
    gui = module_4pt1.GuiBasics()
    gui.main_loop()

if __name__ == "__main__":
    main()