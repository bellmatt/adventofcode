use regex::Regex;

fn calculate_mul(instruction: &str) -> i32 {
    let mut split = instruction.split(",");
    let x = split.next().unwrap().replace("mul(", "").parse::<i32>().unwrap();
    let y = split.next().unwrap().replace(")", "").parse::<i32>().unwrap();
    return x * y
}

fn main() {
    let input = include_str!("../input/day3_example.txt");
    let input = include_str!("../input/day3_input.txt");
    let re = Regex::new(r"mul\([0-9]*,[0-9]*\)").unwrap();
    let matches: Vec<_> = re.find_iter(input).map(|m| m.as_str()).collect();
    let mut sum = 0;
    for instruction in matches {
        calculate_mul(instruction);
    }
    println!("Sum: {}", sum);
    
    //let input = include_str!("../input/day3_example2.txt");
    let re_find_dont = Regex::new(r"don't\(\)").unwrap();
    let re_find_do = Regex::new(r"do\(\)").unwrap();
    let matches: Vec<&str> = re_find_dont.split(input).collect();
    let mut sum_part2 = 0;
    for (i, section) in matches.iter().enumerate() {
        if i == 0 {
            // Assume first one is enabled (unless the don't() is right at the start?)
            let got: Vec<_> = re.find_iter(section).map(|m| m.as_str()).collect();
            for instruction in got {
                sum_part2 += calculate_mul(instruction);
            }
        }
        else {
            // re-run the regex but look for do() to re-enable
            let got: Vec<&str> = re_find_do.split(section).collect();
            for (i, section) in got.iter().enumerate() {
                if i == 0 {
                    continue;
                }
                let found: Vec<_> = re.find_iter(section).map(|m| m.as_str()).collect();
                for instruction in found {
                    sum_part2 += calculate_mul(instruction);
                }
            }
        }
    }
    println!("Sum part 2: {}", sum_part2);
}