#!usr/bin/env python3

import game


def main() -> None:
    game = Game()
    connect_to_game()      
    

def connect_to_game() -> None:
    if get_action() == 1:
        game.connect_to_game("localhost", 9999)
    else:
        game.host_game("localhost", 9999)    


def get_action() -> str:
    action = ""
    while action != "1" and action != "2":
        action = input("1 to join a game 2 to create new one : ")
    return int(action)


if __name__ == "__main__":
    main()    