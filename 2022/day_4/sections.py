with open("sections.txt") as f:
    data = f.read()

lines = data.split("\n")


t = [tuple(tuple(map(int, s.split("-"))) for s in x.split(",")) for x in lines]
print(
    "Part 1:",
    sum(((a >= c and b <= d) or (a <= c and b >= d) for ((a, b), (c, d)) in t)),
)

print(
    "Part 2:",
    sum((a <= d and b >= c for ((a, b), (c, d)) in t)),
)
