from typing import List, Tuple
from statistics import median


def syntax_checker_find_corrupted(input: List[str]) -> Tuple[str, str]:
    open_chars = ["[", "(", "{", "<"]
    char_map = {"[": "]", "(": ")", "{": "}", "<": ">"}
    open_queue = []
    invalid_char_scores = {"": 0, ")": 3, "]": 57, "}": 1197, ">": 25137}
    for char in input:
        if char in open_chars:
            open_queue.append(char)
        else:
            last_open = open_queue.pop()
            if char != char_map[last_open]:
                print(f"expected {char_map[last_open]}, got {char}")
                return ("corrupted", invalid_char_scores[char])
    completion_chars = list(char_map[x] for x in reversed(open_queue))
    score = 0
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}
    for i in range(len(completion_chars)):
        score = (score * 5) + score_map[completion_chars[i]]
    return ("incomplete", score)


if __name__ == "__main__":
    navigation_subsystem = [
        list(line.strip()) for line in open("./src/day10_input.txt", "r").readlines()
    ]
    sum_corrupted_scores = 0
    incomplete_scores = []
    for line in navigation_subsystem:
        status, score = syntax_checker_find_corrupted(line)
        if status == "corrupted":
            sum_corrupted_scores += score
        elif status == "incomplete":
            incomplete_scores.append(score)

    print(f"Part 1: {sum_corrupted_scores}")
    print(f"Part 2: {median(sorted(incomplete_scores))} from {len(incomplete_scores)}")
