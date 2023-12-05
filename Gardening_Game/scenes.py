"""scenes.py, holds all scenes used for the game"""

#all the imports used
import pygame
import sys
import os
import sprites
import random
from dialogue import *
from pygame import mixer
from constants import HEIGHT, WIDTH

from player import Raindrop, Meter, Sapling, ReducingObject
from button import Button

FPS = 60
running = True

class Scene:
    """creating the parent Scene class"""
    def __init__(self, SCREEN):
        self.SCREEN = SCREEN
    
    def update(self):
        """raises an error for itself, but update will be used to create the scenes after initialization"""
        raise NotImplementedError("Subclasses must implement the update method.")
    
    def draw(self):
        """draws the scene onto the screen"""
        raise NotImplementedError("Subclasses must implement the draw method.")
    
    def get_font(self, font_type, size):
        """returns text in the desired font and size"""
        self.font_type = font_type
        self.size = size
        font = pygame.font.Font(self.font_type, self.size)
        return font
    
    def text_scroller(self, message_list):
        """returns a True/False statement and used in 'cutscenes' or passive events with dialogue."""
        self.font = self.get_font("assets/fonttext.ttf", 26)
        self.snip = self.font.render("", True, "white")
        self.counter = 0
        self.speed = 3 #if a faster speed is desired try using 1/3 

        done = False
        run = True

        self.index = 0
        self.message = message_list[self.index] #runs through the list of dialogue from dialogue.py
        
        self.SFX_TEXT = mixer.Sound("assets/sfx_text.mp3")
        self.timer = pygame.time.Clock()

        while run:
            self.timer.tick(FPS)
            pygame.draw.rect(self.SCREEN, "black", [0, 500, WIDTH, HEIGHT-500])

            if self.counter < self.speed * len(self.message):
                #moves through the text one letter at a time with a dependency on the speed used
                self.SFX_TEXT.play()
                self.counter += 1
            elif self.counter >= self.speed * len(self.message):
                #once done through the list, sfx will stop and done will be set to true
                #if end of list then the text_scroller function will break the while loop
                done = True
                self.SFX_TEXT.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #quit the program using the x in right-hand corner
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #left mouse click button will move to next index in the list so long as there's more to be read
                    if event.button == 1 and done and self.index < len(message_list) - 1:
                        self.index += 1
                        done = False #done is reset to false if there's more left in list of dialogue
                        self.message = message_list[self.index]
                        self.counter = 0
                    if event.button == 1 and done:
                        run = False #break loop

            self.snip = self.font.render(self.message[0: self.counter//self.speed], True, "white") #creates text
            self.SCREEN.blit(self.snip, (10, 510)) #puts text onto screen at desired location
            pygame.display.flip() #displays all

        return done
   
    def fade(self, width, height): 
        """creates a fade to black transition to  move through scenes, requires width and height of screen as parameters"""
        fade = pygame.Surface((WIDTH, HEIGHT))
        fade.fill((0,0,0))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            self.SCREEN.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)
    
    def display_text(self, text, duration_seconds, x_pos, y_pos):
        """creates a rectangle with text that fades depending on seconds and where to place it on the screenn"""
        font_size = 24
        font = pygame.font.Font("assets/fonttext.ttf", font_size)
        text_render = font.render(text, True, "white")

        #creates a transparent rectangle
        rect_width = text_render.get_width() + 20  
        rect_height = text_render.get_height() + 20  
        rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA) #transparency
        pygame.draw.rect(rect_surface, (0, 0, 0, 128), (0, 0, rect_width, rect_height))

        #puts text onto rectangle
        text_rect = text_render.get_rect(center=(rect_width // 2, rect_height // 2))
        rect_surface.blit(text_render, text_rect)

        start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - start_time < duration_seconds * 1000: #seconds needed for fadeout to begin
            alpha = min((pygame.time.get_ticks() - start_time) / (duration_seconds * 10), 255)
            rect_surface.set_alpha(alpha)
            self.SCREEN.blit(rect_surface, (x_pos - rect_width // 2, y_pos - rect_height // 2))
            pygame.display.flip()

        rect_surface.set_alpha(0)
        self.SCREEN.blit(rect_surface, (x_pos - rect_width // 2, y_pos - rect_height // 2))
        pygame.display.flip()

class MainMenuScene(Scene):
    """creates main menu scene with gui interface for 'play'-starting the game, 'options'- for credits, 'quit to exit
    and a 'skip' button to skip straight into the watering game"""
    def __init__(self, SCREEN):
        super().__init__(SCREEN)
        self.BG = pygame.image.load("assets/bg_main.png")

    def update(self):
        MOUSE_POS = pygame.mouse.get_pos()

        #creating screen and buttons for GUI

        self.SCREEN.blit(self.BG, (0, 0))

        MENU_BUTTON_IMAGE = pygame.image.load("assets/button_play.png")
        MENU_BUTTON_SFX = pygame.mixer.Sound("assets/sfx_correct.mp3")
        MENU_FONT = "assets/fontmain.ttf"

        MENU_TEXT = self.get_font(MENU_FONT, 80).render("GARDEN GAME", True, "#d3f5e2")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 180))

        #play, options, quit, and skip buttons
        PLAY_BUTTON = Button(image=MENU_BUTTON_IMAGE, pos=(640, 360),
                             text_input="play", font=self.get_font("assets/fontmain.ttf", 40),
                             base_color="#022119", hovering_color="White")
        OPTIONS_BUTTON = Button(image=MENU_BUTTON_IMAGE, pos=(640, 460),
                                text_input="options", font=self.get_font("assets/fontmain.ttf", 40),
                                base_color="#022119", hovering_color="White")
        QUIT_BUTTON = Button(image=MENU_BUTTON_IMAGE, pos=(640, 560),
                             text_input="quit", font=self.get_font("assets/fontmain.ttf", 40),
                             base_color="#022119", hovering_color="White")
        SKIP_BUTTON = Button(image=None, pos=(1100, 640),
                             text_input="skip", font=self.get_font("assets/fontmain.ttf", 20),
                             base_color="#022119", hovering_color="White")       

        self.SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SKIP_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(self.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if user clicks right mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MOUSE_POS):
                    MENU_BUTTON_SFX.play()
                    pygame.mixer.music.fadeout(1500)
                    pygame.time.delay(1500)
                    #game starts
                    return 'game'
                if OPTIONS_BUTTON.checkForInput(MOUSE_POS):
                    MENU_BUTTON_SFX.play()
                    #goes to options screen
                    return 'options'
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if SKIP_BUTTON.checkForInput(MOUSE_POS):
                    MENU_BUTTON_SFX.play()
                    pygame.mixer.music.fadeout(1500)
                    pygame.time.delay(1500)
                    #immediately jumps to the watering game
                    return 'water_game'


        return None  #transition isn't needed to move to new scene as button selection does this

    def draw(self, SCREEN):
        pygame.display.update()

class OptionsScene(Scene):
    """Options subclass used for credits and resources/assets used in the game after pressing the 'credits' button
    or returning to main menu"""
    def __init__(self, SCREEN):
        super().__init__(SCREEN)
        self.BG = pygame.image.load("assets/bg_main.png")

    def update(self):
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        self.SCREEN.blit(self.BG, (0, 0))

        MENU_BUTTON_SFX = pygame.mixer.Sound("assets/sfx_correct.mp3") #sfx used after clicking the button

        OPTIONS_IMG = pygame.image.load("assets/button_play.png")
        OPTIONS_TEXT = self.get_font("assets/fontmain.ttf",40).render("OPTIONS", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #credits and back button
        OPTIONS_ASSET_LIST = Button(image= OPTIONS_IMG, pos=(640, 460),
                                    text_input="credits", font=self.get_font("assets/fontmain.ttf", 40),
                                    base_color="#022119", hovering_color="White")
        OPTIONS_BACK = Button(image=None, pos=(640, 560), 
                                    text_input="back", font=self.get_font("assets/fontmain.ttf",40), 
                                    base_color="#022119", hovering_color="White")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(self.SCREEN)            
        OPTIONS_ASSET_LIST.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_ASSET_LIST.update(self.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #if left mouse button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    MENU_BUTTON_SFX.play()
                    return 'main_menu' #return to main menu
                if OPTIONS_ASSET_LIST.checkForInput(OPTIONS_MOUSE_POS):
                    MENU_BUTTON_SFX.play()
                    os.system("notepad.exe assets/assets_list.txt") #pop notepad window of all credits will appear
                    return None

        return None  #no transition

    def draw(self, SCREEN):
        pygame.display.update()

class IntroScene(Scene):
    def __init__(self, SCREEN):
        super().__init__(SCREEN)
        self.scene_state = "train" #setting scene name

    def update(self):
        train_image = pygame.image.load("assets/img_train.png")
        picture = pygame.transform.scale(train_image, (1280, 720))
        
        #if-elif conditions used to transition through scenes
        if self.scene_state == "train": 
            self.fade(1280,720)
            self.SCREEN.blit(picture, (0, 1))

            mixer.music.load("assets/sfx_train.mp3")
            pygame.time.delay(2000)
            mixer.music.play(0)

            done = self.text_scroller(m1) #setting text_scroller to 'done' for True or False return value

            if done:
                self.scene_state = "paper"  #move to next scene
                paper_sfx = pygame.mixer.Sound("assets/sfx_paper.wav")
                paper_sfx.play()

        elif self.scene_state == "paper": #next scene is established if conditions are met
            paper = pygame.image.load("assets/img_paper.png")
            self.SCREEN.blit(paper, (240, 100))
            
            pygame.display.update()
            pygame.time.delay(1500)  # Delay before showing the text scroller
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.scene_state = "text_scroller" #move to next (3rd) scene

        elif self.scene_state == "text_scroller": #third scene
            self.SCREEN.blit(picture, (0, 1))
            done = self.text_scroller(m2) #text scroller function with the next list of dialogue set up
            if done:
                self.scene_state = "end"  #move to final scene

        elif self.scene_state == "end": #setting final scene
            done = self.text_scroller(m3)
            if done:
                pygame.mixer.music.fadeout(1500)
                return 'start_game_rules' #move to the next 'level' which is the StartGameScene'

        pygame.display.update()

    def draw(self, SCREEN):
        pygame.display.update()
        pygame.time.delay(300)

class StartGameScene(Scene):
    """StartGameScene's level opens with the rules of the following scene/level. Players can choose between seeds and
    depending on the season, only the correct seed chosen will move to the game (tomatoes in this version of the game)"""
    def __init__(self, SCREEN):
        super().__init__(SCREEN)
        mixer.music.load("assets/music_shop.mp3")
        mixer.music.play(-1)
        self.scene_state = "start_game_rules"
        self.bg_color = (0, 0, 0, 128)  #transparent screen bg
        self.display_text_timer = 0
        self.display_text_duration = 3000  #this duration is used to display the text from the function 'display_text()'

    def update(self):
        shelf_image = pygame.image.load("assets/img_shelf.png")
        bg = pygame.transform.scale(shelf_image, (1280, 720))
        self.SCREEN.blit(bg, (0, 0))
        SHOP_MOUSE_POS = pygame.mouse.get_pos()

        if self.scene_state == "start_game_rules":
            #beginning scene with image of rules
            self.bg_end = pygame.image.load("assets/season_template_game_rules.png")
            self.bg_rect = self.bg_end.get_rect()

            
            x = (WIDTH - self.bg_rect.width) // 2
            y = (HEIGHT - self.bg_rect.height) // 2
            
            self.SCREEN.blit(self.bg_end, (x,y))

            pygame.display.update()
            pygame.time.delay(400)  #delay before showing the text scroller
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.scene_state = "select"  #move to select stage

        elif self.scene_state == "select":

            BOTTOM_TEXT = self.get_font("assets/fontmain.ttf", 20).render(
                "please select the appropriate seeds to get started", True, "Black")
            BOTTOM_RECT = BOTTOM_TEXT.get_rect(center=(520, 700)) #bottom text to help user navigate to next scene
            self.SCREEN.blit(BOTTOM_TEXT, BOTTOM_RECT)
            incorrect_sfx = pygame.mixer.Sound("assets/sfx_incorrect.wav")
            correct_sfx = pygame.mixer.Sound("assets/sfx_complete.mp3")

            #tomato, carrot, and turnip buttons used to move to next scene
            TOMATO_BUTTON = Button(image=sprites.tomato_image,
                                   pos=(260 + sprites.tomato_image.get_width() / 2,
                                        43 + sprites.tomato_image.get_height() / 2),
                                   text_input="blank", font=self.get_font("assets/fonttext.ttf", 1),
                                   base_color="#022119", hovering_color="White")
            CARROT_BUTTON = Button(image=sprites.carrot_image,
                                   pos=(100 + sprites.carrot_image.get_width() / 2,
                                        43 + sprites.carrot_image.get_height() / 2),
                                   text_input="blank", font=self.get_font("assets/fonttext.ttf", 1),
                                   base_color="#022119", hovering_color="White")
            TURNIP_BUTTON = Button(image=sprites.turnip_image,
                                   pos=(400 + sprites.turnip_image.get_width() / 2,
                                        43 + sprites.turnip_image.get_height() / 2),
                                   text_input="blank", font=self.get_font("assets/fonttext.ttf", 1),
                                   base_color="#022119", hovering_color="White")

            #blit background
            self.SCREEN.blit(bg, (0, 1))

            #blit individual images
            for item, position in [
                (sprites.carrot_image, (100, 43)),
                (sprites.tomato_image, (260, 43)),
                (sprites.turnip_image, (400, 43)),
                (sprites.hose_image, (100, 255)),
                (sprites.hat_image, (420, 255)),
                (sprites.sack1_image, (100, 430)),
                (sprites.sack2_image, (500, 425)),
                (sprites.note1_image, (800, 200)),
                (sprites.note2_image, (975, 100)),
                (sprites.wateringcan_image, (300, 440))
            ]:
                self.SCREEN.blit(BOTTOM_TEXT,BOTTOM_RECT)
                self.SCREEN.blit(item, position)

            for button in [TOMATO_BUTTON, CARROT_BUTTON, TURNIP_BUTTON]:
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #left mouse click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #tomato is the only option that moves game to next scene
                    if TOMATO_BUTTON.checkForInput(SHOP_MOUSE_POS):
                        mixer.Sound.play(correct_sfx)
                        pygame.mixer.music.stop()
                        pygame.time.delay(200)
                        return 'water_game'
                    #both carrot and turnip will produce an 'error' sound if selected
                    elif CARROT_BUTTON.checkForInput(SHOP_MOUSE_POS):
                        mixer.Sound.play(incorrect_sfx)
                        self.display_text("Cannot be grown in this season.", 2, 200 + sprites.carrot_image.get_width()/2,
                                          123 + sprites.carrot_image.get_height()/2)

                    elif TURNIP_BUTTON.checkForInput(SHOP_MOUSE_POS):
                        mixer.Sound.play(incorrect_sfx)
                        self.display_text("Cannot be grown in this season.", 2, 500 + sprites.carrot_image.get_width()/2,
                                          123 + sprites.carrot_image.get_height()/2)
    def draw(self, SCREEN):
        pygame.display.flip()

class GameScene(Scene):
    """GameScene is the watering game that requires players to collect raindrops and avoid acid rain in
    order for their plant to grow to its fully mature stage and harvest it. 3 sprites are used to update
    the player sprite: sapling, young plant, and almost mature. this scene specifically uses all classes
    and subclasses from player.py. A timer with a countdown of 90 seconds will be used."""
    def __init__(self, SCREEN):
        super().__init__(SCREEN)
        mixer.music.load("assets/music_watergame.mp3")
        mixer.music.play(-1)
        
        #player sprite assets
        self.player_sapling = pygame.image.load("assets/img_tomato_plant1.png") 
        self.player_young_plant = pygame.image.load("assets/img_tomato_plant2.png")
        self.player_almost_mature = pygame.image.load("assets/img_tomato_plant3.png")

        #initializes the player sprite as the sapling for start of game
        self.current_player_sprite = self.player_sapling

        #initializing other variables
        self.player_rect = self.current_player_sprite.get_rect(center=(WIDTH // 2, HEIGHT-110))
        self.reducing_objects = []
        self.raindrops = []  #list to store Raindrop objects
        self.meter = Meter()
        self.plant = Sapling()  #initialize with the Sapling subclass
        self.clock = pygame.time.Clock()

        #sounds/music
        self.collision_sfx = pygame.mixer.Sound("assets/sfx_drop.mp3")  # Replace with the actual path
        self.collision_sfx.set_volume(0.2)
        self.neg_collision_sfx = pygame.mixer.Sound("assets/sfx_sun.wav")
        self.neg_collision_sfx.set_volume(0.5)
        self.upgrade1_sfx = pygame.mixer.Sound("assets/sfx_correct.mp3")
        self.upgrade2_sfx = pygame.mixer.Sound("assets/sfx_correct2.mp3")
        self.downgrade_sfx = pygame.mixer.Sound("assets/sfx_incorrect.wav")
        self.timer = 90 #90 second timer
        self.last_time = pygame.time.get_ticks()

    def update(self):
        self.SCREEN.fill("sky blue") 
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.last_time) / 1000.0  # Convert milliseconds to seconds
        self.last_time = current_time


        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_rect.left > 0:
            self.player_rect.x -= 5
        if keys[pygame.K_RIGHT] and self.player_rect.right < WIDTH:
            self.player_rect.x += 5

        #update and draw raindrops
        for raindrop in self.raindrops:
            raindrop.update()
            pygame.draw.rect(self.SCREEN, (0, 0, 255), raindrop.rect)

        #update and draw reducing objects
        for reducing_object in self.reducing_objects:
            reducing_object.update()
            pygame.draw.rect(self.SCREEN, (255, 0, 0), reducing_object.rect)

        #draw player
        self.SCREEN.blit(self.current_player_sprite, self.player_rect)

        #drawing the meter as a green progress bar that goes across the screen
        meter_width = int((self.meter.value / self.plant.water_capacity) * 1280)
        pygame.draw.rect(self.SCREEN, (0, 255, 0), (10, 10, meter_width, 20))

        #draw plant stage on top left corner
        plant_text = self.get_font("assets/fontmain.ttf", 24).render(f"Plant Stage: {self.plant.growth_stage}", True, "black")
        self.SCREEN.blit(plant_text, (10, 40))

        #check for collisions with raindrops
        for raindrop in self.raindrops:
            if self.player_rect.colliderect(raindrop.rect):
                self.meter.increment(raindrop.value) #if player hits raindrop, the meter increases by set raindrop's value
                self.raindrops.remove(raindrop) #raindrop is then removed from list
                self.collision_sfx.play() #sfx when collision occurs (positive)

        #check for collisions with reducing objects
        for reducing_object in self.reducing_objects:
            #very similar to raindrops 
            if self.player_rect.colliderect(reducing_object.rect):
                self.meter.increment(reducing_object.value) #if player hits reducing object, the meter decreases by RO's value
                self.reducing_objects.remove(reducing_object)
                self.neg_collision_sfx.play() #sfx when collision occurs (negative)

        #remove raindrops that have gone off-screen
        self.raindrops = [raindrop for raindrop in self.raindrops if raindrop.rect.y < HEIGHT]

        #generates new raindrops randomly for each stage
        if self.plant.growth_stage == 1 and random.random() < 0.02:
            new_raindrop = Raindrop(WIDTH, HEIGHT, self.plant.growth_stage)
            self.raindrops.append(new_raindrop)
        elif self.plant.growth_stage == 2 and random.random() < 0.03:
            #probability is increased to create more raindrops
            new_raindrop = Raindrop(WIDTH, HEIGHT, self.plant.growth_stage)
            self.raindrops.append(new_raindrop)
        elif self.plant.growth_stage == 3 and not self.meter.value >= self.plant.water_capacity:
            #probability is further increased to create more raindrops so long as the player hasn't won
            if random.random() < 0.055:
                new_raindrop = Raindrop(WIDTH, HEIGHT, self.plant.growth_stage)
                new_raindrop.rect.y = 0  #set the initial position at the top
                self.raindrops.append(new_raindrop)

        #update and draw the plant based on meter value
        self.plant = self.plant.grow(self.meter.value)

        #removes reducing objects that have gone off-screen
        self.reducing_objects = [reducing_object for reducing_object in self.reducing_objects if reducing_object.rect.y < HEIGHT]

        #generate new reducing objects randomly for each stage
        if self.plant.growth_stage == 1 and random.random() < 0.02:
            new_reducing_object = ReducingObject(WIDTH, HEIGHT, self.plant.growth_stage)
            self.reducing_objects.append(new_reducing_object)
        elif self.plant.growth_stage == 2 and random.random() < 0.03:
            #RO's probability increases with each level
            new_reducing_object = ReducingObject(WIDTH, HEIGHT, self.plant.growth_stage)
            self.reducing_objects.append(new_reducing_object)
        elif self.plant.growth_stage == 3 and not self.meter.value >= self.plant.water_capacity:
            if random.random() < 0.05:
                new_reducing_object = ReducingObject(WIDTH, HEIGHT, self.plant.growth_stage)
                new_reducing_object.rect.y = 0  # Set the initial position at the top
                self.reducing_objects.append(new_reducing_object)

        #draw stage
        plant_text = self.get_font("assets/fontmain.ttf", 24).render(f"Plant Stage: {self.plant.growth_stage}", True, "black")
        self.SCREEN.blit(plant_text, (10, 40))

        #check for changes in growth stage
        new_growth_stage = self.plant.growth_stage

        #change player sprite based on growth stage
        if new_growth_stage == 2 and self.current_player_sprite != self.player_young_plant:
            self.upgrade1_sfx.play() #sfx first upgrade level
            self.current_player_sprite = self.player_young_plant
            self.player_rect = self.current_player_sprite.get_rect(center=self.player_rect.center)
        elif new_growth_stage == 3 and self.current_player_sprite != self.player_almost_mature:
            self.upgrade2_sfx.play() #sfx second/last upgrade level
            self.current_player_sprite = self.player_almost_mature
            self.player_rect = self.current_player_sprite.get_rect(center=self.player_rect.center)

        #check the growth stage and update/draw raindrops and reducing objects accordingly
        #depending on stage, raindrops will begin to move faster based on speed attributes in Raindrop and RO classes
        if self.plant.growth_stage == 1:
            for raindrop in self.raindrops:
                raindrop.update()
                pygame.draw.rect(self.SCREEN, (0, 0, 255), raindrop.rect)
            for reducing_object in self.reducing_objects:
                reducing_object.update()
                pygame.draw.rect(self.SCREEN, (255, 0, 0), reducing_object.rect)

        elif self.plant.growth_stage == 2:
            for raindrop in self.raindrops:
                raindrop.update()
                pygame.draw.rect(self.SCREEN, (0, 0, 255), raindrop.rect)
            for reducing_object in self.reducing_objects:
                reducing_object.update()
                pygame.draw.rect(self.SCREEN, (255, 0, 0), reducing_object.rect)

        elif self.plant.growth_stage == 3 and not self.meter.value >= self.plant.water_capacity:
            for raindrop in self.raindrops:
                raindrop.rect.y += raindrop.speed

            for reducing_object in self.reducing_objects:
                reducing_object.rect.y += reducing_object.speed

            #remove raindrops and reducing objects that are off-screen
            self.raindrops = [raindrop for raindrop in self.raindrops if raindrop.rect.y < HEIGHT]
            self.reducing_objects = [reducing_object for reducing_object in self.reducing_objects if reducing_object.rect.y < HEIGHT]

            #draw raindrops
            for raindrop in self.raindrops:
                pygame.draw.rect(self.SCREEN, (0, 0, 255), raindrop.rect)

            #draw reducing objects
            for reducing_object in self.reducing_objects:
                pygame.draw.rect(self.SCREEN, (255, 0, 0), reducing_object.rect)

        elif self.plant.growth_stage == 3 and self.meter.value >= self.plant.water_capacity:
            #if playere has reached stage 3 and satisfied the plant's water capacity requirement, player wins
            pygame.mixer.music.fadeout(1500)
            return 'player_win'  #player wins stage
        
        self.timer -= elapsed_time
        if self.timer <= 0 and self.plant.growth_stage <= 3:
            #handle game-over condition when the timer reaches zero and the plant is not fully grown
            pygame.mixer.music.fadeout(1500)
            return 'game_over'#game over stage
        
        #draw the updated timer
        timer_text = self.get_font("assets/fontmain.ttf", 24).render(f"Time: {int(self.timer)}", True, "black")
        self.SCREEN.blit(timer_text, (10, 70))
        pygame.display.flip()
        self.clock.tick(FPS)

    def draw(self, SCREEN):
        pygame.display.flip()

class GameOverScene(Scene):
    #if player runs out of time then they lose the game, but have the option to return to the main menu or quit
    def __init__(self, SCREEN):
        super().__init__(SCREEN)
        self.font = pygame.font.Font("assets/fontmain.ttf", 36)
        self.menu_button_sfx = pygame.mixer.Sound("assets/sfx_correct.mp3")

        #initialize buttons
        self.quit_button = Button(image=None, pos=(640, 500), text_input="quit",
                                  font=self.get_font("assets/fontmain.ttf", 24),
                                  base_color="white", hovering_color="Yellow")

        self.return_to_menu_button = Button(image=None, pos=(640, 300),
                                            text_input="return to menu",
                                            font=self.get_font("assets/fontmain.ttf", 24),
                                            base_color="white", hovering_color="Yellow")

    def update(self):
        MOUSE_POS = pygame.mouse.get_pos()

        self.bg_end = pygame.image.load("assets/img_season_template.png")
        self.bg_rect = self.bg_end.get_rect()
        #coords used to center image
        x = (WIDTH - self.bg_rect.width) // 2
        y = (HEIGHT - self.bg_rect.height) // 2
        
        self.SCREEN.fill("black")
        self.SCREEN.blit(self.bg_end, (x,y))

        MENU_BUTTON_SFX = pygame.mixer.Sound("assets/sfx_correct.mp3")
        MENU_FONT = "assets/fontmain.ttf"

        WIN_TEXT = self.get_font(MENU_FONT, 70).render("GAME OVER", True, "white")
        WIN_RECT = WIN_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))

        #menu and quit buttons
        MENU_BUTTON = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 + 50),
                             text_input="return to menu", font=self.get_font("assets/fontmain.ttf", 40),
                             base_color="white", hovering_color="Yellow")
        QUIT_BUTTON = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 + 200),
                             text_input="quit", font=self.get_font("assets/fontmain.ttf", 40),
                             base_color="white", hovering_color="yellow")
     

        self.SCREEN.blit(WIN_TEXT, WIN_RECT)

        for button in [MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(self.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MOUSE_POS):
                    MENU_BUTTON_SFX.play()
                    return 'main_menu' #return to main menu
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit() #exit game

        return None  #no transition needed

    def draw(self, SCREEN):
        pygame.display.update()

class PlayerWinScene(Scene):
    """very similar to game over screen, if player wins, they move to this stage with a special screen, but still
    have the option to return to main menu or quit the game"""
    def __init__(self, SCREEN):
        super().__init__(SCREEN)
        self.font = pygame.font.Font("assets/fontmain.ttf", 36)
        self.menu_button_sfx = pygame.mixer.Sound("assets/sfx_correct.mp3")

        #initialize buttons with dummy values
        self.quit_button = Button(image=None, pos=(640, 500), text_input="quit",
                                  font=self.get_font("assets/fontmain.ttf", 24),
                                  base_color="white", hovering_color="Yellow")

        self.return_to_menu_button = Button(image=None, pos=(640, 380),
                                            text_input="return to menu",
                                            font=self.get_font("assets/fontmain.ttf", 24),
                                            base_color="white", hovering_color="Yellow")

    def update(self):
        MOUSE_POS = pygame.mouse.get_pos()

        self.tomato_img = pygame.image.load("assets/img_tomato_plant4.png")
        self.bg_end = pygame.image.load("assets/img_season_template.png")
        self.bg_rect = self.bg_end.get_rect()

        #coords for image
        x = (WIDTH - self.bg_rect.width) // 2
        y = (HEIGHT - self.bg_rect.height) // 2
        
        self.SCREEN.fill("black")
        self.SCREEN.blit(self.bg_end, (x,y))
        self.SCREEN.blit(self.tomato_img, (500, 150)) #tomatoes grown by player in custom win screen

        MENU_BUTTON_SFX = pygame.mixer.Sound("assets/sfx_correct.mp3")
        MENU_FONT = "assets/fontmain.ttf"

        WIN_TEXT = self.get_font(MENU_FONT, 70).render("YOU WIN", True, "white")
        WIN_RECT = WIN_TEXT.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))

        #buttons for main menu and quit
        MENU_BUTTON = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 + 50),
                             text_input="return to menu", font=self.get_font("assets/fontmain.ttf", 40),
                             base_color="white", hovering_color="Yellow")
        QUIT_BUTTON = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 + 200),
                             text_input="quit", font=self.get_font("assets/fontmain.ttf", 40),
                             base_color="white", hovering_color="yellow")
     

        self.SCREEN.blit(WIN_TEXT, WIN_RECT)

        for button in [MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(MOUSE_POS)
            button.update(self.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MENU_BUTTON.checkForInput(MOUSE_POS):
                    MENU_BUTTON_SFX.play()
                    return 'main_menu'
                if QUIT_BUTTON.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        return None  # If no transition is needed

    def draw(self, SCREEN):
        pygame.display.update()