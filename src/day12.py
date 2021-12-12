from typing import List, Tuple


def is_small_cave(input: str) -> bool:
    return not input.isupper() and input not in ("start", "end")


def find_next_route_options(curr_pos: str, input: List[Tuple[str, str]]) -> List[str]:
    options = []
    for route in input:
        if route[0] == curr_pos:
            options.append(route[1])
        elif route[1] == curr_pos and route[0] not in ("start", "end"):
            options.append(route[0])
    return options


if __name__ == "__main__":
    cave_system = [
        tuple(line.rstrip().split("-"))
        for line in open("./src/day12_testinput.txt", "r").readlines()
    ]
    curr_pos = "start"
    paths = [["start"]]
    finished_paths = 0
    while finished_paths < len(paths):
        for path in paths:
            path_copy = path.copy()
            current_loc = path[len(path) - 1]
            if "end" not in path and "stuck" not in path:
                curr_path_updated = False
                # Find the possible routes from last entry in the path
                options = find_next_route_options(current_loc, cave_system)
                for dest in options:
                    if not curr_path_updated:
                        if is_small_cave(dest) and path.count(dest) < 1:
                            # Small cave not visited before in this path
                            path.append(dest)
                            curr_path_updated = True
                        elif dest.isupper() or dest == "end":
                            path.append(dest)
                            curr_path_updated = True
                            if dest == "end":
                                finished_paths += 1
                    else:
                        # Create new path
                        if (
                            (is_small_cave(dest) and dest not in path_copy)
                            or dest.isupper()
                            or dest == "end"
                        ) and (path_copy + [dest]) not in paths:
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
