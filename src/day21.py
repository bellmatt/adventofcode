from itertools import cycle


if __name__ == "__main__":
    # Input
    positions = [7, 8]
    # Test input
    # positions = [4,8]

    # Part 1: Deterministic dice
    numbers = cycle(list(range(1, 101, 1)))
    scores = [0, 0]
    turn = 0
    while True:
        print(turn)
        for p in range(len(positions)):
            sum_rolls = 0
            for _ in range(3):
                roll = numbers.__next__()
                sum_rolls += roll
            positions[p] = (
                (positions[p] + sum_rolls) % 10
                if ((positions[p] + sum_rolls) % 10 != 0)
                else 10
            )
            scores[p] += positions[p]
            if scores[p] >= 1000:
                break
        if scores[p] >= 1000:
            break
        turn += 1
    losing_score = scores[(p + 1) % 2]
    dice_rolls = turn * 2 * 3 + (3 if p == 0 else 0)
    print(
        f"After {turn} turns, player {((p+1)%2) + 1} loses, score: {losing_score}. Dice rolls = {dice_rolls}. Result = {losing_score*dice_rolls}"
    )
