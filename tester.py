import reversiBot, basicBot, time

bot1 = basicBot.get_move
bot1_color = 1
bot1_total_time = 0
bot1_total_moves = 0

bot2 = reversiBot.get_move
bot2_color = 2
bot2_total_time = 0
bot2_total_moves = 0


starting_boards = [
    
]

turns = 0
board = reversiBot.Board()

while turns != 60:
    if len(board.get_valid_moves(bot1_color)) != 0:
        t1 = time.perf_counter()
        board.do_move(bot1_color, *bot1(bot1_color, board.lst))
        t2 = time.perf_counter()
        turns += 1
        bot1_total_time += t2 - t1
        bot1_total_moves += 1
    print(board)
    if len(board.get_valid_moves(bot2_color)) != 0:
        t1 = time.perf_counter()
        board.do_move(bot2_color, *bot2(bot2_color, board.lst))
        t2 = time.perf_counter()
        turns += 1
        bot2_total_time += t2 - t1
        bot2_total_moves += 1
    print(board)

print(f"bot1 average time: {round(bot1_total_time / bot1_total_moves, 4)}")
print(f"bot2 average time: {round(bot2_total_time / bot2_total_moves, 4)}")
print(f"score bot1: {board.get_score(bot1_color)}")
print(f"score bot2: {board.get_score(bot2_color)}")
