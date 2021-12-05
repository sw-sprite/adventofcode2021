import math

with open("input.txt") as f:
    lines = f.read()

# cleans up input, num_drawn is the number called
# bingo_cards is the bingo board in 2d array
lines = lines.split("\n\n")
num_drawn = lines[0].split(",")
num_drawn = [int(i) for i in num_drawn]
bingo_cards = lines[1:]
bingo_cards = [x.split() for x in bingo_cards]
bingo_cards = [list( map(int,i) ) for i in bingo_cards]
bingo_check = bingo_cards

# print(bingo_check)
# print(num_drawn)
# for i in num_drawn:
#     print(i)
# print(bingo_cards[0])
# write functions to check for win and calculate score when won

# update bingo card at index using number
def update_bingo(num, index):
    for i in range(len(bingo_cards[index])):
        if bingo_cards[index][i] == num:
            bingo_check[index][i] = 'x'
    # print(bingo_check)

# check num check for this number at the bingo card at index  
def check_win(num, index):
    col_win = [True] * 5
    row_win = [True] * 5
    for x in range(len(bingo_check[index])):
        # print(x)
        if bingo_check[index][x] != 'x':
            col_win[x%5] = False
            row_win[x//5] = False

    have_bingo = False
    best_score = 0
    for i in range(len(col_win)):
        if col_win[i] == True:
            have_bingo = True
            score = get_col_score(index, num)
            # print(type(score), type(best_score))
            best_score = max(score, best_score)
        elif row_win[i] == True:
            have_bingo = True
            score = get_row_score(index, num)
            # print(type(score), type(best_score))
            best_score = max(score, best_score)
    return have_bingo, best_score

def get_row_score(arr_index, num):
    sum = 0
    for i in range(len(bingo_cards[arr_index])):
        if bingo_check[index][i] == 'x': continue
        sum += int(bingo_cards[arr_index][i])
    return int(sum * num)

def get_col_score(arr_index, num):
    sum = 0
    for i in range(len(bingo_cards[arr_index])):
        if bingo_check[index][i] == 'x': continue
        sum += int(bingo_cards[arr_index][i])
    return int(sum * num)



# quick unit test
# print(get_row_score(0, bingo_cards[0]))

# ans for pt1
last_score = -1
for i in num_drawn:
    # print("drawn: ", i)
    for index in range(len(bingo_cards)):
        # print(i, index)
        update_bingo(i, index)
        win, score = check_win(i, index)
        # print(win, score)
        if win:
            print(score)
            exit()

# print(bingo_check)