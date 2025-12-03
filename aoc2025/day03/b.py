from ..core import open_file

batteries: list[list[int]] = []

with open_file() as f:
    for line in f:
        bank = [int(d) for d in line.strip()]
        batteries.append(bank)

total_output_joltage = 0

N_TURNS = 12

for bank in batteries:
    joltage = 0
    min_index = 0
    for turns in range(N_TURNS - 1, -1, -1):
        if min_index < len(bank) - turns - 1:
            digit = max(*bank[min_index : len(bank) - turns])
        else:
            digit = bank[min_index]
        min_index = bank.index(digit, min_index) + 1
        joltage += digit * 10**turns
    total_output_joltage += joltage

print(total_output_joltage)
