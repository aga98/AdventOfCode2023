from utils import read_input


def process_input(lines: list) -> (int, int):
    time = int(lines[0].split(":")[1].strip().replace(" ", ""))
    distance = int(lines[1].split(":")[1].strip().replace(" ", ""))
    return time, distance


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
    race_time, race_distance = process_input(read_input())
    # slow but works
    win_options = calculate_race_wins(race_time, race_distance)
    print(f"Total wins: {win_options}")
