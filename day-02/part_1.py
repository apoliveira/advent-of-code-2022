lines = open("input.txt", "r")

you_map = { "A": "R", "B": "P", "C": "S" }
me_map = { "X": "R", "Y": "P", "Z": "S" }

move_val = { "R": 1, "P": 2, "S":3 }

wins = [("R","S"), ("S", "P"), ("P", "R")]

def score(me_, you_):
    me = me_map[me_]
    you = you_map[you_]

    if me == you:
        return 3 + move_val[me]
    
    if (me, you) in wins:
        return 6 + move_val[me]

    return move_val[me]

points = 0

for line in lines:
    you, me = line.replace("\n","").split(" ")
    points += score(me, you)

print(points)
