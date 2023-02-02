print("Welcome to the game of tic-tac-toe or x and o, you know how to play, so go on and have fun!")
print("Just know that the positions to input are of the form: ")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

p1, p2, p3, p4, p5, p6, p7, p8, p9 = " ", " ", " ", " ", " ", " ", " ", " ", " " # p stands for "position", so p1 means
                                                                                # position 1, p2 means position 2 etc.

game_playout = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']  # the letters are placeholders until the real game starts,
            # after which each chronologically will be replaced with a 0 or a 1, 0 representing o and 1 representing x
won = 0
count = 0
x_pos = None
o_pos = None
used_positions = []


def win_check():
    if game_playout[0] == game_playout[1] == game_playout[2]:
        return 1
    elif game_playout[3] == game_playout[4] == game_playout[5]:
        return 1
    elif game_playout[6] == game_playout[7] == game_playout[8]:
        return 1
    elif game_playout[0] == game_playout[3] == game_playout[6]:
        return 1
    elif game_playout[0] == game_playout[4] == game_playout[8]:
        return 1
    elif game_playout[1] == game_playout[4] == game_playout[7]:
        return 1
    elif game_playout[2] == game_playout[5] == game_playout[8]:
        return 1
    elif game_playout[2] == game_playout[4] == game_playout[6]:
        return 1


def layout_changer():
    global p1, p2, p3, p4, p5, p6, p7, p8, p9

    if x_pos == 1:
        p1 = "x"
    elif x_pos == 2:
        p2 = "x"
    elif x_pos == 3:
        p3 = "x"
    elif x_pos == 4:
        p4 = "x"
    elif x_pos == 5:
        p5 = "x"
    elif x_pos == 6:
        p6 = "x"
    elif x_pos == 7:
        p7 = "x"
    elif x_pos == 8:
        p8 = "x"
    elif x_pos == 9:
        p9 = "x"

    if o_pos == 1:
        p1 = "o"
    elif o_pos == 2:
        p2 = "o"
    elif o_pos == 3:
        p3 = "o"
    elif o_pos == 4:
        p4 = "o"
    elif o_pos == 5:
        p5 = "o"
    elif o_pos == 6:
        p6 = "o"
    elif o_pos == 7:
        p7 = "o"
    elif o_pos == 8:
        p8 = "o"
    elif o_pos == 9:
        p9 = "o"


while won != 1:

    x_pos = input("Choose your position to place x (1 to 9) ")
    while not x_pos.isnumeric():
        print("Error! Looks like you've haven't entered a number, please try again!")
        x_pos = input("Choose your position to place x (1 to 9) ")
    x_pos = int(x_pos)
    while x_pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or x_pos in used_positions:
        print(f"| {p1} | {p2} | {p3} |")
        print(f"| {p4} | {p5} | {p6} |")
        print(f"| {p7} | {p8} | {p9} |")
        print("Invalid position! Please try another value:")
        x_pos = int(input("Choose your position to place x (1 to 9) "))

    used_positions.append(x_pos)
    count += 1
    game_playout.pop(x_pos - 1)
    game_playout.insert(x_pos - 1,
                        1)  # We replace the (x_pos-1)th index element in game_playout with 1,where 1 indicates an 'x'
    layout_changer()
    print(f"| {p1} | {p2} | {p3} |")
    print(f"| {p4} | {p5} | {p6} |")
    print(f"| {p7} | {p8} | {p9} |")

    won = win_check()
    if won == 1:
        print("x has won! Congratulations!")
        print()
        print("Thank you for playing the game! Hope you enjoyed!")
        quit()
    elif count >= 9:
        print()
        print("Draw!")
        print("Thank you for playing the game! Hope you enjoyed!")
        quit()

    o_pos = input("Choose your position to place o (1 to 9) ")
    while not o_pos.isnumeric():
        print("Error! Looks like you've haven't entered a number, please try again!")
        o_pos = input("Choose your position to place o (1 to 9) ")
    o_pos = int(o_pos)
    while o_pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or o_pos in used_positions:
        print(f"| {p1} | {p2} | {p3} |")
        print(f"| {p4} | {p5} | {p6} |")
        print(f"| {p7} | {p8} | {p9} |")
        print("Invalid position! Please try another value:")
        o_pos = int(input("Choose your position to place o (1 to 9) "))

    used_positions.append(o_pos)
    count += 1
    game_playout.pop(o_pos - 1)
    game_playout.insert(o_pos - 1,
                        0)  # We replace the (o_pos-1)th index element in game_playout with 0,where 0 indicates an 'o'
    layout_changer()
    print(f"| {p1} | {p2} | {p3} |")
    print(f"| {p4} | {p5} | {p6} |")
    print(f"| {p7} | {p8} | {p9} |")

    won = win_check()
    if won == 1:
        print("o has won! Congratulations!")
print()
print("Thank you for playing the game! Hope you enjoyed!")
