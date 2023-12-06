from functools import reduce
from utils import read_input


def process_input(lines: list) -> list:
    times = lines[0].split(":")[1].split()
    times = [int(time) for time in times]
    distances = lines[1].split(":")[1].split()
    distances = [int(distance) for distance in distances]
    return list(zip(times, distances))


def calculate_race_wins(time: int, record: int):
    wins = 0
    for hold_time in range(time):
        racing_time = time - hold_time
        distance = racing_time * hold_time
        if distance > record:
            wins += 1
            print(f"Time: {time}, Hold time: {hold_time}, Racing time: {racing_time}, "
                  f"Distance: {distance} > Record: {record}")
    return wins


if __name__ == "__main__":
    times_distances = process_input(read_input())
    win_options = [calculate_race_wins(t, r) for t, r in times_distances]
    print(f"Wins per race: {win_options}")
    mult = reduce(lambda x, y: x * y, win_options, 1)
    print(f"Total wins: {mult}")
