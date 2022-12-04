with open("items.txt") as f:
    data = f.read()

lines = data.split("\n")


def compute_priority(item):
    ascii = ord(item)
    return (ascii - 65 + 1 + 26) if (ascii - 97 < 0) else (ascii - 97 + 1)


print(
    "Part 1:",
    sum(
        compute_priority(
            set(line[: int(len(line) / 2)])
            .intersection(set(line[int(len(line) / 2) :]))
            .pop()
        )
        for line in lines
    ),
)

print(
    "Part 2:",
    sum(
        compute_priority(set.intersection(*(map(set, lines[i : i + 3]))).pop())
        for i in range(0, len(lines), 3)
    ),
)


# print(sum)
