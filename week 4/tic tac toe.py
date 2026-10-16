class TicTacToe:
    def __init__(self):
        self.__board = [' ' for _ in range(9)]

    def __minimax(self, is_maximising):
        """Minimax algorithm to evaluate the best move."""
        if self.__is_winner('O'): return -1  # Computer wins, return -1
        if self.__is_winner('X'): return 1   # Human wins, return +1
        if ' ' not in self.__board: return 0  # Draw, return 0

        if is_maximising:  # Human (X) is maximising
            best_score = float('-inf')
            for i in range(9):
                if self.__board[i] == ' ':
                    self.__board[i] = 'X'
                    score = self.__minimax(False)
                    self.__board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:  # Computer (O) is minimising
            best_score = float('inf')
            for i in range(9):
                if self.__board[i] == ' ':
                    self.__board[i] = 'O'
                    score = self.__minimax(True)
                    self.__board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def __is_game_end(self, player):
        if self.__is_winner(player):
            self.__display_board()
            print(f"{'You' if player == 'X' else 'I'} win!")
            return True

        if self.__is_draw():
            self.__display_board()
            print("It's a draw!")
            return True

        return False

    def __computer_move(self):
        """Make a move for the computer using the minimax algorithm."""
        best_score = float('inf')  # The computer (O) minimises
        best_move = None

        for cell in range(len(self.__board)):
            if self.__board[cell] == ' ':
                self.__board[cell] = 'O'
                score = self.__minimax(True)  # Pass True to let the human (X) maximise
                self.__board[cell] = ' '

                if score < best_score:  # Minimising: look for the lowest score
                    best_score = score
                    best_move = cell

        if best_move is not None:
            self.__board[best_move] = 'O'

    def __display_board(self):
        print("Current Board:\n")
        for row in range(3):
            print(" | ".join(self.__board[row*3:(row+1)*3]))
            if row < 2:
                print("---------")
        print()

    def __is_draw(self):
        return ' ' not in self.__board

    def __is_winner(self, player):
        """Check if the given player has won the game."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        return any(all(self.__board[cell] == player for cell in condition) for condition in win_conditions)

    def __player_move(self):
        position = int(input("Enter your move (0-8): "))

        while position < 0 or position > 8:
            print("Invalid position. Please try again.")
            position = int(input("Enter your move (0-8): "))

        while self.__board[position] != ' ':
            print("Position already taken. Try another.")
            position = int(input("Enter your move (0-8): "))

        self.__board[position] = 'X'

    def run(self):
        print("Welcome to Tic-Tac-Toe.\nYou are player X. I am player O.\n")
        while True:
            self.__display_board()
            self.__player_move()
            if self.__is_game_end('X'): break
            self.__computer_move()
            if self.__is_game_end('O'): break


# Example usage:
if __name__ == "__main__":
    game = TicTacToe()
    game.run()


