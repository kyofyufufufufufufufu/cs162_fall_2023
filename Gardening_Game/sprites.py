"""
sprites.py

loads all sprites used for the game
"""

import pygame

carrot_image = pygame.image.load("assets/img_bag_carrot.png")
tomato_image = pygame.image.load("assets/img_bag_tomato.png")
turnip_image = pygame.image.load("assets/img_bag_turnip.png")

hat_image = pygame.image.load("assets/img_hat.png")
hose_image = pygame.image.load("assets/img_hose.png")
note1_image = pygame.image.load("assets/img_note1.png")
note2_image = pygame.image.load("assets/img_note2.png")
sack1_image = pygame.image.load("assets/img_sack.png")
sack2_image = pygame.image.load("assets/img_sack2.png")
wateringcan_image = pygame.image.load("assets/img_wateringcan.png")

carrot_rect = carrot_image.get_rect(center=(230//2, 150//2))
tomato_rect = tomato_image.get_rect(center=(230//2, 150//2))
turnip_rect = turnip_image.get_rect(center=(230//2, 150//2))