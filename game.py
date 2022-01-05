import socket
import threading 

class Game:

    def __init__(self):
        self.format = "utf-8"

        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.you = "X"
        self.opponent = "O"
        self.winner = None
        self.game_over = False
        self.counter = 0

    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((host, port))
        server.listen(1)

        client, addr = server.accept()

        self.you = "X"
        self.opponent = "O"

        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()

    def connect_to_game(self, host, port):    
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        client.connect((host, port))

        self.you = "O"
        self.opponent = "X"
        threading.Thread(target=self.handle_connection, args=(client,)).start()

    def handle_connection(self, client):
        print("Game is on!")
        while not self.game_over:       
            if self.turn == self.you:
                print("Your turn")
                move = input('Enter your move (row, column):')
                if self.check_valid_move(move.split(',')):
                    self.apply_move(move.split(','), self.you, client)
                    self.turn = self.opponent
                    client.send(move.encode(self.format))
                else:
                    print("Invalid move!")  
            else:
                data = client.recv(1024)
                if not data:
                    break
                else:
                    self.apply_move(data.decode(self.format).split(','), self.opponent, client)  
                    self.turn = self.you

    def apply_move(self, move, player, client):
        if self.game_over:
            return
        self.counter += 1
        self.board[int(move[0])][int(move[1])] = player
        self.print_board()
        if self.check_if_won():
            if self.winner == self.you:
                exit()
            elif self.winner == self.opponent:
                print("You lose!")
                exit()
        else:
            if self.counter == 9:
                print("It's a tie!")
                exit()                                     

    def check_valid_move(self, move):
        return self.board[int(move[0])][int(move[1])] == " "

    def check_if_won(self):
            for row in range(3):
                if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.you: 
                    self.winner = self.you
                    self.game_over = True
                    return True

            for col in range(3):
                if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.you: 
                    self.winner = self.you
                    self.game_over = True
                    return True        

            if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.you:         
                self.winner = self.you
                self.game_over = True
                return True   

            if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.you:         
                self.winner = self.you
                self.game_over = True
                return True        

    def print_board(self):
        for row in range(3):
            print(" | ".join(self.board[row]))
            if row != 2:
                print("----------")            
