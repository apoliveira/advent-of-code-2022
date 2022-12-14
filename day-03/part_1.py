lines = open("input.txt", "r")

points = 0

def get_common_letter(first_half, second_half):
    for l in second_half:
        if l in first_half:
            return  l

def letter_points(l):
    if l < "a":
        return ord(l) - ord("A") + 26 + 1 # Uppercase letters are 27-52
    return ord(l) - ord("a") + 1

for line in lines:
    mid = len(line) // 2
    first_half, second_half = line[:mid], line[mid:]

    common_letter = get_common_letter(first_half, second_half)

    point = letter_points(common_letter)
    
    print(first_half, second_half)
    print("\t", common_letter, point)

    points += point

print(points)
