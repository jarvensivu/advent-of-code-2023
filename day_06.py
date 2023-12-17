import functools
from pathlib import Path
from utils import read_input


def calculate_options(allowed_time, record_distance):
    min_to_beat_record = None
    max_to_beat_record = None

    for x in range(1, int(allowed_time)):
        distance = x * (int(allowed_time) - x)
        if distance > int(record_distance):
            min_to_beat_record = x
            break

    for x in range(int(allowed_time), 1, -1):
        distance = x * (int(allowed_time) - x)
        if distance > int(record_distance):
            max_to_beat_record = x
            break
    
    if min_to_beat_record is None or max_to_beat_record is None:
        return 0

    return max_to_beat_record - min_to_beat_record + 1


def part_one(file_content):
    allowed_times = file_content[0].split(':')[1].split()
    record_distances = file_content[1].split(':')[1].split()

    options = []
    for x in range(len(allowed_times)):
        options.append(calculate_options(allowed_times[x], record_distances[x]))

    return functools.reduce(lambda x, y: x * y, options)


def part_two(file_content):
    allowed_time = file_content[0].split(':')[1].replace(' ', '')
    record_distance = file_content[1].split(':')[1].replace(' ', '')

    return calculate_options(allowed_time, record_distance)


def day_06():
    print("Advent of Code - day 6")
    file_path = Path('.', 'data', 'input_06.txt')
    file_content = read_input(file_path)
    if file_content:
        solution1 = part_one(file_content)
        print(f"Solution for part one is: {solution1}")
        solution2 = part_two(file_content)
        print(f"Solution for part two is: {solution2}")


day_06()
