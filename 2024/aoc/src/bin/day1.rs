

fn main() {
    let input = include_str!("../input/day1_example.txt");
    //let input = include_str!("../input/day1_input.txt");

    // Parse the input into a vector of vectors
    let v: Vec<_> = input
    .lines()
    .map(|line| line.split("   ").collect::<Vec<_>>())
    .collect::<Vec<_>>();

    // Transpose the vectors 
    // - is there an easier way to do this for a vector of vectors?)
    // - is this possible to do as part of parsing the input above?
    let rows = v.len();
    let cols = v[0].len();
    let transposed: Vec<Vec<_>> = (0..cols).map(|col| {
        (0..rows)
            .map(|row| v[row][col].parse::<i32>().unwrap())
            .collect()
    }).collect();

    // Sort the vectors
    // - again feels like sort could happen above
    let sorted = transposed.iter().map(|row| {
        let mut row = row.clone();
        row.sort();
        row
    }).collect::<Vec<_>>();

    // Find the differences between each item in the sorted vectors
    let mut sum_differences = 0;
    for i in 0..sorted.len()-1 {
        for j in 0..sorted[i].len() {
            let diff = sorted[i][j] - sorted[i+1][j];
            sum_differences += diff.abs();
        }
    }
    println!("{:?}", sum_differences);
}
