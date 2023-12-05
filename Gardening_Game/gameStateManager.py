# gameStateManager.py

import pygame
import sys
import os

class GameStateManager:
    def __init__(self):
        self.current_state = None

    def set_state(self, new_state):
        self.current_state = new_state

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Example: Switch to the game scene when the spacebar is pressed
                    self.set_state(GameScene())

