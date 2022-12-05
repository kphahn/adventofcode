import collections

with open("crates.txt") as f:
    data = f.read()

storage, instructions_raw = data.split("\n\n")
get_stacks = lambda: [
    [crate for crate in reversed(stack) if crate != " "]
    for stack in zip(*(row[1::4] for row in storage.split("\n")[:-1]))
]

instructions = [
    list(map(int, filter(str.isnumeric, line.split(" "))))
    for line in instructions_raw.split("\n")
]

# Part 1
stacks_1 = get_stacks()
for quantity, source, destination in instructions:
    for i in range(quantity):
        stacks_1[destination - 1].append(stacks_1[source - 1].pop())

# Part 2
stacks_2 = get_stacks()
for quantity, source, destination in instructions:
    stacks_2[destination - 1].extend(
        reversed([stacks_2[source - 1].pop() for i in range(quantity)])
    )

print("Part 1: ", "".join(stack[-1] for stack in stacks_1))
print("Part 2: ", "".join(stack[-1] for stack in stacks_2))
