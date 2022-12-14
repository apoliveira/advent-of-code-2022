lines = open("input.txt", "r")

points = 0

def to_tuple(s):
    nums = s.split("-")
    return (int(nums[0]), int(nums[1]))

def get_assignments(l):
    a1, a2 = l.split(',')

    return to_tuple(a1), to_tuple(a2)

def is_in(t1, t2):
    a,b = t1
    x,y = t2
    return x <= a and b <= y

def contained(a1, a2):
    return is_in(a1, a2) or is_in(a2, a1)

for line in lines:
    assign1, assign2 = get_assignments(line)

    point = contained(assign1, assign2)

    points += point

print(points)
