use std::fs::File;
use std::io::prelude::*;
use std::io::{self, BufReader};

// Converts numbers from word form to number value
fn get_value(str: &str) -> u32 {
    match str {
        "one" => return 1,
        "two" => return 2,
        "three" => return 3,
        "four" => return 4,
        "five" => return 5,
        "six" => return 6,
        "seven" => return 7,
        "eight" => return 8,
        "nine" => return 9,
        &_ => return 0,
    }
}

/*
    Gets first and last numbers to appear in a string. Does not include numbers
    as words (ie: one, two).
*/
fn find_first_last_number(str: &str) -> (usize, usize, u32, u32) {
    let possible_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

    let mut left_index = 0;
    let mut right_index = 0;
    let mut left_value = 0;
    let mut right_value = 0;
    let mut unset = true;

    for num in possible_numbers {
        let result = str.find(num);
        let right_result = str.rfind(num);

        if result.is_some() {
            let index = result.unwrap();
            let r_index = right_result.unwrap();

            if unset || left_index >= index {
                unset = false;
                left_index = index;
                left_value = num.to_digit(10).unwrap();
            }

            if right_index <= r_index {
                right_index = r_index;
                right_value = num.to_digit(10).unwrap();
            }
        }
    }

    return (left_index, right_index, left_value, right_value);
}

fn main() -> io::Result<()> {
    let file = File::open("src/input.txt")?;
    let reader = BufReader::new(file);
    let mut sum = 0;
    let possible_checks = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];

    for line in reader.lines() {
        let unwrapper = line.unwrap();
        let (mut index_left, mut index_right, mut left_value, mut right_value) =
            find_first_last_number(&unwrapper);

        for word in possible_checks {
            let result = unwrapper.find(word);
            let right_result = unwrapper.rfind(word);

            if !result.is_none() {
                let index = result.unwrap();
                let idx_right = right_result.unwrap();

                if index <= index_left {
                    left_value = get_value(word);
                    index_left = index;
                }
                if idx_right >= index_right {
                    right_value = get_value(word);
                    index_right = idx_right;
                }
            }
        }

        sum += format!("{}{}", left_value, right_value)
            .parse::<i32>()
            .unwrap();
    }

    println!("{sum}");
    Ok(())
}
