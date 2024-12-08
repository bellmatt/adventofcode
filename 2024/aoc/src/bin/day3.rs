use regex::Regex;


fn main() {
    let input = include_str!("../input/day3_example.txt");
    let input = include_str!("../input/day3_input.txt");
    let re = Regex::new(r"mul\([0-9]*,[0-9]*\)").unwrap();
    let matches: Vec<_> = re.find_iter(input).map(|m| m.as_str()).collect();
    let mut sum = 0;
    for instruction in matches {
        let mut split = instruction.split(",");
        let x = split.next().unwrap().replace("mul(", "").parse::<i32>().unwrap();
        let y = split.next().unwrap().replace(")", "").parse::<i32>().unwrap();
        sum += x * y;
    }
    println!("Sum: {}", sum);
    
}