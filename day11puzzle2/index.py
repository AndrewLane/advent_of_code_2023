import re

debug = False

input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

input = """...#...............................................#............................#........#.............................................#....
.................................#............#...........................#.........................#....................#..................
.......................#........................................#...........................................................................
..........#...........................................................................#.....................................................
...................#.........#............#.....................................................#...........................................
...........................................................................................................#......#.............#...........
.......#......#..........#..................................................................................................................
..........................................................#............#....................................................................
.#...............................................#...........................#......................#..................................#....
..............................................................#.....................#................................#.....#................
.......................#.......#.....#...................................................................#.................................#
..................#.........................................................................................................................
.............#........................................#.............#.............................#...........................#.............
............................................................................................#.......................................#.......
............................#..................................................#.................................#..........................
.........#...........#...............................................................................#......................................
................................#......#..........#......................................................................#..................
...........................................................................................................#................................
.................#....................................................................#...........#.......................................#.
..........................................................................#.....#.....................................#.....................
..............................................................#.............................................................................
....................................................................#..................................#.............................#......
..#..........................................#..............................................................................................
........................................................................................#..................#......#.........................
.........#.......#......#..........................#.........................................#..............................................
...........................................................................#........................#.......................................
.....#......................................................#.....................#...................................................#.....
..............................#...........#...........#...........#.........................................................................
#................................................#......................#.................................#.................................
........#..........................................................................................................#........................
..............#...........#..........#...................#..................................................................................
....................#..........................................................................#............................................
.........................................................................................#..............#....................#......#.......
...#......................................#..................#..............................................................................
..................................#................................#........................................#............#..................
.......................#............................................................#...........................................#.........#.
...............................................................................#................#...........................................
...............................#............................................................................................................
................#.......................#.................................................#.................................................
.........#..................................................#..........#.............................................................#......
.....................#.............................#........................................................................................
...............................................................................................#.......#.....................#..............
..................................#................................................................................#....................#...
.#.....#.....#.............................#....................................#.....#.....................#...............................
......................................#....................................#.....................................................#..........
.........................#..................................................................................................................
...................................................#........................................................................................
..............................#..............................................................#......#..................#....................
....................#...................#..........................#..........#...........................#....................#............
......................................................................................#.....................................................
..#.....#...........................#.....................#.................................................................................
............................................................................................................................................
............................................................................................................................................
................#.......................................................................................#...............................#...
.......................#.....................................................#.......#......................................................
............................................................................................................................................
.....#......................#.....#...........#................................................#..................#.........................
................................................................................#............................#..............................
.......................................................................#........................................................#...........
..........#...........................................#...............................#................................................#....
.......................................#...................................#.........................#...................#..................
....................#............................#.........#......#...........................#....................................#........
............................................................................................................................................
..#.....................................................................................#......................#............................
................................#........................................#....................................................#.............
............#..............................................................................................................................#
...............................................................#.......................................#...........#........................
......#...............#....................#........................#........#...............................#..............................
.............................#...............................................................#..............................................
............................................................................................................................................
.........................................................................................................#..................................
..#.............................#.......................#.............................#...........................................#.........
..............#..................................#..............................................#.............#..............#..............
..........................................................................#...........................................#.....................
..................#........................................#................................#.........................................#.....
............................#.......................................................................#.......................................
........................................#..........#...........#............................................................................
...........#................................................................................................................................
.........................#........................................................#..........................................#..............
................................................................................................#......#............#................#......
#.....................................#.....#..........................#....................................................................
.....#.......#.................#.....................#......................................#...................................#...........
............................................................................................................................................
.........#..........................................................#................#...............#......#............#.................#
............................#...............................#..................#......................................................#.....
................................................................................................#............................#..............
#......................#..........#.........................................................................................................
..................#................................#...............................#....................#.......#...........................
.......#..............................#.....#.............................................................................#.................
............#.......................................................#........#..................................................#...........
..............................................................................................#....................#......................#.
............................#...........................................................#..................#................................
#............................................................................................................................#..............
......#................#............#.................#..............................................#.............................#........
................#.............................................................#......#......................................................
................................#..............#..............#.........#...................................................................
.......................................#...............................................................................#................#...
...........#.............................................#..............................#...................................................
....................................................#.......................................................................#...............
.....#.................#..........................................#...........................................#.............................
#..............................#..................................................................#.........................................
...........................................#.............................................................#..........................#.......
.................................................#........#....................#............................................................
.............#..........................................................................#..........................#...........#............
............................................................................................................................................
..................#..............................................#.................................#.....................#..................
...................................................#....................#......................................#.......................#....
........................#.....................#.............................................................................................
...#...........................................................................#.....#.....#........................#..............#........
.............................................................#..............................................................................
..........#..................#.......................#.........................................#........#...................................
...........................................................................#..................................................#.............
.......................#.........#.........#..........................................................................#.....................
...............................................................................................................#............................
...#............#........................................#.....................#.............#........#.....................................
........................................................................................#..............................................#....
..........#..............#.....#.....................................#.............#........................................................
............................................................................................................................................
...................................................#........#...............#..............#...............#...........#....................
.....................#......................................................................................................................
.......................................#...............................................................#..........#.........................
.....#...........#..................................................................................................................#.......
.....................................................................................#......................................#...............
.............#..............................................................................................................................
........................................................................#.......#..............#................................#...........
.....................#..........#.......................#...................................................................................
.....................................................................................................................#...............#......
...........#...............#.............#..................................................#.......#......................#...............#
.................................................................#........#...............................#.................................
#............................................#..............................................................................................
......................................................................................#.....................................................
.........................................................#.....................................#..................................#.........
...................................................................#..............#...........................#........#....................
......#..........................................#..................................................#.......................................
..........................................................................................................#.................................
....................#..............#..........................#................................................................#............
...............................................................................#........#...........................................#.......
..........................................#......................................................#..........................................
........................#........................................#......#..........................................#........................
...........#.....................#...............#.......#.................................................#...............#...........#...."""


