
import os
import random
import time

# Colors
class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BRIGHT = "\033[1m"
    RESET = "\033[0m"

def clear_screen():
    print("\033[H\033[J", end="")  # Clear terminal

class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def draw_board(self):
        clear_screen()
        print("Tic-Tac-Toe\n")
        for i in range(3):
            row = " │ ".join(self.cells[i*3:(i+1)*3])
            print(f" {row} ")
            if i < 2:
                print("---+---+---")
        print()

    def update_cell(self, index, player):
        if self.cells[index] == " ":
            self.cells[index] = player
            return True
        return False

    def is_full(self):
        return all(cell != " " for cell in self.cells)

    def check_winner(self):
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in combos:
            if self.cells[a] == self.cells[b] == self.cells[c] != " ":
                return self.cells[a], (a,b,c)
        return None, None

def get_player_input(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if 0 <= move <= 8:
                if board.update_cell(move, player):
                    return
                else:
                    print(f"{Color.RED}Cell occupied! Try again.{Color.RESET}")
            else:
                print(f"{Color.RED}Invalid input! Must be 1-9.{Color.RESET}")
        except ValueError:
            print(f"{Color.RED}Enter a number!{Color.RESET}")

def ai_move(board):
    empty = [i for i, c in enumerate(board.cells) if c == " "]
    time.sleep(0.5)
    move = random.choice(empty)
    board.update_cell(move, "O")
    print(f"{Color.YELLOW}AI placed O in position {move+1}{Color.RESET}")
    time.sleep(0.7)

def main():
    print(f"{Color.BRIGHT}Welcome to Tic-Tac-Toe!{Color.RESET}")
    mode = input("Select mode: 1) Single Player  2) Two Player: ").strip()
    scores = {"X":0,"O":0}

    while True:
        board = Board()
        winner = None
        board.draw_board()

        while not winner and not board.is_full():
            # Player X move
            get_player_input(board, "X")
            board.draw_board()
            winner, _ = board.check_winner()
            if winner or board.is_full():
                break

            # AI or Player O
            if mode == "1":
                ai_move(board)
            else:
                get_player_input(board, "O")

            board.draw_board()
            winner, _ = board.check_winner()

        if winner:
            print(f"{Color.GREEN}🎉 Player {winner} wins!{Color.RESET}")
            scores[winner] += 1
        else:
            print(f"{Color.YELLOW}It's a tie!{Color.RESET}")

        print(f"Scores => X: {scores['X']}  O: {scores['O']}")
        if input("Play again? (y/n): ").lower() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
