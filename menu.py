from game import *

game = Game()

action = input("1 to join a game 2 to create new one : ")

if int(action) == 1:
    game.connect_to_game("localhost", 9999)
elif int(action) == 2:
    game.host_game("localhost", 9999)    
else:
    print("Invalid action")