
fn is_increasing(row: &Vec<i32>) -> bool {
    if contains_duplicates(row) {
        return false;
    }
    let mut row_clone = row.clone();
    row_clone.sort();
    return *row == row_clone
}

fn contains_duplicates(row: &Vec<i32>) -> bool {
    let mut row = row.clone();
    row.sort();
    for i in 0..row.len()-1 {
        if row[i] == row[i+1] {
            return true;
        }
    }
    return false;
}

fn is_decreasing(row: &Vec<i32>) -> bool {
    if contains_duplicates(row) {
        return false;
    }
    let mut row_clone = row.clone();
    row_clone.sort();
    row_clone.reverse();
    return *row == row_clone
}

fn safe_diff_amount(row: &Vec<i32>) -> bool {
    let mut row = row.clone();
    row.sort();
    for i in 0..row.len()-1 {
        let diff = (row[i] - row[i+1]).abs();
        if diff > 3 {
            return false;
        }
    }
    return true;
}

fn is_safe(row: &Vec<i32>) -> bool {
    if (!is_decreasing(&row) && !is_increasing(&row)) || !safe_diff_amount(&row){
        println!("Unsafe level: {:?}", row);
        return false;
    }
    return true;
}

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
        if is_safe(&row) {
            safe_count += 1;
        }
        else {
            for i in 0..row.len() {
                // Remove the number at i, then check if the row is safe
                let mut row_clone = row.clone();
                row_clone.remove(i);
                if is_safe(&row_clone) {
                    safe_count += 1;
                    break;
                }
            }
        }
    }
    println!("Safe count: {}", safe_count);

}