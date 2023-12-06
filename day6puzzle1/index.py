import re

debug = True

input = """Time:      7  15   30
Distance:  9  40  200"""

input = """Time:        38     94     79     70
Distance:   241   1549   1074   1091"""


def debugprint(*args):
    if debug == True:
        print(*args)

def parse_line(line):
    time_or_distance_regex = r"^(.*):\s+(.*)$"
    matches = re.match(time_or_distance_regex, line)
    if not matches:
        raise Exception("Invalid line: " + line)

    numbers = matches.group(2)
    return [int(x) for x in numbers.split() if x != ""]

def get_number_of_record_breakers(time, distance):
    record_breakers = []
    for hold_time in range(1, time):
        total_distance = time * hold_time - hold_time * hold_time
        debugprint(f"Total distance is {total_distance} if we hold for {hold_time} in a {distance} race")
        if total_distance > distance:
            record_breakers.append(hold_time)
    return record_breakers


def parse_input(input):
    total = 1
    lines = input.splitlines()
    if (len(lines) != 2):
        raise Exception("Expected 2 lines, got " + str(len(lines)))
    time_numbers = parse_line(lines[0])
    distance_numbers = parse_line(lines[1])
    if len(time_numbers) != len(distance_numbers):
        raise Exception("Expected same number of time and distance numbers")
    debugprint("Time numbers: " + str(time_numbers))
    debugprint("Distance numbers: " + str(distance_numbers))
    for time, distance in zip(time_numbers, distance_numbers):
        record_breakers = get_number_of_record_breakers(time, distance)        
        debugprint(f"Total record breakers for {time} and {distance} is {len(record_breakers)}")
        total *= len(record_breakers)

    return total

print(parse_input(input))