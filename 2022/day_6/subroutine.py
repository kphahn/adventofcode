with open("signals.txt") as f:
    data = f.read()


def sliding_window(n, iterable):
    for i in range(len(iterable) - n + 1):
        yield iterable[i : i + n]


def find_sequence(n, sequence):
    for i, window in enumerate(sliding_window(n, sequence)):
        if len(window) == len(set(window)):
            return i + n


print("Part 1:", find_sequence(4, data))
print("Part 1:", find_sequence(14, data))
