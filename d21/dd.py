a = 4
b = 2
d = 1
won = False
count = 0

print(23%10)

def roll():
    global d
    d += 1
    return d

class Player():
    def __init__(self, starting, score):
        self.pos = starting
        self.score = score

    def take_turn(self, dice):
        global count
        tmp = 0
        # print("dice is: ", dice)
        # print("pos is:", self.pos)
        for i in range(3):
            tmp += dice + i
            count += 1
        print("TMP is: ", tmp)

        self.pos = (self.pos + tmp) % 10

        if self.pos == 0:
            self.pos = 10

        self.score += self.pos
        dice += 3
        # print("dice is: ", dice)
        # print("pos is:", self.pos)
        # print("score is:", self.score)
        # exit()
        if self.score >= 1000:
            return True, dice
        else:
            return False, dice

p1 = Player(a, 0)
p2 = Player(b, 0)

while not won:
# for i in range(3):
    # print("----------------------")
    # print("p1 turn:")
    won, d = p1.take_turn(d)
    
    if won:
        print(p2.score * count)
        break

    # print("----------------------")
    # print("p2 turn:")
    won, d = p2.take_turn(d)
    
    if won:
        print(p1.score * count)
        break

