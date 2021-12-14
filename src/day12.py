from typing import List, Tuple


def is_small_cave(input: str) -> bool:
    return not input.isupper() and input not in ("start", "end")


def find_next_route_options(
    curr_pos: str, input: List[Tuple[str, str]], path: List[str]
) -> List[str]:
    options = []
    small_cave_visited_twice = ""
    for cave in path:
        if is_small_cave(cave) and path.count(cave) > 1:
            small_cave_visited_twice = cave
            break
    # print(small_cave_visited_twice)
    for route in input:
        # works for part 1:
        # if route[0] == curr_pos and not (is_small_cave(route[1]) and route[1] in path):
        #     options.append(route[1])
        # elif (
        #     route[1] == curr_pos
        #     # not a small cave that has already been visited
        #     and not (is_small_cave(route[0]) and route[0] in path)
        #     and route[0] not in ("start", "end")
        # ):
        #     options.append(route[0])

        if curr_pos == route[0] and route[1] not in ["start"]:
            if is_small_cave(route[1]):
                # if no small cave has been visited twice, this one can be an option
                if small_cave_visited_twice == "":
                    options.append(route[1])
                # if the destination cave has been visited twice, then don't do anything
                elif small_cave_visited_twice == route[1]:
                    pass
                # if one of the caves has been visited twice,
                # then only add this one as an option if it has not been visited before
                elif path.count(route[1]) == 0:
                    options.append(route[1])
            else:
                # add any non-small caves
                options.append(route[1])
        elif curr_pos == route[1] and route[0] not in ["start"]:
            if is_small_cave(route[0]):
                if small_cave_visited_twice == "":
                    options.append(route[0])
                elif small_cave_visited_twice == route[0]:
                    pass
                elif path.count(route[0]) == 0:
                    options.append(route[0])
            else:
                options.append(route[0])
    return options


if __name__ == "__main__":
    cave_system = [
        tuple(line.rstrip().split("-"))
        for line in open("./src/day12_input.txt", "r").readlines()
    ]
    curr_pos = "start"
    paths = [[curr_pos]]
    finished_paths = 0
    while finished_paths < len(paths):
        for path in paths:
            path_copy = path.copy()
            current_loc = path[len(path) - 1]
            if "end" not in path and "stuck" not in path:
                curr_path_updated = False
                # Find the possible routes from last entry in the path
                options = find_next_route_options(current_loc, cave_system, path)
                for dest in options:
                    if not curr_path_updated:
                        path.append(dest)
                        curr_path_updated = True
                        if dest == "end":
                            finished_paths += 1
                    else:
                        if (path_copy + [dest]) not in paths:
                            paths.append(path_copy + [dest])
                            curr_path_updated = True
                            if dest == "end":
                                finished_paths += 1
                if not curr_path_updated:
                    path.append("stuck")
                    finished_paths += 1
    final_paths = 0
    for path in paths:
        if path[len(path) - 1] != "stuck":
            final_paths += 1
            print(path)
    print(final_paths)
