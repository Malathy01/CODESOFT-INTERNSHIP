board = [" " for _ in range(9)]

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def available_moves():
    return [i for i in range(9) if board[i] == " "]

def ai_move():
    # Try to win
    for move in available_moves():
        board[move] = "O"
        if check_winner("O"):
            board[move] = " "
            return move
        board[move] = " "

    # Block player win
    for move in available_moves():
        board[move] = "X"
        if check_winner("X"):
            board[move] = " "
            return move
        board[move] = " "

    # Take center
    if 4 in available_moves():
        return 4

    # Take any corner
    for move in [0,2,6,8]:
        if move in available_moves():
            return move

    # Otherwise random
    return available_moves()[0]

print("🎮 TIC-TAC-TOE: You (X) vs AI (O)")

while True:
    display_board()

    move = int(input("Choose your position (0-8): "))
    if board[move] != " ":
        print("Invalid move. Try again.")
        continue

    board[move] = "X"

    if check_winner("X"):
        display_board()
        print("🎉 You win!")
        break

    if not available_moves():
        display_board()
        print("🤝 It's a draw!")
        break

    ai = ai_move()
    board[ai] = "O"

    if check_winner("O"):
        display_board()
        print("🤖 AI wins!")
        break
