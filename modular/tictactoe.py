
from board import Board
from player import get_human_input, ai_move
from utils import Color, delay, clear_screen

def choose_mode():
    print(f"{Color.CYAN}Choose Game Mode:{Color.RESET}")
    print("1. Human vs AI")
    print("2. Human vs Human")
    while True:
        choice = input("Enter 1 or 2: ")
        if choice in ["1","2"]:
            return choice
        print(f"{Color.RED}Invalid choice!{Color.RESET}")

def play_game(mode="1", scores=None):
    if scores is None:
        scores = {"X":0,"O":0}
    board = Board()
    clear_screen()
    board.display()
    current_turn = "X"

    while True:
        if mode=="1":
            if current_turn=="X":
                get_human_input(board, "X")
            else:
                ai_move(board)
        else:
            get_human_input(board, current_turn)

        clear_screen()
        board.display()

        winner = board.check_winner()
        if winner or board.is_full():
            print("\n")
            if winner:
                print(f"{Color.GREEN}Player {winner} wins!{Color.RESET}")
                scores[winner] += 1
            else:
                print(f"{Color.YELLOW}It's a tie!{Color.RESET}")
            print(f"Score -> X: {scores['X']} | O: {scores['O']}\n")
            break

        current_turn = "O" if current_turn=="X" else "X"

    if input("Play again? (y/n): ").lower()=="y":
        play_game(mode, scores)
    else:
        print("Thanks for playing!")

if __name__=="__main__":
    print(f"{Color.CYAN}Welcome to Tic Tac Toe!{Color.RESET}")
    mode = choose_mode()
    play_game(mode)
