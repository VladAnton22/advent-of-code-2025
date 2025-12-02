def parse_ranges(content):
    """Parse input string into list of (lo, hi) tuples."""
    ranges = []
    for r in content.split(","):
        a, b = r.split("-")
        ranges.append((int(a), int(b)))
    return ranges

def generate_invalid_numbers(lo, hi):
    """
    Generate all repeated-pattern invalid numbers that fall inside [lo, hi].
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



with open("input.txt", "r") as f:
    content = f.read().strip()

ranges = parse_ranges(content)

result_sum = 0
for lo, hi in ranges:
    invalid_nums = generate_invalid_numbers(lo, hi)
    result_sum += sum(invalid_nums)

print("Part 1:", result_sum)    # 53420042388