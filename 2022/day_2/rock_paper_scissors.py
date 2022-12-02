with open("strategy_guide.txt") as f:
    data = f.read()
games_guide = data.split("\n")

# part 1
points = {"X": 1, "Y": 2, "Z": 3}
constellations = [
    ["A Z", "B X", "C Y"],  # lose
    ["A X", "B Y", "C Z"],  # draw
    ["A Y", "B Z", "C X"],  # win
]

# part 2
outcome = {"X": 0, "Y": 1, "Z": 2}
shapes = [
    {"A": 3, "B": 1, "C": 2},  # lose
    {"A": 1, "B": 2, "C": 3},  # draw
    {"A": 2, "B": 3, "C": 1},  # win
]

sum_part_1 = 0
sum_part_2 = 0
for game in games_guide:

    # part 1
    for i in range(0, 3):
        if any(game == x for x in constellations[i]):
            sum_part_1 = sum_part_1 + i * 3 + points[game[2:]]

    # part 2
    o = outcome[game[2:]]
    sum_part_2 = sum_part_2 + o * 3 + shapes[o][game[:1]]

print(sum_part_1)
print(sum_part_2)
