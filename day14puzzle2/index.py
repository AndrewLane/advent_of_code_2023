debug = False

input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

input = """##..O..#...#..#..#...#.......O.#.#...#..#...#....#.#...##..OO....#.O.....O.O.#...O..#.........#.#OO.
O#O.OOO......OO...O##.#.........#OOO..#...#....#.O...#.#.OO......O..#.O#....#..#.O.....O...O......#.
O.O....O..#.O#.O#......#O.#.#O.#.....OO.#O.......O.#O.#...#.O###.OO..O...O..O#...#....#.#.O....O.O..
O.....#.....#.....O##..OO..O.##..O....O..O...O.........O.....#.#.OO.OO....O..#O....#...O.OO.O...O..O
.O.....#..O..#.........O#...........O.#..#..#.OO#..#....O.#O..OO..O#O.O#.##..#...OO#..O...#...O.....
......O...O.OO......##.O....#....O#...#.......#..#..##.###....OO.O#.O..#.O..OO#.O#O..#..#.O..O.....#
O..O##...O#..#.##.....O##......O..O......##.#...O...#........O.#.....O#O...#O...O...#...O..O.O#.##..
....#.#.....OO#O.#.O...#OO...#..##.#...O...O.#...#.O.O#.....OO.....O.#.O#..##.O#.##O..O..#O.#.#.#...
O.#...............###...OO.O...O..OO.#...........####...###OO#.O##O..#.#.....O....#OO.O...#O......OO
O.....O........O.OOO....#......OO..##.OO.#OO#..#.O....#.O.##...#..#.##......O..O..O#.....#...#O...#.
O....O..O..#.OOO...#....O#........OO#O..O.....O#..#...#.#..O...#......O#........OO#...O......O..###O
OOO..OO.................O##OO..#O..O#.#..O....OO...O..OO.#.#.O#OO....#..##....O....O....#..##.....O.
O.....O.O#O.##.......O..O.O##.....#O..O#...O..O..........O.#........#O.#O.#.#OO..O#.......#.#...O#O.
.#.....O.OO...O####O..O...#.O.##.#.O.O.#..#..OO.O..##....#OOO...O..#.O#.O#.....OOO.O#O#.#O...O#O.#..
.OO.O.#........OO.#O...O..#....O.#...........O...O.#..O.....#.O.O..O#.......O.O#O.###..#O..O....O#..
...O..#.OOO..#..OO.OOO#..OOO.O.#O...O.O#..#....O...O....#.....O..O.##.#OO.#.#....#....###..#O#...#..
..##O#.#..O#.O....OO.#O.O.OOOO.##..OO...OO..O......O.O..O#..O.#....O.#O...O.OOOO#.O..#OO...O..#.....
...#..O....O.....#.OO.#O......O......#..O#...O#...#OO...O#......#.O.O...#OOO.#..O........O#....#..#.
O.........O.......##.O.O#...#.#....#.#..#....#.OO...O#.#O.#O...O...#O.OO...O.#....#OO.O..#.###.O..O.
.#....#.#..#.O..#..OO.#.....O...O...#O..O.#......#...O....##......#.#O..O.##......#...##.O..O..OO.#.
........O.O#O..#...OO.O...O.....O.O.##.O....##.###O#O..O..#.##...O..##.......O.##..............#..#O
##.....O....O.###..#O..#....OO..OO..OO..O.....O..#....OO....#..O#.....#O..#.#O.#......O#.........#.O
....O..O#.#.O..O.O...OO...........#...O.#.OOOO..OO..##........O......#...O.......#.........OO...#.O#
O..OO..#.O...##.......#.......O...##.O.#......#....O.#...O....#...#..#..O...O..OO..##O...O##.OO#....
OOOOO..#...#OO.........#....O..#.#OO..........O.....O..O.#.......#.OO..#.#.O.#....O..O.....O.#..OO#.
O.OO.#O.#........O#.#O.O...#.......#O.O....#.#.O.#O...#...#O#.O#...#.#..O..O#OO#.O.O.......O.#O.....
....#.O.........OOO...#..O...#..O..#O.#OO...O.##O...#..O...##......O...O..O.#..#O..O..#.#...O..O.O..
O.......O....#..O.O....#......#..#......##..#.#..O...#..O..O.O..#.#O.#OO.O#.....O##O..O.#..###O..O..
O.O.O..........#O.OO.O....O..#..O##..O..OO....O.OO.#O.........O..#......O........OO....#O.........O.
#...#.O..###.........O.OO.#....#OO....#.O.......O..OO.O.#O#..##.O..O......O.....#..#.#..O.O#.#OO.O.#
....O....#..O..OO......OO#..##OO.O.#O.O#...O..#O#......O.....OO....OOO.#.OOO.O##O........O....O.....
..OO#..O...#.O.#OO.....#..O...O....#...OO...#O.#...........O..##....O.OOO.OO#O.....#.........#.....O
.O...O..#...#O...O..OOO.#..O..OO#..#.##..OO.#.OO.O.....#O......O..#.#..#....#.OO..#....#...OO...O.OO
...#......O.#.O.O....O.....O#..O#..#...#.#...#O........#.#OOO.........O....#.O##OOO.....#.#O#....O..
.O..#..OO..O#.#..O.O...O.O#..O..O..O...OOOO.O....O..##...#OO##.#..O##O.#......#.O...OO#O##..#.#.#O.O
..#........#.#..O.OO.#O....#.#..##..#.......#O..#...O.#....#........O...O.##.OO#.......#.OO.##O#.O#.
#O..#....O###OO.#.#.##....O...#..#O.#.#......#.....##.#O#O..O..#..#.OO.O..##...O...........#.....#O#
OO....###.O.#O.#...#..#O.O.....O...#O#.O#..O..#O#......O.O...O.#....O.#.#O..OO...O.#...O..O...O.###.
O..O.O..OO.OO.#O..#............#......O...#....O###.O...#.O.O....#...OOO...O.O......O..##.....O.##.O
.O.O..OO.#O...#.#O#..O#O...##.#.##...O...O.O.O..OO.OO.O..#.O.#.O.........O.O#.O.#.#......O.....#...#
#.##.......#O.....#......OOO...O.........#O.O.#O#..O.....O...O#.#.....#..#........####.O.O..O..##O..
.O.............OO.O..#..#.OOO...#.O..##O..O...O..O..OO............O.O.O.OO..O.#O..#OOO.O..##..OOO#.#
.#.......O.....O..O..OO.....O..#O...OO#O.....#..#..OO..#.O.O.#........O......O.....O...O...OO.O.....
#.#..#.#.O..O..............O#O#...O.O..#.#.O.#.#.....#..O#.O...#........O.#..O....#O##OO..O...##...O
.#....#.#..O.O...O..O#...O..O..##....O......O#..O.O...OO.O.#...O.......#..O....O....##.#...OO.#.....
..##....#.O.#..O.#......O#...###.#.##O.O..#........O..O#O.........#.###O.O#...O..#OOO.##O.#.O....#.#
##..#...O....O...OO.OO..O#..#.#.O.O.......O#.O.O........O..##...O..#......O..#..O.O......##...OO....
O..#..O.......#O.O..##.O.O#....OO#.O.....#......##...#..###.OO..#..O.#...OO..OO.OO.OO.OO......#....#
.O...#OOO.O...#.O#......OO..O....#...O.OO#......#.....O#O....#....##O#.......#O#O.##O....#....O.O...
...#O.#O...O..O..O..#..OO.O#..........#.OO..O.....#O.OO.O....O.O...O..#............O#..O..O..#O#.#..
....O.O...O........O..##..O.O..#..#.O...O#OO#..O..#..#OO#O..O...#.O#.##...OO...#...#......O..#...O.O
O.....#O#....O#...#.O..OO.#.#....#O#.O..#...#..O##O..#.O..O..O#.O..OO.#.#O..O....#...OOO.....O....#.
.#.#..O.##.O#.........O#.O....O....#.#...#O..O....O...#..O#.#..O....O.....OO.....#......OO.....#..O.
O......O.....#.....O##O#O......#....OO...#..O...O....#O......OO.O##.O#O.OOO.....OO.#...O#...O...#..#
O..O...O#...#...O..#..O..O...#O..#O.....O##.#.#...O.O...#..O...#.OO#O..#..#.#.O.O.O..#..O#....O#O...
.........#O.O....OO.#OOO.....O#...O..#.O#O#.#........O...#O.....O.#.#.O.O#...........O...#...#.....#
..O...OO#O.#O..OO..OO###.OO....O......###..O........OO..#..O..........#.......O..O..O..#...O..OO..#.
#.OO...........OO#.....O......O##..O.#....O.O.#....OO.#O##OO...O...O..O.#.#OO....#.#......#.##.O...O
..#..#.O.....#..#..O#..O..O......##OO#O....#.......OOO...#O..O...#..O...#..O......O.O..O..O.#...O#..
.O.OO#...#.......#.......O..O#.O.....#.O..O..OO#......###..OO.O.O.#.#........#.#.#........OO#O.#...O
.##....#..OO..O.OO.O.#...O#.##.#...O....O.#.....#...#..O#.##.....O....###.O.#...O.#.O..#.#......O...
OO..O..#.O...###.O..#..O.OO#..O.....O.O...O.....##OOO.O#.O.....#..#.....O....O#...#..O.O#.#.....O...
...##.O..#...O.#..#OO.....O#....##OO.....OO....#O...................#.O#OO.#.OO................O.O..
...O...#.....O..#.#.O..O.O......O.........O.O#..#.........##......#..#....O..#..##O.....O.O......O.#
.#...O........#.OOO......#OO.O#........#.....#.#.....#OO.#.O.O..O.O..#...O...#..###.....OOO...O#OO..
...OOO....O...#..#.O......O..#.##O.#.OO...OOO#O...##O#.....#...#..O#....#.....#O#..O#..#...#..OO....
.O...#..OO..O...#...O..##.....#O##..O#...O.O..O##..OOO#.#..#O..#...#..OO.....#....##.#.......O#.O..O
O#OO..O#O..........#..#......#..O#.#O#...O...#...OO..........OO..OOO#O..O.O.....O.O.#O.O....#.......
#O#...O#O..O...O.....OO..........#OOOO.#O..OO#O#O..#.O.#.#O##..#.O.OO.#...#.....#O..O....O...#...O#.
O.#.O.OOO..O.O.O##OO...O##..O...###..OOO...O..#..#.......#O.........#.#....OO.#.O#...#.O...O.O.....O
#.#..O..O.O###..#O.....#......OO.O..##.#......#.O#OO.....O......#.........O#...OO..#.....O...O.#.O..
..O........O...##..#....#.......O.##OOO........O....O......#....#..O#...O..........O##....#.#O.O#O#O
..##O#.O.........O.O...........O.OO.#..##.O#.#.OO..O##O.....#O...#..O...#...#.O...#...##.......O.O..
.O..#.....#O.O.#O#O#.....O....#....##O....#.......OO.#...O#...OO#...O..#.O#...O.O#..O.O##O.....OO.#.
.O.O......#.O...O.#.#O....OO.....O.#..OOO#.O..#O.#OO....##OO.OOOOO#.OO...#.O...#......#.O......#.#OO
.#O.OO.#O.....#.O..O#...........O#OO.#.....#.....#.OO......O.#.#.#O..O#.#O.O.#O......OOO.#..O.OO.O..
O........OOO..OO#.#.##.#...#.O.......#....O.##O...##O.O.#..#..O.O......#...#..#.#O....#...OO........
O..#.#....#.#.O..O#OOO....O..O....O#.OO#.#.O.O......OO..#O..O#O.##....O.##....#O.O#.O...........O.O.
...O.#.#.O..O#....#.O..O.O...O..O.#..O#...O#......O.#...O.OOO.##OOO...#....O.....#..O....O.O.#..#...
.O..O#.#.O.....#O..#O.O.#....OO..#......#.#..........O#..##...O...O#...O.OO..O#O.....O.OO.O#O..O....
#...O...OO.#.OO.OO..O..#.#.O....##..O..O....#OO#.....O.O.............##..........O....O..#.O.##.....
....#....##O.#..O#.#.#.O.#O....#O..O##O...#.#...OO#O.##.#......#O.OO...#.......#O#...O#.......O.#..O
....O.##.O.O#.#....O.....O#O.O.O#.O.........OOO#.#O##O..O.O#..OO.#.#O.......##O...O.....O...O....O..
....O....#..OO...#.O.#..O......O..O..##.O#..#OO..OO.O....O##....O.##.#......O.OO##....O....#.O#.....
#O..O#..O..#..OO.......O...O.....O...O..O.#.#.#OO.O...........#..#..O..O#.#.#O.......#O.#..#.#.O.O..
.O....#.##.#...O....O.#OOOO.O#O.##O#..##..#O.#..#.O.#O......#...#......O.OO.O.O#..O#.O.O...##..#O...
.O...O.......###.#...##.#..O..O...#.#....#OOOOO.O.#O#....O..O#.O#O...#.OO...O.....OO.O.O.O..#.O#....
........O#..#O.#..O.#..###O#...O#..#.O..#OO...#.#.#.O#......O....O......#..##..#OO.O#OOO.#..#.O..#O.
#..#O....O..O.....#O.#O..O.O#.#.O.......#O.OO.#.O...O.O...O.O..#.#O##O..#O.#.OO...#........O.O#...#.
...#..O..##..O.#..#..O.#.#.O....OOO#...O.##.#.O.#...O#..OO.OOO#....O..O....OO#O.#O.#...O..#.O...O.#.
.O....#OO#.#O......#O..OO...#O.OO.......O..O##O#.#..OO.O.#O#..........#OO...............OO.#...#O..#
.###..##...O..O.O....O...#.O..OO.#.#O.#.....O...O..#.....#..........#O.O#.#..O....##O..OO.O...#.O.O.
..#...OO#.....#......##....O...O..O..O.#.O..#.O##.##..OO.O...#...O....O..#..O##.#..#.OO....#O#......
.....##......OO.O..#......#.#.O##..#.O.........O.OO..O.#....O.....#O..O.....#O.....#O........#..O...
....#..O..OOO..OO...O.##.O..........#O.....#O.O.OOOOOOO...OO.....O......#..OOO#...####O..OO.O.#.....
.O...O#.OOOOO##O#.....#...O.O.#..#.....O.#......O..O.OO..OO.#.OO...#O#O..#.O..O....OO.O..O..O.#O....
.......OO...#......#.O.......#.OO..#..O##O#.#.O.O.#........O.....#O....O..#....OOO...OOO..........O.
O..O..#...#.#.O#...O.....O.#.....O..#O#.....#....#.O..O.#O.#..#....O.....OO..O..#...O.....O#.O...#..
#O....O.#OOO#.........O...O#...O##O..O#O.O.....O...O.#.O..##...#OO..#..O..#...#....#.#.....#....OO..
#OO.....#..#...OO.....O...#...............#.......#.OOOO#.#.....O.O.O.#.O..##......OO#..#...O......O"""


