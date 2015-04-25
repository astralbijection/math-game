import json
import random
import sys
import time

import pygame

import assets
import colors
import enemy
import title


_cameras = pygame.camera.list_cameras()
cam = pygame.camera.Camera(_cameras[0], (640, 480), 'RGB')
cam.start()

def init():
    highscores = None
    try:
        highscorefile = open('highscores.json', 'r')
        highscorefile.close()
    except FileNotFoundError:
        highscorefile = open('highscores.json', 'w+')
        defaultscorefile = open('assets/data/defaultscores.json', 'r')
        highscorefile.write(defaultscorefile.read())
        highscorefile.close()
        defaultscorefile.close()
    with open('highscores.json', 'r') as file:
        txt = file.read()
        highscores = json.loads(txt)
    pygame.init()
    pygame.display.set_caption("Math Game")
    display = pygame.display.set_mode((1280, 1024), pygame.FULLSCREEN)
    return display

def bust():
    img = cam.get_image()
    pygame.image.save(img, 'he-who-alt-f4s.png')

def terminate():
    bust()
    cam.stop()
    pygame.quit()
    sys.exit()

def main():
    d = init()
    title.startscreen(d)

if __name__ == '__main__':
    main()
