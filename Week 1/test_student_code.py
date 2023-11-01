"""
Motor.py

Leland Wendel
July 3, 2023

Implements an engine as a complex class.
"""


class Motor:
    """A class to represent a car engine."""

    def __init__(self, cylinders, liters, aspiration, code):
        """Instantiation"""

        self.cylinders = cylinders
        self.liters = liters
        self.aspiration = str(aspiration)
        self.code = str(code)

    def get_horsepower(self):
        """Returns potential HP based on user input and available options."""
        if self.aspiration == "Turbocharged":
            return int(self.liters * 120)
        if self.aspiration == "Supercharged":
            return int(self.liters * 80 + self.liters * 80 / 2)
        if self.aspiration == "Naturally Aspirated":
            return int(self.liters * 80)

    def get_cost(self):
        """Returns cost to build the motor, based on user specifications."""
        if self.aspiration == "Turbocharged":
            return int(self.cylinders * self.liters * 100)
        elif self.aspiration == "Supercharged":
            return int(self.cylinders * self.liters * 150)
        else:
            return int(self.cylinders * self.liters * 50)

    def get_redline(self):
        """Returns the redline (max RPM) of the motor."""
        return int(self.cylinders / self.liters * 3000)


    #### reading through the code
    def create_file(self) -> None:
        testmotor = Motor(200, 30, "Naturally Aspirated", "code")

        hp = testmotor.get_redline()
        print(f"hp = {hp}")

        with open(self.aspiration, "w") as output_file:
            output_file.write((str(self.aspiration)) + "\n")
            output_file.write((str(hp)) + "\n")

testfile = Motor(200, 30, "Naturally Aspirated", "code")

testfile.create_file()