def debugprint(*args):
    if debug == True:
        print(*args)


all_galaxies = []


def parse_line(line, y):
    line_regex = r"^[\.#]+$"
    matches = re.match(line_regex, line)
    if not matches:
        raise Exception("Invalid line: " + line)

    # find all hashtags in the line
    for match in re.finditer("#", line):
        x = match.start()
        galaxy = (x, y)
        all_galaxies.append(galaxy)


def calculate_sum_of_shorted_distances(all_galaxies, galaxyless_rows, galaxyless_cols):
    total = 0
    for i in range(0, len(all_galaxies)):
        for j in range(i + 1, len(all_galaxies)):
            galaxy1 = all_galaxies[i]
            galaxy2 = all_galaxies[j]
            debugprint("Calculating distance between ", galaxy1, " and ", galaxy2)
            min_x = min(galaxy1[0], galaxy2[0])
            max_x = max(galaxy1[0], galaxy2[0])
            min_y = min(galaxy1[1], galaxy2[1])
            max_y = max(galaxy1[1], galaxy2[1])
            extra_x = 0
            extra_y = 0
            for x in range(min_x, max_x + 1):
                if x in galaxyless_cols:
                    extra_x += 1_000_000 - 1
            for y in range(min_y, max_y + 1):
                if y in galaxyless_rows:
                    extra_y += 1_000_000 - 1
            debugprint(
                f"Total of {(max_x-min_x+extra_x)} steps in x, {max_y-min_y+extra_y} steps in y"
            )
            total += (max_x - min_x + extra_x) + (max_y - min_y + extra_y)
    return total


def parse_input(input):
    lines = input.splitlines()
    max_y = len(lines)
    max_x = len(lines[0])
    for y, line in enumerate(lines):
        parse_line(line, y)

    debugprint(all_galaxies)
    galaxyless_rows = [
        y for y in range(max_y) if not any(galaxy[1] == y for galaxy in all_galaxies)
    ]
    galaxyless_cols = [
        x for x in range(max_x) if not any(galaxy[0] == x for galaxy in all_galaxies)
    ]

    debugprint(galaxyless_rows, "galaxyless rows")
    debugprint(galaxyless_cols, "galaxyless cols")

    return calculate_sum_of_shorted_distances(
        all_galaxies, galaxyless_rows, galaxyless_cols
    )


print(parse_input(input))
