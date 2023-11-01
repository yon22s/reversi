import reversiBot


# A function to return your next move.
# 'board' is a 8x8 int array, with 0 being an empty cell and 1,2 being you and the opponent,
# determained by the input 'me'.
def get_move(me: int, board: "list[list[int]]"):
    board = reversiBot.Board(board, len(board))
    return board.get_valid_moves(me)[0]
