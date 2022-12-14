import itertools

lines = open("input.txt", "r").read().split("\n")

points = 0

def get_common_letter(first_half, second_half):
    for l in second_half:
        if l in first_half:
            return  l

def letter_points(l):
    if l < "a":
        return ord(l) - ord("A") + 26 + 1 # Uppercase letters are 27-52
    return ord(l) - ord("a") + 1

def grouper(xs, n):
    return [ xs[i:i+n] for i in range(0, len( xs ), n)]

for group in grouper(lines, 3):
    if len(group) < 3:
        break

    common_letter = ( set(group[0]) & set(group[1]) & set(group[2]) ).pop()

    point = letter_points(common_letter)
    
    points += point

print(points)
