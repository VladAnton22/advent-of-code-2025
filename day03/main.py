def calculate_joltage(bank):
    largest_num = 0
    for tens_index in range(len(bank) - 1):
        for ones_index in range(tens_index + 1, len(bank)):
            current_num = int(str(bank[tens_index]) + str(bank[ones_index]))
            if current_num > largest_num:
                largest_num = current_num

    return largest_num


with open('input.txt', 'r') as f:
    batteries = f.readlines()

total_joltage = 0
for bank in batteries:
    bank = bank.strip()
    max_joltage = calculate_joltage(bank)
    total_joltage += max_joltage

print("Part 1:", total_joltage)     # 16927