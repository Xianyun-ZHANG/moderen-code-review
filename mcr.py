def check_winner(board, mark):
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if all([cell == mark for cell in board[i]]):  # Rows
            return True
        if all([board[j][i] == mark for j in range(3)]):  # Columns
            return True
    # Diagonals
    if all([board[i][i] == mark for i in range(3)]) or \
       all([board[i][2-i] == mark for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def get_valid_move(board):
    while True:
        try:
            move = tuple(map(int, input("Enter move (row column): ").split()))
            if len(move) == 2 and all(0 <= m < 3 for m in move) and board[move[0]][move[1]] == ' ':
                return move
        except ValueError:
            pass
        print("Invalid move. Try again.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        display_board(board)
        print(f"Player {current_player}'s turn.")
        row, col = get_valid_move(board)
        board[row][col] = current_player
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()


