from ..core import open_file

batteries: list[list[int]] = []

with open_file() as f:
    for line in f:
        bank = [int(d) for d in line.strip()]
        batteries.append(bank)

total_output_joltage = 0

for bank in batteries:
    first = max(*bank[:-1])
    i = bank.index(first)
    if i < len(bank) - 2:
        second = max(*bank[(i + 1) :])
    else:
        second = bank[-1]

    total_output_joltage += first * 10 + second

print(total_output_joltage)
