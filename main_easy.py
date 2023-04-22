import keyboard
import time
import os
from random import randint

SIZE_GAME_SPACE = 20

game_space = []
for _ in range(SIZE_GAME_SPACE):
    game_space.append([' ' for _ in range(SIZE_GAME_SPACE)])

vector = 's'
apple_x, apple_y = randint(0, SIZE_GAME_SPACE - 1), randint(0, SIZE_GAME_SPACE - 1)

while True:
    pass

    time.sleep(0.3)
    os.system('cls')
