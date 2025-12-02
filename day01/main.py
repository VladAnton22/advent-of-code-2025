# ------------- Part 1 ---------------

mod = 100
pointer = 50
zero_counter = 0

def change_pointer(current, instruction):
    """Function that returns the new poisition of the dial after an instruction."""

    direction = instruction[0]
    value = int(instruction[1:])

    if direction.lower() == "r":
        new_pointer = (current + value) % mod
    elif direction.lower() == "l":
        new_pointer = (current - value) % mod

    return new_pointer

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

    for line in lines:
        line = line.strip()
        pointer = change_pointer(pointer, line)
        if pointer == 0:
            zero_counter += 1

print(zero_counter)
