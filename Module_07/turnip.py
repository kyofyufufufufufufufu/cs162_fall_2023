"""turnip class"""
import plant
import wiltingError

class Turnip(plant.Plant):
    """turnip subclass requirements"""
    def __init__(self):
        # plant.Plant.__init__(self)
        super().__init__()

        self.name = "turnip"
        #total capacity of water per week
        self.water_required = 20
        #season(s) allowed to plant
        self.season = self.season[0], self.season[2]
        #total capacity of sunlight before scorching occurs
        self.sunlight = {2: "partial"}
        #can the plant be harvested
        self.harvest = True

    # def check_sunlight(self, user_input_sun):
    #     """Override the check_sunlight method for Turnip."""
    #     try:
    #         user_input_sun = int(user_input_sun)
    #         return user_input_sun == 2  # Assuming partial sun/shade is the second option
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")
    #         return False