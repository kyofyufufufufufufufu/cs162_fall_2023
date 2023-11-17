"""
Implementing Parent class (Plant)
"""
from seasonalError import SeasonalError

import wiltingError


class Plant():
    def __init__(self):
        """default settings for plants"""
        self.name = "default"
        #water will be on a 0-100 scale
        self.water_required = 0
        #seasons as a list required for certain plants
        self.season = ["spring", "summer", "fall", "winter", "any"]
        #sunlight will be on 3 levels: Full sun, partial sun, and full shade.
        self.sunlight = {1: "full", 2: "partial", 3: "shade"}
        #can the plant be harvested, automatically set to True
        self.harvest = True
    
    def __str__(self):
        """print attributes"""
        return f"""name: {self.name}\nwater amount: {self.water_required}\nseason(s): {self.season}
sumlight amount: {self.sunlight}\nharvestable: {self.harvest}"""
    
    def add_water(self):
        """adding water as needed for the plant"""
        self.water_added = 0  # Initialize outside the loop
        while True:
            try:
                user_input = int(input("How many units of water will you add? "))
                print(f"Before update: {self.water_added}")

                if user_input == 0:
                    print("Please enter a number greater than zero.")
                elif user_input < 0:
                    print("Please enter a positive number.")
                else:
                    self.water_added += user_input
                    print(f"After update: {self.water_added}")

                    if self.water_added == self.water_required:
                        print("Perfect! Your plant looks very happy!!")
                        break
                    elif self.water_added > self.water_required:
                        raise wiltingError.OverwateringError("Error overfilling!")

            except ValueError:
                print("That is an invalid input. Please enter a number.")

    def season_search(self):
        """season select"""
        print(f"""It's springtime, which means it's time to plant some seeds.\n
        Which seeds would you like to plant?
              1. Turnip
              2. Tomato
              """)
        while True:
            try:
                plant_selection = int(input("Please enter here: "))
                if plant_selection == 1:
                    break
                elif plant_selection == 2:
                    print("That plant is out of season.")
                    raise SeasonalError("SeasonalError occured, inability to plant out of season.")
                else:
                    print("Invalid input. Try again")
                    continue
            except ValueError:
                print("Try again.")
                continue

    def check_sunlight(self, user_input):
        try:
            user_input = int(user_input)
            if user_input in self.sunlight:
                selected_option = self.sunlight[user_input]
                return selected_option
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
                return None  # or raise an exception if necessary
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None  # or raise an exception if necessary