from pathlib import Path
from utils import read_input


def part_one(values):
    if all(value == 0 for value in values):
        return 0
    new_sequence = []
    for x in range(len(values) - 1):
        difference = int(values[x+1]) - int(values[x])
        new_sequence.append(difference)
    return int(values[-1]) + part_one(new_sequence)


def part_two(values):
    if all(value == 0 for value in values):
        return 0
    new_sequence = []
    for x in range(len(values) - 1):
        difference = int(values[x+1]) - int(values[x])
        new_sequence.append(difference)
    return int(values[0]) - part_two(new_sequence)


def day_09():
    print("Advent of Code - day 9")
    file_path = Path('.', 'data', 'input_09.txt')
    file_content = read_input(file_path)
    if file_content:
        solution1 = sum(part_one(line.split()) for line in file_content)
        print(f"Solution for part one: {solution1}")
        solution2 = sum(part_two(line.split()) for line in file_content)
        print(f"Solution for part two: {solution2}")


day_09()
