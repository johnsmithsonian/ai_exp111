class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def print_board(self):
        print("\n".join(['|'.join(self.board[i*3:(i+1)*3]) for i in range(3)]), end="\n\n")

    def is_winner(self, player):
        return any(all(self.board[i] == player for i in condition) for condition in [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
        ])

    def is_full(self):
        return ' ' not in self.board

    def minimax(self, is_maximizing):
        if self.is_winner('O'): return 1
        if self.is_winner('X'): return -1
        if self.is_full(): return 0

        best_score = float('-inf') if is_maximizing else float('inf')
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O' if is_maximizing else 'X'
                score = self.minimax(not is_maximizing)
                self.board[i] = ' '
                best_score = max(score, best_score) if is_maximizing else min(score, best_score)
        return best_score

    def best_move(self):
        return max((i for i in range(9) if self.board[i] == ' '), 
                   key=lambda i: self.minimax(False))

    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'X':
                move = int(input("Enter your move (0-8): "))
                if self.board[move] == ' ':
                    self.board[move] = self.current_player
                else:
                    print("Invalid move! Try again.")
                    continue
            else:
                self.board[self.best_move()] = 'O'

            if self.is_winner(self.current_player):
                self.print_board()
                print(f"{self.current_player} wins!")
                break
            if self.is_full():
                self.print_board()
                print("It's a draw!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    TicTacToe().play()