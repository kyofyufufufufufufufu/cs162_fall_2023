"""game.py"""

import pygame
from dialogue import *
from pygame import mixer
from scenes import Scene

from gameStateManager import GameStateManager as gs
from scenes import *

#setting up intialization
FPS = 60
WIDTH, HEIGHT = 1280, 720
running = True

#Game class that will help walk through all events in the game
class Game():
    def __init__(self):
        #initializing pygame and mixer for music/sounds
        pygame.init()
        mixer.init()
        
        
        mixer.music.load("assets/music_main.wav")
        mixer.music.set_volume(1)
        mixer.music.play()
        
        self.SCREEN = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption("Menu")

        self.BG = pygame.image.load("assets/bg_main.png")
        self.timer = pygame.time.Clock()
        self.game_state_manager = gs() 

    def run(self):
        """runs the game based on keywords that all the gamestatemanager to move through events"""
        self.game_state_manager.set_state(MainMenuScene(self.SCREEN))
        
        while running:
            self.game_state_manager.handle_events()
            transition_result = self.game_state_manager.current_state.update()
            #these if-elif statements help to set and move through scenes based on keywords as mentioned above
            if transition_result == 'options':
                self.game_state_manager.set_state(OptionsScene(self.SCREEN))  #switch scene
            elif transition_result == 'game':
                self.game_state_manager.set_state(IntroScene(self.SCREEN))  # switch to intro
            elif transition_result == 'main_menu':
                self.game_state_manager.set_state(MainMenuScene(self.SCREEN))  # Switch to the game scene
            elif transition_result == 'start_game_rules':
                Scene.fade(self,1280,720) #fade used for proper transition between scenes
                self.game_state_manager.set_state(StartGameScene(self.SCREEN))
            elif transition_result == 'water_game':
                self.game_state_manager.set_state(GameScene(self.SCREEN))
            elif transition_result == 'player_win':
                self.game_state_manager.set_state(PlayerWinScene(self.SCREEN))
            elif transition_result == 'game_over':
                self.game_state_manager.set_state(GameOverScene(self.SCREEN))
            self.game_state_manager.current_state.draw(self.SCREEN) #draws each scene

            pygame.display.flip()
            self.timer.tick(FPS)
