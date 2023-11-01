"""
Author: Tabitha Geiger
Date: 09/29/2023

The purpose of this lab is to create a Class with subclasses. In addition, methods will be utilized.

Tests:

housetest = House(100, 100, 100, 100)
Input
housetest.get_sq_feet

Output

Total bedroom square feet: 100 sq feet
Total livingroom square feet: 100 sq feet
Total kitchen square feet: 100 sq feet
Total bathroom square feet: 100 sq feet

Total square feet of house is: 400 sq feet.


housetest.lights_on_off()

Input
Off

Output
"The lights are now off. Goodnight."

housetest.lockdoor()

Input
Yes

Output
"The door is now locked."
"""
import sys


class House:
    """Represents a house and its rooms."""
    def __init__(self)-> None:
        self.livingroom: int = 100
        self.kitchen: int = 100
        self.bedroom: int = 100
        self.bathroom: int = 100
    
    def get_sq_feet(self) -> int:
        """Uses attributes from __init__ to determine total square feet of house."""
        total = (self.livingroom + self.kitchen + self.bedroom + self.bathroom)
        return total

    def print_total_sq_ft(self) -> None:
        total = House()
        result = total.get_sq_feet()
        print(f"Total square feet: {result} sq feet\n")
        print(f"""Total bedroom square feet: {self.bedroom} sq feet\nTotal livingroom square feet: {self.livingroom} sq feet\nTotal kitchen square feet: {self.kitchen} sq feet\nTotal bathroom square feet: {self.bathroom} sq feet\n""")
    
    def lights_on_off(self) -> None:
        """Lights on or off based on user input."""
        light_on_off = input("Turn lights on or off...\n Enter 'on' or 'off': ")
        while light_on_off.upper() != "ON" and light_on_off.upper() != "OFF":
            print("Invalid input. Try again.")
            light_on_off = input("Turn lights on or off...\n Enter 'on' or 'off': ")
        if light_on_off.upper() == "ON":
            print("Lights are now on.\n")
        elif light_on_off.upper() == "OFF":
            print("Lights are now off. Good night.\n")
    
    def lockdoor(self) -> None:
        """Locks or keeps door unlocked based on user input."""
        lock_door = input("Lock the door? Y or N? ")
        while lock_door.lower() != "y" and lock_door.lower() != 'n':
            print("That is not a valid input. Please try again.")
            lock_door = input("Lock the door? Y or N? ")
        if lock_door.lower() == "y":
            print("The door is now locked.\n")
        elif lock_door.lower() == 'n':
            print("The door is still unlocked.\n")

    def goodbye(self) -> None:
        """Exits the program."""
        message = input("Press Y to exit: ")
        while message.lower() != "y":
            print("That is an invalid input. Try again.")
            message = input("Press Y to exit: ")
        if message.lower() == "y":
            sys.exit("Goodbye.")

    def create(self) -> None:
        output_file = open(str(self.livingroom), "w")
        output_file.write(str(self.livingroom) + " square feet" + "\n")
        output_file.write(str(self.bedroom) + " square feet" + "\n")
        output_file.write(str(self.kitchen) + " square feet" + "\n")
        output_file.write(str(self.bathroom) + " square feet" + "\n")
        output_file.close()

housetest = House()
housetest.create()