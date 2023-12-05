"""player.py

creates the Raindrop, Reducing Object (acid rain), as well as the Plant and
its Sapling, Young Plant, and Almost Mature subclasses.
"""

import pygame
import random
from constants import HEIGHT, WIDTH

class Raindrop:
    """raindrop is used to add water to the plants to help them grow, this class is connected to the Plant class
    in relation to the specific subclass's water_capacity and the meter's incrementation"""
    def __init__(self, WIDTH, HEIGHT, stage):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 10), 0, 10, 10) #10x10 pixels in size
        self.speed = random.randint(2, 5) #determines speed of raindrop
        self.value = 2 #the value determines how much capacity fills the meter
        self.speed_y = 2 
        self.direction = 1

        #parameters change based on growth stage of plant
        if stage == 2:
            self.speed += 1  #increases speed for stage 2
        elif stage == 3:
            self.speed += 2  #increases speed even more for stage 3
    def update(self):
        self.rect.y += self.speed

class ReducingObject:
    """Reducing Object (called Acid Rain in the game) decrements the plant's growth with a -1 value and is directly
    related to the meter, it uses very similar properties to the Raindrop class"""
    def __init__(self, WIDTH, HEIGHT, stage):
        self.rect = pygame.Rect(random.randint(0, WIDTH - 10), 0, 10, 10)
        self.speed = random.randint(2, 5)
        self.value = -1  #negative value to reduce the meter
        self.speed_y = 2 
        self.direction = 1

        #parameters change based on growth stage
        if stage == 2:
            self.speed += 1  #increases speed for stage 2
        elif stage == 3:
            self.speed += 2  #increases speed even more for stage 3
    def update(self):
        self.rect.y += self.speed

class Meter:
    """the meter is used both visually and to measure the plant's water_capacity"""
    def __init__(self):
        self.value = 0
    def increment(self, value):
        self.value += value

class Plant:
    """the plant class has attributes like water capacity to determine a specific subclass's need for water in order to grow
    or in the case of stage 3, how much in order to win"""
    def __init__(self, stage, water_capacity):
        self.stage = stage #used to determine growth and what stages must be used
        self.water_capacity = water_capacity
        self.growth_stage = stage

    def grow(self, meter_value):
        """the grow function will only be used for subclasses, so it raises an error in the parent Plant class
        if attempted"""
        raise NotImplementedError("Subclasses must implement the grow method.")

class Sapling(Plant):
    """sapling is the first stage in the plant's growth cycle"""
    def __init__(self):
        super().__init__(stage=1, water_capacity=12)

    def grow(self, meter_value):
        if meter_value >= 12:
            return YoungPlant() #moves to next stage
        return self

class YoungPlant(Plant):
    """YoungPlant is the second stage in the plant's growth cycle"""
    def __init__(self):
        super().__init__(stage=2, water_capacity=28)

    def grow(self, meter_value):
        if meter_value >= 28:
            return AlmostMature() #moves to last stage after water capacity has been met
        return self #just like the sapling, it will continue to return its own stage until its conditions have been met

class AlmostMature(Plant):
    """the plant's form before the final form (tomato)"""
    def __init__(self):
        super().__init__(stage=3, water_capacity=50)

    def grow(self, meter_value):
        if meter_value >= self.water_capacity:
            return self #a special return value will be raised in the main scene.py function
        return self