def debugprint(*args):
    if debug == True:
        print(*args)


def get_pretty_figure(figure):
    return "\n".join(figure)


def process_shift(line, shift_direction):
    arr = list(line)
    done_something = True
    while done_something == True:
        done_something = False
        for i in range(0, len(arr)):
            if arr[i] == "O":
                if shift_direction == "left":
                    if i > 0 and arr[i - 1] == ".":
                        arr[i - 1] = "O"
                        arr[i] = "."
                        done_something = True
                else:
                    if i < len(arr) - 1 and arr[i + 1] == ".":
                        arr[i + 1] = "O"
                        arr[i] = "."
                        done_something = True
            elif arr[i] == "." or arr[i] == "#":
                pass
            else:
                raise Exception(f"Unknown character {arr[i]} in line: {line}")

    return "".join(arr)


def calculate_north_weight(figure):
    transposed_figure = transpose_figure(figure)
    total = 0
    line_length = len(transposed_figure[0])
    for line in transposed_figure:
        for idx, char in enumerate(line):
            if char == "O":
                total += line_length - idx

    return total


def transpose_figure(figure):
    return list(["".join(item) for item in map(list, zip(*figure))])


def process_north(figure):
    figure = transpose_figure(figure)
    figure = [process_shift(line, "left") for line in figure]
    return transpose_figure(figure)


