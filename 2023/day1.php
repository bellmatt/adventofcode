<?php

$example_array = explode("\n", file_get_contents("day1_example.txt"));
$example_array_part2 = explode("\n", file_get_contents("day1_example_2.txt"));
$array = explode("\n", file_get_contents("day1.txt"));

echo calculate_calibration_values_ints($example_array) . "\n";
echo calculate_calibration_values_ints($array) . "\n";

function calculate_calibration_values_ints($array) {
    $total = 0;
    for ($i = 0; $i < count($array); $i++) {
        $inner_array = str_split($array[$i]);
        $total += intval(get_first_digit($inner_array) . get_last_digit($inner_array));
    }
    return $total;
}

function get_first_digit($array) {
    $numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    $first_digit = 0;
    for ($i = 0; $i < count($array); $i++) {
        if ($array[$i] != '0') {
            $first_digit = intval($array[$i]);
            if ($first_digit > 0) {
                return $first_digit;
            }
        }
        else {
            $first_digit = 0;
            return $first_digit;
        }
        for ($n = 0; $n < count($numbers); $n++) {
            //echo "Checking " . $numbers[$n] . " against " . implode(array_slice($array, $i, 5)) . "\n";
            if (str_starts_with(implode(array_slice($array,$i)), $numbers[$n])) {
                //echo "Found first digit: " . $numbers[$n] . "\n";
                return $n + 1;
            }
        }
    }
    return $first_digit;
}

function get_last_digit($array) {
    $numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    $last_digit = 0;
    for ($i = array_key_last($array); $i >= 0; $i--) {
        if ($array[$i] != '0') {
            $last_digit = intval($array[$i]);
            if ($last_digit > 0) {
                return $last_digit;
            }
        }
        else {
            $last_digit = 0;
            return $last_digit;
        }
        for ($n = 0; $n < count($numbers); $n++) {
            //echo "Checking " . $numbers[$n] . " against " . implode(array_slice($array,$i)) . "\n";
            if (str_starts_with(implode(array_slice($array, $i)), $numbers[$n])) {
                //echo "Found last digit: " . $numbers[$n] . "\n";
                return $n + 1;
            }
        }
    }
    return $last_digit;
}
