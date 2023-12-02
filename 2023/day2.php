<?php

$example = explode("\n", file_get_contents("day2_example.txt"));
$input = explode("\n", file_get_contents("day2.txt"));

$bag_contents = [
    "red" => 12,
    "green" => 13,
    "blue" => 14,
];

echo calculate_possible_games($bag_contents, $example) . "\n";
echo calculate_possible_games($bag_contents, $input) . "\n";

function calculate_possible_games($bag_contents, $input_array) {
    $total_possible = 0;
    $total_cube_power = 0;
    for ($i=0; $i < count($input_array); $i++) {
        $game_is_possible = True;
        $game_record = explode(": ", $input_array[$i]);
        $game_id = intval(explode(" ", $game_record[0])[1]);
        // $game_record[1] = "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        $sets = explode("; ", $game_record[1]);
        $cubes_revealed = ["red" => 0, "green" => 0, "blue" => 0];
        $max_cubes_required = ["red" => 0, "green" => 0, "blue" => 0];

        // For each set, check the count of coloured cubes against the bag contents
        for ($n=0; $n < count($sets); $n++) {
            // $sets[0] = "3 blue, 4 red"
            $cubes = explode(", ", $sets[$n]);
            // $cubes = ["3 blue", "4 red"]
            for ($j=0; $j < count($cubes); $j++) {
                // $cubes[0] = "3 blue"
                $count = explode(" ", $cubes[$j])[0];
                $colour = explode(" ", $cubes[$j])[1];
                $cubes_revealed[$colour] = intval($count);
                if ($cubes_revealed[$colour] > $max_cubes_required[$colour]) {
                    $max_cubes_required[$colour] = $cubes_revealed[$colour];
                }
            }
            if ($bag_contents["red"] >= $cubes_revealed["red"] && $bag_contents["green"] >= $cubes_revealed["green"] && $bag_contents["blue"] >= $cubes_revealed["blue"]) {
                echo "Game " . $game_id . " is possible.\n";
            }
            else {
                // One of the sets is not possible so the whole game is not possible
                echo "Game " . $game_id . " is not possible.\n";
                $game_is_possible = False;
            }
        }
        echo implode(" ", $cubes_revealed) . "\n";
        echo implode(" ", $max_cubes_required) . "\n";
        $cube_power = array_product($max_cubes_required);

        if ($game_is_possible) {
            $total_possible+=$game_id;
        }
        $total_cube_power+=$cube_power;
    }

    return $total_possible . " " . $total_cube_power;
}