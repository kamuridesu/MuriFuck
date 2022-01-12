#[allow(non_snake_case)]
use std::io::{self, Write};
// use std::env;

fn generate(text: String) -> String {
    let mut string = Vec::new();
    for chr in text.chars() {
        string.push(chr as u32);
    }
    let mut increase = String::new();
    for chr in string.iter() {
        for _ in 0..*chr {
            increase += "+";
        }
        increase += "\n";
        increase += ">";
    }
    increase += "\n";
    for _ in string.iter() {
        increase += "<";
    }
    increase += "\n";
    for _ in string.iter() {
        increase += ". >";
    }
    return increase
}

fn interpreter(text: &str) {
    let mut tape = Vec::new();
    let mut pointer = 0;
    // populate tape with 0s with 30 cells
    for _ in 0..30 {
        tape.push(0);
    }

    let content = text.split("");
    for chr in content {
        match chr {
            "+" => {
                tape[pointer] += 1;
            }
            "-" => {
                tape[pointer] -= 1;
            }
            ">" => {
                pointer += 1;
            }
            "<" => {
                pointer -= 1;
            }
            "." => {
                print!("{}", tape[pointer] as u8 as char);
            }
            "," => {
                let mut input = String::new();
                io::stdin().read_line(&mut input).unwrap();
                tape[pointer] = input.trim().parse::<u32>().unwrap();
            }
            _ => {}
        }
    }
}

fn input(text: &str) -> String {
    print!("{}", text);
    let _ = io::stdout().flush();
    let mut user_input = String::new();
    io::stdin().read_line(&mut user_input).expect("fail");
    return user_input;

}

fn main() {
    let text = input("Digite algo: ");
    let bf_code = generate(text);
    println!("{}", bf_code);
    interpreter(&bf_code);
    // let args: Vec<String> = env::args().collect();
    // println!("{:?}", args);
}

