use regex::Regex;


fn main() {
    let input = include_str!("../input/day2_example.txt");
    let input = include_str!("../input/day2_input.txt");

    // Parse the input into a vector of vectors
    let v: Vec<_> = input
    .lines()
    .map(|line| line.split(" ").collect::<Vec<_>>())
    .collect::<Vec<_>>();

}