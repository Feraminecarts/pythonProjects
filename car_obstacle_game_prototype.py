import time
import sys
import random
from pynput.keyboard import Controller
from keyboard import *



def sprite_mover(sprite, direction):
    # sys.stdout.flush()
    for i in range(0, len(sprite)):
        if direction == 'd':
            for index in range(len(sprite[i]) - 2, 1, -1):
                sprite[i][index], sprite[i][index - 1] = sprite[i][index - 1], sprite[i][index]
            list_interpreter(sprite[i], i)
        elif direction == 'a':
            for index in range(1, len(sprite[i]) - 2):
                sprite[i][index], sprite[i][index + 1] = sprite[i][index + 1], sprite[i][index]
            list_interpreter(sprite[i], i)
        # else:
        #     list_interpreter(sprite[i], i)

def list_interpreter(list, line_num):
    count = 0
    length = len(list)
    for digit in list:
        if digit == 9 and count == length-1 and line_num == 7:
            print("|", end="")
        elif digit == 9 and count == length-1:
            print("|")
        elif digit == 9:
            print("|", end="")
        elif digit == 1:
            print("x", end="")
        elif digit == 2:
            print("-", end="")
        elif digit == 3:
            print("0", end="")
        elif digit == 0 and count == length-1:
            print(" ")
        elif digit == 0 or (digit == 0 and count == length-1 and line_num == 23):
            print(" ", end="")
        count += 1


keybord = Controller()
time.sleep(1)
for i in 'Welcome to the "car" game! Press "a" to move left and "d" to move right, and press "o" at any time to exit the game. Good Luck!':
    keybord.press(i)
    keybord.release(i)
    time.sleep(0.04)
print()

# one_dim = [9, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 9]
road = [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 2, 1, 1, 1, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [9, 0, 3, 2, 1, 1, 1, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [9, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]]

for num in range(0, len(road)):
    list_interpreter(road[num], num)
while True:
    rand_num = random.randint(0, 1)
    if is_pressed('d'):
        print()
        sprite_mover(road, 'd')
        time.sleep(0.12)
    if is_pressed('a'):
        print()
        sprite_mover(road, 'a')
        time.sleep(0.12)
    if is_pressed('o'):
        print()
        print("Thank you for playing!")
        break


#
# for i in range(0, len(sprite)):
#     touchd = 'no'
#     toucha = 'no'
#     if sprite[3][24] + sprite[3][23] == 12:
#         touchd = 'yes'
#     if sprite[3][0] + sprite[3][1] == 12:
#         toucha = 'yes'
#     if direction == 'd' and touchd == 'no' :
#         for index in range(len(sprite[i]) - 2, 1, -1):
#             sprite[i][index], sprite[i][index - 1] = sprite[i][index - 1], sprite[i][index]
#         list_interpreter(sprite[i], i)
#     elif direction == 'a' and toucha == 'no':
#         for index in range(1, len(sprite[i]) - 2):
#             sprite[i][index], sprite[i][index + 1] = sprite[i][index + 1], sprite[i][index]
#         list_interpreter(sprite[i], i)
#     else:
#         list_interpreter(sprite[i], i)


# import time
# for i in range(0, 100):
#     time.sleep(0.1)
#     print("""             |  xxxxxx
#                0-xxxx-0
#                  xxxx
#              |           x
#                          x           |
#                          .           |
#              |
#              |
#                                      |
#                                      | """)
#     time.sleep(0.1)
#
#     print("""             |
#              |
#                                      |
#                                      |
#              |
#              |   xxxx
#                0-xxxx-0              |
#                 xxxxxx               |
#              | 0-xxxx-0
#                  xxxx                   """)
#
#     time.sleep(0.1)
#
#     print("""             |
#              |           x
#                          x           |
#                          .           |
#              |
#              |   xxxx
#                0-xxxx-0              |
#                 xxxxxx               | """)
#
#
