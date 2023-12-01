<?php

$example_array = explode("\n", file_get_contents("day1_example.txt"));
$array = explode("\n", file_get_contents("day1.txt"));

echo calculate_calibration_values($example_array) . "\n";
echo calculate_calibration_values($array) . "\n";


function calculate_calibration_values($array) {
    $total = 0;
    for ($i = 0; $i < count($array); $i++) {
        $inner_array = str_split($array[$i]);
        # Find first digit
        $first_digit = 0;
        $last_digit = 0;
        for ($j = 0; $j < count($inner_array); $j++) {
            if ($inner_array[$j] != '0') {
                $first_digit = intval($inner_array[$j]);
                if ($first_digit > 0) {
                    break;
                }
            }
            else {
                $first_digit = 0;
                break;
            }
        }
        # Find last digit
        for ($j = array_key_last($inner_array); $j >= 0; $j--) {
            if ($inner_array[$j] != '0') {
                $last_digit = intval($inner_array[$j]);
                if ($last_digit > 0) {
                    break;
                }
            }
            else {
                $last_digit = 0;
                break;
            }
        }
        $total += intval($first_digit . $last_digit);
        
    }
    return $total;
}