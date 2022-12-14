from collections import deque

lines = open("input.txt", "r").readlines()

split_index = lines.index("\n")
config, moves = lines[:split_index ], lines[split_index + 1:]

def get_info(move):
    split = move.split(" ")

    return int(split[1]), int(split[3]), int(split[5])

def from_config_line(line):
    entries = [ line[i:i+4] for i in range(0,len(line), 4) ]

    return list(
            map( 
                lambda xs: xs.replace("[", "").replace("]","").replace(" ", "").replace("\n",""),
                entries
            )
    )

def from_config(confg):
    num_chars = len(config[0])
    num_stacks = ( num_chars + 1 ) // 4

    stacks = []
    for _ in range(num_stacks):
        stacks.append(deque())

    for line in config[:-1]:
        entries = from_config_line(line)
        for i, entry in enumerate(entries):
            if entry:
                stacks[i].append(entry)

    return stacks

def move_crates(start, end, amt):
    crates = [deques[start - 1].popleft() for _ in range(amt)]

    deques[end - 1].extendleft(crates[::-1])

# init dequeues
deques = from_config(config)

for move in moves:
    amt, start, end = get_info(move)
    
    move_crates(start, end, amt)
    
print("".join([de[0] for de in deques]))
