def parse_ranges(content):
    """Parse input string into list of (lo, hi) tuples."""
    ranges = []
    for r in content.split(","):
        a, b = r.split("-")
        ranges.append((int(a), int(b)))
    return ranges

def generate_invalid_numbers_p1(lo, hi):
    """
    Generate all numbers in [lo, hi] that are a pattern repeated twice.
    Returns a list of integers.
    """
    invalid = []
    len_lo = len(str(lo))
    len_hi = len(str(hi))

    # Only count even full lengths
    for total_len in range(len_lo + (len_lo % 2), len_hi + 1, 2):
        half_len = total_len // 2
        start = 10 ** (half_len - 1)    # smallest number with half_len digits
        end = 10 ** half_len            # 1 + the largest number with half_len digits

        # Generate s + s patter numbers e.g. (1010, 1111, ..., 9999)
        for x in range(start, end):
            s = str(x)
            num = int(s + s)
            # Check if numbers are inside the current range (lo, hi)
            if lo <= num <= hi:
                invalid.append(num)

    return invalid

def generate_invalid_numbers_p2(lo, hi):
    """
    Generate all numbers in [lo, hi] that are made up of a repeated pattern.
    Returns a list of integers.
    """
    invalid = set()
    len_lo = len(str(lo))
    len_hi = len(str(hi))

    for total_len in range(len_lo, len_hi + 1):
        # Try all divisors of total_len (pattern lengths)
        for pattern_len in range(1, total_len):
            if total_len % pattern_len == 0:
                repetitions = total_len // pattern_len
                if repetitions >= 2:
                    # Generate all patterns of this length
                    start = 10 ** (pattern_len - 1)
                    end = 10 ** pattern_len

                    for x in range(start, end):
                        pattern = str(x)
                        num = int(pattern * repetitions)
                        if lo <= num <= hi:
                            invalid.add(num)

    return list(invalid)



with open("input.txt", "r") as f:
    content = f.read().strip()

ranges = parse_ranges(content)

# Part 1
result_sum_p1 = 0
for lo, hi in ranges:
    invalid_nums = generate_invalid_numbers_p1(lo, hi)
    result_sum_p1 += sum(invalid_nums)

print("Part 1:", result_sum_p1)    # 53420042388

# Part 2
result_sum_p2 = 0
for lo, hi in ranges:
    invalid_nums = generate_invalid_numbers_p2(lo, hi)
    result_sum_p2 += sum(invalid_nums)

print("Part2:", result_sum_p2)      # 69553832684