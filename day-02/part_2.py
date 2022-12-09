lines = open("input.txt", "r")

you_map = { "A": "R", "B": "P", "C": "S" }
me_map = { "X": "R", "Y": "P", "Z": "S" }

move_val = { "R": 1, "P": 2, "S":3 }

wins = [("R","S"), ("S", "P"), ("P", "R")]

def score(me, you):
    if me == you:
        return 3 + move_val[me]
    
    if (me, you) in wins:
        return 6 + move_val[me]

    return move_val[me]

points = 0

for line in lines:
    you_, result = line.replace("\n","").split(" ")
    you = you_map[you_]

    print(line)
    if result == "Y":
        me = you
    else:
        for win in wins:
            if result == "X":
                a,b = win # if it's to be a loss, we'll do the losing move
            else:
                b,a = win # otherwise, we need the winning move
            print("\t", a, b)
            if you == a:
                me = b
                break

    new_points = score(me, you)
    
    print(me, you, result, new_points)
    points += new_points

print(points)
