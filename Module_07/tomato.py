"""tomato class"""
import plant
import wiltingError

class Tomato(plant.Plant):
    """tomato subclass requirements"""
    def __init__(self):
        plant.Plant.__init__(self)

        self.name = "tomato"
        #total capacity of water per week
        self.water_required = 40
        #season(s) allowed to plant
        self.season = self.season[0], self.season[1]
        #total capacity of sunlight before scorching occurs
        self.sunlight = {1: "full"}
        #can the plant be harvested
        self.harvest = True

    # def check_sunlight(self, user_input_sun):
    #     """Override the check_sunlight method for Turnip."""
    #     try:
    #         user_input_sun = int(user_input_sun)
    #         return user_input_sun == 1  # Assuming partial sun/shade is the second option
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")
    #         return False