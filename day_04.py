from pathlib import Path
from utils import read_input


def part_one(line):
    numbers = line.split(":")[1].replace("|", "").split()
    matches = len(numbers) - len(set(numbers))
    return int(2 ** (matches - 1))


def part_two(file_content):
    cards = [1] * len(file_content)

    for i, line in enumerate(file_content):
        numbers = line.split(":")[1].replace("|", "").split()
        matches = len(numbers) - len(set(numbers))
        for j in range(1, matches + 1):
            cards[i + j] += cards[i]

    return sum(cards)


def day_04():
    print("Advent of Code - day 4")
    file_path = Path('.', 'data', 'input_04.txt')
    file_content = read_input(file_path)
    if file_content:
        solution1 = sum(part_one(line) for line in file_content)
        print(f"Solution for part one is: {solution1}")
        solution2 = part_two(file_content)
        print(f"Solution for part two is: {solution2}")


day_04()