def process_south(figure):
    figure = transpose_figure(figure)
    figure = [process_shift(line, "right") for line in figure]
    return transpose_figure(figure)


def process_east(figure):
    return [process_shift(line, "right") for line in figure]


def process_west(figure):
    return [process_shift(line, "left") for line in figure]


def calculate_hash_of_figure(figure):
    return hash("".join(figure))


def process_figure(figure):
    hashes = {}
    north_weights = {}

    debugprint(get_pretty_figure(figure))
    debugprint("")
    cycles = 1000000000
    for cycle in range(1, cycles + 1):
        hash_of_before = calculate_hash_of_figure(figure)
        if hash_of_before in hashes.keys():
            # we found a loop!
            cycle_start = hashes[hash_of_before]
            debugprint(f"Cycle {cycle} maps to cycle {cycle_start}")

            cycle_loop_length = cycle - cycle_start

            figure = process_east(process_south(process_west(process_north(figure))))
            debugprint(f"After cycle {cycle}")
            debugprint(get_pretty_figure(figure))
            debugprint(f"^^^ should be the same as after cycle {cycle_start}")

            return north_weights[
                cycle_start + ((cycles - cycle_start) % cycle_loop_length)
            ]
        else:
            figure = process_east(process_south(process_west(process_north(figure))))
            hashes[hash_of_before] = cycle
            debugprint(f"After cycle {cycle}")
            debugprint(get_pretty_figure(figure))
            north_weights[cycle] = calculate_north_weight(figure)
            debugprint(f"North weight after cycle {cycle}: {north_weights[cycle]}")
    return north_weights[cycle]


def parse_input(input):
    return process_figure(input.splitlines())


print(parse_input(input))
