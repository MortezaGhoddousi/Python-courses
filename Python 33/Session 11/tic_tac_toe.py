import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("420x520")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False

        self.status = tk.Label(
            root,
            text="Player X's Turn",
            font=("Arial", 18, "bold"),
            pady=15
        )
        self.status.pack()

        self.board_frame = tk.Frame(root)
        self.board_frame.pack()

        self.buttons = []

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Arial", 28, "bold"),
                    width=5,
                    height=2,
                    command=lambda index=row * 3 + col: self.make_move(index)
                )
                button.grid(row=row, column=col, padx=5, pady=5)
                self.buttons.append(button)

        self.reset_button = tk.Button(
            root,
            text="New Game",
            font=("Arial", 16, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.reset_game
        )
        self.reset_button.pack(pady=20)

    def make_move(self, index):
        if self.game_over:
            return

        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index]["text"] = self.current_player

            if self.current_player == "X":
                self.buttons[index]["fg"] = "blue"
            else:
                self.buttons[index]["fg"] = "red"

            if self.check_winner():
                self.status.config(text=f"Player {self.current_player} Wins!")
                messagebox.showinfo(
                    "Game Over",
                    f"Player {self.current_player} wins!"
                )
                self.game_over = True
                return

            if "" not in self.board:
                self.status.config(text="It's a Draw!")
                messagebox.showinfo(
                    "Game Over",
                    "The game is a draw!"
                )
                self.game_over = True
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.status.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if (
                self.board[a] == self.board[b] ==
                self.board[c] != ""
            ):
                self.buttons[a].config(bg="lightgreen")
                self.buttons[b].config(bg="lightgreen")
                self.buttons[c].config(bg="lightgreen")
                return True

        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False

        self.status.config(text="Player X's Turn")

        for button in self.buttons:
            button.config(
                text="",
                bg="SystemButtonFace",
                fg="black"
            )


def main():
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()