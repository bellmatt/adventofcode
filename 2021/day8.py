from pathlib import PurePath
import sys

if __name__ == "__main__":
    input = open(PurePath(sys.argv[0]).with_suffix('.txt'), "r").readlines()

    # Part 1
    count_1 = 0
    count_4 = 0
    count_7 = 0
    count_8 = 0
    for line in input:
        for output_value in line.split("|")[1].split():
            if len(output_value) == 2:
                count_1 += 1
            elif len(output_value) == 4:
                count_4 += 1
            elif len(output_value) == 3:
                count_7 += 1
            elif len(output_value) == 7:
                count_8 += 1

    print(count_1 + count_4 + count_7 + count_8)

    # Part 2
    # example = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    output_sum = 0
    for line in input:
        digit_mapping = [""] * 10
        while any(digit_mapping[x] == "" for x in range(10)):
            for signal in line.split("|")[0].split():
                if len(signal) == 2:
                    digit_mapping[1] = signal
                elif len(signal) == 4:
                    digit_mapping[4] = signal
                elif len(signal) == 3:
                    digit_mapping[7] = signal
                elif len(signal) == 7:
                    digit_mapping[8] = signal
                # 6 is the only digit with 6 segments that does not contain all 3 segments from 7
                # if 7 in digit_mapping: print(list(digit_mapping[7]))
                if (
                    len(signal) == 6
                    and len(digit_mapping[7]) > 0
                    and not all(x in signal for x in list(digit_mapping[7]))
                ):
                    digit_mapping[6] = signal
                # 3 is the only remaining digit that has all of the segments from 1
                elif (
                    len(signal) == 5
                    and len(digit_mapping[1]) > 0
                    and all(x in signal for x in list(digit_mapping[1]))
                ):
                    digit_mapping[3] = signal
                # 5 is the only digit where all its segments are contained in 6
                elif (
                    len(signal) == 5
                    and len(digit_mapping[6]) > 0
                    and all(x in digit_mapping[6] for x in list(signal))
                ):
                    digit_mapping[5] = signal
                # 2 is the only remaining digit with 5 segments (now that we have 3 and 5)
                elif (
                    len(signal) == 5
                    and len(digit_mapping[5]) > 0
                    and len(digit_mapping[3]) > 0
                ):
                    digit_mapping[2] = signal
                # 9 has all the digits from 4
                elif (
                    len(signal) == 6
                    and len(digit_mapping[4]) > 0
                    and all(x in signal for x in list(digit_mapping[4]))
                ):
                    digit_mapping[9] = signal
                # last one is 0
                elif len(signal) == 6:
                    digit_mapping[0] = signal
        output_value = ""
        for output_value_segment in line.split("|")[1].strip().split(" "):
            for i, pattern in enumerate(digit_mapping):
                if len(pattern) == len(output_value_segment) and all(
                    x in pattern for x in list(output_value_segment)
                ):
                    output_value += str(i)
        output_sum += int(output_value)
    print(f"output: {output_sum}")
