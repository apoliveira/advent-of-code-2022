def elf_with_most_calories(elf_loads):
    elf_totals = map(sum, elf_loads)

    return max(elf_totals)

lines = open("part_1.txt", "r")
values = []

curr_value = []

for line in lines:
    if line == "\n":
        values += [curr_value]
        curr_value = []
    else:
        curr_value += [ int(line) ]
    
values += [curr_value]

print(elf_with_most_calories( values ) )
