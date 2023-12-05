"""Testing used for StartGameScene including mouse position and correct sfx is played when clicked
2 positive tests and 1 negative test"""

import pygame
import pytest
from scenes import StartGameScene
import sprites

#fixture to create an instance of the StartGameScene stage of the game
@pytest.fixture
def start_game_scene():
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    return StartGameScene(SCREEN)

def test_start_game_scene_initial_state(start_game_scene):
    """testing the scene's initial state"""
    assert start_game_scene.scene_state == "start_game_rules"
    assert start_game_scene.bg_color == (0, 0, 0, 128)
    assert start_game_scene.display_text_timer == 0
    assert start_game_scene.display_text_duration == 3000

def test_start_game_scene_update_select_state(start_game_scene, mocker):
    """testing StartGameScene's tests the transition of the first scene 'game_start_rules' to the next scene 'select' """
    #positive test
    mocker.patch("pygame.mouse.get_pos", return_value=(0, 0))  #mock mouse position
    mocker.patch("pygame.event.get", return_value=[pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1)])
    mocker.patch("pygame.time.delay")

    start_game_scene.update()

    #assetions to test mouse positions and stage selection
    assert start_game_scene.scene_state == "select"

def test_start_game_scene_update_select_tomato_button(start_game_scene, mocker):
    """testing sfx when player selects the tomato and its transition to the next stage"""
    #positive test
    mocker.patch("pygame.mouse.get_pos", return_value=(300, 100))  #mock mouse position
    mocker.patch("pygame.event.get", return_value=[pygame.event.Event(pygame.MOUSEBUTTONDOWN)])
    mocker.patch("pygame.mixer.Sound.play")
    mocker.patch("pygame.mixer.music.stop")
    mocker.patch("pygame.time.delay")

    next_scene = start_game_scene.update()

    assert next_scene == 'water_game'

def test_start_game_scene_update_select_carrot_button(start_game_scene, mocker):
    """tests sfx when carrot is selected"""
    #negative test
    mocker.patch("pygame.mouse.get_pos", return_value=(150, 100))
    mocker.patch("pygame.event.get", return_value=[pygame.event.Event(pygame.MOUSEBUTTONDOWN)])
    mocker.patch("pygame.mixer.Sound.play")
    mocker.patch("pygame.time.delay")
    mocker.patch.object(start_game_scene, "display_text")

    next_scene = start_game_scene.update()

    assert next_scene is None #asserts scene returned after clicking the carrot button is None

    start_game_scene.display_text.assert_called_once_with("Cannot be grown in this season.", 2, 200 + sprites.carrot_image.get_width()/2,
                                                          123 + sprites.carrot_image.get_height()/2)
