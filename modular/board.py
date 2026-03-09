
from utils import Color

class Board:
    def __init__(self):
        # 9 cells, empty cells store numbers as string for placeholders
        self.cells = [str(i+1) for i in range(9)]
        self.winning_positions = []

    def display(self):
        # Draw single board
        print("\n")
        for i in range(3):
            row = ""
            for j in range(3):
                idx = i*3 + j
                cell = self.cells[idx]
                if idx in self.winning_positions:
                    row += f"{Color.GREEN}{cell}{Color.RESET}"
                else:
                    row += f"{cell}"
                if j < 2:
                    row += " | "
            print(" " + row)
            if i < 2:
                print("---+---+---")
        print("\n")

    def update_cell(self, pos, player):
        if self.cells[pos] not in ["X", "O"]:
            self.cells[pos] = player
            return True
        return False

    def is_full(self):
        return all(c in ["X", "O"] for c in self.cells)

    def check_winner(self):
        combos = [
            [0,1,2],[3,4,5],[6,7,8],  # rows
            [0,3,6],[1,4,7],[2,5,8],  # cols
            [0,4,8],[2,4,6]           # diagonals
        ]
        for combo in combos:
            a,b,c = combo
            if self.cells[a]==self.cells[b]==self.cells[c] and self.cells[a] in ["X","O"]:
                self.winning_positions = combo
                return self.cells[a]  # winner
        self.winning_positions = []
        return None
