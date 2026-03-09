
import random
from utils import Color, delay

def get_human_input(board, player):
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
    # Smart AI: win if possible, block if needed, else pick center/side/corner
    delay(0.5)
    empty = [i for i, c in enumerate(board.cells) if c not in ["X","O"]]
    # Try to win
    for move in empty:
        board.cells[move] = "O"
        if board.check_winner() == "O":
            print(f"{Color.YELLOW}AI placed O in position {move+1}{Color.RESET}")
            return
        board.cells[move] = str(move+1)
    # Block opponent
    for move in empty:
        board.cells[move] = "X"
        if board.check_winner() == "X":
            board.cells[move] = "O"
            print(f"{Color.YELLOW}AI placed O in position {move+1}{Color.RESET}")
            return
        board.cells[move] = str(move+1)
    # Pick center
    if 4 in empty:
        board.update_cell(4,"O")
        print(f"{Color.YELLOW}AI placed O in position 5{Color.RESET}")
        return
    # Pick random
    move = random.choice(empty)
    board.update_cell(move,"O")
    print(f"{Color.YELLOW}AI placed O in position {move+1}{Color.RESET}")
    delay(0.7)
