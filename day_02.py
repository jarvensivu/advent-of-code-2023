from pathlib import Path
from utils import read_input

max_cubes = { "red": 12, "green": 13, "blue": 14, }

def part_one(line):
    game = line.split(":")[1].replace(";", "").replace(",", "").strip().split(" ")
  
    for x in range(0, len(game), 2):
        if int(game[x]) > max_cubes[game[x+1]]:
            return 0

    return int(line.split(":")[0].split(" ")[1])

def part_two(line):
    game = line.split(":")[1].replace(";", "").replace(",", "").strip().split(" ")

    min_cubes = { "red": 0, "green": 0, "blue": 0, }

    for x in range(0, len(game), 2):
        if int(game[x]) > min_cubes[game[x+1]]:
            min_cubes[game[x+1]] = int(game[x])

    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]

def day_02():
    print("Advent of Code - day 2")
    file_path = Path('.', 'data', 'input_02.txt')
    file_content = read_input(file_path)
    if file_content:
        solution1 = sum(part_one(line) for line in file_content)
        print(f"Solution for part one is: {solution1}")
        solution2 = sum(part_two(line) for line in file_content)
        print(f"Solution for part two is: {solution2}")

day_02()