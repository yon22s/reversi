class Board:
    def __init__(self, board: "list[list[int]] | None"=None, size: int=8) -> None:
        if board is None:
            self.lst = [[0 for x in range(8)] for y in range(3)] + [[0, 0, 0, 2, 1, 0, 0, 0]] + [[0, 0, 0, 1, 2, 0, 0, 0]] + [[0 for x in range(8)] for y in range(3)]
        else:
            self.lst = board
        self.board_size = size

    def __getitem__(self, item) -> "list[int]":
        return self.lst[item]
        

    def __repr__(self) -> str:
        ret = ""
        for n in range(self.board_size):
            ret += str(self.lst[n]) + "\n"
        return ret


    def __str__(self) -> str:
        ret = ""
        for n in range(self.board_size):
            ret += str(self.lst[n]) + "\n"
        return ret

    
    def copy(self):
        return Board(self.board_size, list(map(list.copy, self.lst)))

    
    def inBoard(self, i, j) -> bool:
        return self.board_size > i >= 0 and self.board_size > j >= 0


    def get_score(self, me: int) -> int:
        score = 0

        for i in range(self.board_size):
            for j in range(self.board_size):
                value = self[i][j]
                if value != 0:
                    if value == me:
                        score += 1
                    else:
                        score -= 1

        return score

    def get_rating(self, me: int, depth: int) -> float:
        if depth == 0:
            # base evaluation
            # TODO: improve
            return self.get_score()

        enemy = 3 - me

        max_eval = float("-inf")

        for i, j in self.get_valid_moves(me):
            new_board = self.copy()
            new_board.do_move(me, i, j)
            current_eval = -new_board.get_rating(enemy, depth - 1)

            if current_eval > max_eval:
                max_eval = current_eval

        return max_eval

    def is_valid(self, me: int, i: int, j: int) -> bool:
        if self[i][j] != 0:
            return False
        # check every direction
        enemy = 3 - me
        for di in range(-1, 2):
            for dj in range(-1, 2):
                current_j = j + dj
                current_i = i + di

                if not self.inBoard(current_i, current_j) or self[current_i][current_j] != enemy:
                    continue
                if not (di == 0 == dj):
                    while self.inBoard(current_i, current_j) and self[current_i][current_j] == enemy:
                        current_j += dj
                        current_i += di
                
                if not self.inBoard(current_i, current_j) or self[current_i][current_j] != me:
                    continue
                
                return True
        
        return False
        

    def get_valid_moves(self, me: int) -> "list[tuple[int, int]]":
        moves = []
        
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.is_valid(me, i, j):
                    moves.append((i, j))
        
        return moves

    def do_move(self, me: int, i: int, j: int) -> None:
        enemy = 3 - me
        self.lst[i][j] = me
        for di in range(-1, 2):
            for dj in range(-1, 2):
                line = []
                current_j = j
                current_i = i
                
                current_j += dj
                current_i += di
                if not self.inBoard(current_i, current_j) or self[current_i][current_j] != enemy:
                    continue

                while self.inBoard(current_i, current_j) and self[current_i][current_j] == enemy:
                    line.append([current_i,current_j])
                    current_j += dj
                    current_i += di
                
                if not self.inBoard(current_i, current_j) or self[current_i][current_j] != me:
                    continue
                
                for tile in line:
                    self[tile[0]][tile[1]] = me

        





# A function to return your next move.
# 'board' is a 8x8 int array, with 0 being an empty cell and 1,2 being you and the opponent,
# determained by the input 'me'.
def get_move(me: int, board: "list[list[int]] | Board"):
    
    if isinstance(board, list):
        board = Board(board, len(board))
    dir1 = {}
    max = float("-inf")
    valid_moves = board.get_valid_moves(me)
    ret = valid_moves[0][0], valid_moves[0][1]
    
    for move in valid_moves:
        rate = board.rate_move(move[0], move[1], me)
        dir1[move] = rate
                
    for key in dir1.keys():
        if dir1[key] > max:
            max = dir1[key]
            ret = key

    
    # if there is no valid move, the bot will never be called in the first place. For safety, we return an invalid result.
    return ret
