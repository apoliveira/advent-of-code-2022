lines = open("input.txt", "r")

points = 0

def to_tuple(s):
    nums = s.split("-")
    return (int(nums[0]), int(nums[1]))

def get_assignments(l):
    a1, a2 = l.split(',')

    return to_tuple(a1), to_tuple(a2)

def end_in(interval, x):
    a,b = interval
    return a <= x <= b

def overlapped(a, b):
    a1, a2 = a
    b1, b2 = b
    return end_in(a, b1) or end_in(a, b2) or end_in(b, a1) or end_in(b, a2)

for line in lines:
    assign1, assign2 = get_assignments(line)

    point = overlapped(assign1, assign2)

    points += point

print(points)
