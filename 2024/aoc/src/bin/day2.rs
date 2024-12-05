
fn main() {
    let input = include_str!("../input/day2_example.txt");
    let input = include_str!("../input/day2_input.txt");

    // Parse the input into a vector of vectors
    let v: Vec<_> = input
    .lines()
    .map(|line| line.split(" ").collect::<Vec<_>>())
    .collect::<Vec<_>>();

    // transform the vector of vectors into a vector of integers
    let levels = v.iter().map(|row| {
        row.iter().map(|level| level.parse::<i32>().unwrap()).collect::<Vec<i32>>()
    }).collect::<Vec<Vec<i32>>>();

    let mut safe_count = 0;
    for row in levels {
        let mut safe = true;
        let mut increasing = true;
        let mut decreasing = true;
        for (i, level) in row.clone().into_iter().enumerate() {
            if (increasing || decreasing || safe) && i > 0 {
                if level <= row[i-1] {
                    increasing = false;
                }
                if level >= row[i-1] {
                    decreasing = false;
                }
                if !increasing && !decreasing {
                    safe = false;
                }
                let diff = (level - row[i-1]).abs();
                if diff <= 0 || diff > 3 {
                    safe = false;
                }
            }
            if i == row.len()-1 {
                if (increasing || decreasing) && safe == true{
                    safe_count += 1;
                }
            }
        }
    }
    println!("Safe count: {}", safe_count);

}