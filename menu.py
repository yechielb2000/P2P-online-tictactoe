import game



if __name__ == "__main__":
    game = Game()

    action = ""
    while action != "1" and action != "2":
        action = input("1 to join a game 2 to create new one : ")

    if int(action) == 1:
        game.connect_to_game("localhost", 9999)
    else:
        game.host_game("localhost", 9999)    