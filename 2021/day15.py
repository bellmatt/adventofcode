import heapq
from pathlib import PurePath
import sys


if __name__ == "__main__":
    risk_map = [
        list(
            int(x) + i + j if int(x) + i + j < 10 else int(x) + i + j - 9
            for i in range(5)
            for x in list(line.strip())
        )
        for j in range(5)
        for line in open(PurePath(sys.argv[0]).with_suffix('.txt'), "r").readlines()
    ]

    start_pos = (0, 0)
    count_of_steps = 0
    total_risk = 0
    finished = False
    visited_positions = {}

    priority_queue = []
    heapq.heappush(priority_queue, (total_risk, start_pos))
    while not finished:

        # Get the current shortest path from the queue
        (current_risk, curr_pos) = heapq.heappop(priority_queue)
        # Track the risk of getting to this position
        visited_positions[curr_pos] = current_risk

        if (
            curr_pos[0] < 0
            or curr_pos[1] < 0
            or curr_pos[0] >= len(risk_map)
            or curr_pos[1] >= len(risk_map[0])
        ):
            continue

        if curr_pos == (len(risk_map) - 1, len(risk_map[0]) - 1):
            finished = True
        # Consider neighbours up, down, left and right
        if curr_pos[0] > 0:
            # left
            if (curr_pos[0] - 1, curr_pos[1]) not in visited_positions:
                heapq.heappush(
                    priority_queue,
                    (
                        current_risk + risk_map[curr_pos[0] - 1][curr_pos[1]],
                        (curr_pos[0] - 1, curr_pos[1]),
                    ),
                )
            # right
        if curr_pos[0] < len(risk_map) - 1:
            if (curr_pos[0] + 1, curr_pos[1]) not in visited_positions:
                heapq.heappush(
                    priority_queue,
                    (
                        current_risk + risk_map[curr_pos[0] + 1][curr_pos[1]],
                        (curr_pos[0] + 1, curr_pos[1]),
                    ),
                )
            # up
        if curr_pos[1] > 0:
            if (curr_pos[0], curr_pos[1] - 1) not in visited_positions:
                heapq.heappush(
                    priority_queue,
                    (
                        current_risk + risk_map[curr_pos[0]][curr_pos[1] - 1],
                        (curr_pos[0], curr_pos[1] - 1),
                    ),
                )
            # down
        if curr_pos[1] < len(risk_map[0]) - 1:
            if (curr_pos[0], curr_pos[1] + 1) not in visited_positions:
                heapq.heappush(
                    priority_queue,
                    (
                        current_risk + risk_map[curr_pos[0]][curr_pos[1] + 1],
                        (curr_pos[0], curr_pos[1] + 1),
                    ),
                )

    print(current_risk)
