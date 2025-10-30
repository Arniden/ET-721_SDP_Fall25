class Connect4:
    def __init__(self, rows=6, cols=7, player_symbols=('X', 'O'), starting_player='O', color_output=True):
        # Basic validation
        if not isinstance(rows, int) or not isinstance(cols, int) or rows < 4 or cols < 4:
            raise ValueError("rows and cols must be integers >= 4")
        if not isinstance(player_symbols, (tuple, list)) or len(player_symbols) != 2:
            raise ValueError("player_symbols must be a tuple/list of two distinct strings/characters")
        if player_symbols[0] == player_symbols[1]:
            raise ValueError("player_symbols must be distinct")
        if starting_player not in player_symbols:
            raise ValueError("starting_player must be one of player_symbols")

        # Store settings at instance level (so different games can have different sizes)
        self.ROWS = rows
        self.COLS = cols
        self.players = (str(player_symbols[0]), str(player_symbols[1]))
        self.current_player = starting_player
        self.color_output = bool(color_output)

        # Initialize board (list of lists filled with spaces)
        self.board = [[' ' for _ in range(self.COLS)] for _ in range(self.ROWS)]

    def switch_player(self):
        """Toggle current player between the two configured symbols."""
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

    def _colorize(self, ch):
        """Return colorized character if enabled and matches players; else return as-is."""
        if not self.color_output:
            return ch
        if ch == self.players[0]:
            # Red-ish for first player
            return '\033[91m' + ch + '\033[0m'
        if ch == self.players[1]:
            # Blue-ish for second player
            return '\033[94m' + ch + '\033[0m'
        return ch

    def print_board(self):
        """Pretty-print the board to the console."""
        print("\nCurrent Board:")
        for row in self.board:
            print('|', end='')
            for cell in row:
                to_print = ' ' if cell == ' ' else self._colorize(cell)
                print(f"{to_print}", end='|')
            print()
        # Footer / coordinates
        print('-' * (self.COLS * 2 + 1))
        # 1-based column indices
        print(' ' + ' '.join(str(i) for i in range(1, self.COLS + 1)))

    def drop_chip(self, column):
        """Drop a chip in the chosen column (1-based). Returns True on success, False otherwise."""
        if not isinstance(column, int) or not (1 <= column <= self.COLS):
            return False

        col_idx = column - 1
        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row][col_idx] == ' ':
                self.board[row][col_idx] = self.current_player
                return True
        return False  # Column full

    def check_win(self, player):
        """Check if a player has 4 in a row (horizontal, vertical, diagonal)."""
        # Horizontal
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                if all(self.board[r][c + i] == player for i in range(4)):
                    return True
        # Vertical
        for r in range(self.ROWS - 3):
            for c in range(self.COLS):
                if all(self.board[r + i][c] == player for i in range(4)):
                    return True
        # Diagonal down-right
        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                if all(self.board[r + i][c + i] == player for i in range(4)):
                    return True
        # Diagonal up-right
        for r in range(3, self.ROWS):
            for c in range(self.COLS - 3):
                if all(self.board[r - i][c + i] == player for i in range(4)):
                    return True
        return False

    def is_full(self):
        """Check if the top row has any empty spaces; if none, the board is full."""
        return all(self.board[0][c] != ' ' for c in range(self.COLS))

    def play_game(self):
        """Interactive game loop (uses input())."""
        print("Welcome to Connect 4!")
        print(f"Board size: {self.ROWS}x{self.COLS}")
        print(f"Players: {self.players[0]} vs {self.players[1]} (starting: {self.current_player})\n")
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn.")
            try:
                column = int(input(f"Enter column (1-{self.COLS}): "))
            except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {self.COLS}.")
                continue

            if not self.drop_chip(column):
                print("Invalid move! Column is full or out of range. Try again.")
                continue

            # Check for win with the player who just moved
            if self.check_win(self.current_player):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_full():
                self.print_board()
                print("It's a tie! No more moves left.")
                break

            self.switch_player()


if __name__ == "__main__":
    Connect4().play_game()

