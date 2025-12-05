from ..core import open_file


with open_file() as f:
    grid = [[1 if c == "@" else 0 for c in line.strip()] for line in f]

accessible = 0

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if not val:
            continue
        adjacent = 0
        if i > 0:
            adjacent += sum(grid[i - 1][max(j - 1, 0) : min(j + 2, len(row))])
        if j > 0:
            adjacent += row[j - 1]
        if j < len(row) - 1:
            adjacent += row[j + 1]
        if i < len(grid) - 1:
            adjacent += sum(grid[i + 1][max(j - 1, 0) : min(j + 2, len(row))])
        if adjacent < 4:
            accessible += 1

print(accessible)
