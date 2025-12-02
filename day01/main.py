mod = 100
pointer = 50
p1_counter = 0
p2_counter = 0

def process_rotation(start, instruction):
    """Function that returns the number of zeros that get passed during each instruction"""

    direction = instruction[0]
    steps = int(instruction[1:])

    if direction == "R":
        dir_step = 1
        first_k = -start % mod    # How many clicks until we get to 0?
    else:   # L
        dir_step = -1
        first_k = start % mod

    zeros = 0

    # Part 2: count zeros after each click
    if first_k > 0 and first_k <= steps:
        zeros += 1

    zeros += max(0, (steps - first_k) // mod)

    # Part 1: get final pointer
    new_pointer = (start + dir_step * steps) % mod

    return new_pointer, zeros


with open('input.txt', 'r') as infile:
    lines = infile.readlines()

    for line in lines:
        line = line.strip()
        pointer, zeros_hit = process_rotation(pointer, line)

        # Part 1: only count if pointer ends on 0
        if pointer == 0:
            p1_counter += 1

        # Part 2
        p2_counter += zeros_hit

print(f"Part 1: {p1_counter}")     # 1089
print(f"Part 2: {p2_counter}")     # 6530

