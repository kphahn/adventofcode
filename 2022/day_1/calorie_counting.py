with open("calorie_counting.txt") as f:
    data = f.read()

calories_per_elve = [sum(map(int, x.split("\n"))) for x in data.split("\n\n")]
max_calories = max(calories_per_elve)
top_three = sum(sorted(calories_per_elve, reverse=True)[:3])
print(max_calories)
print(top_three)
