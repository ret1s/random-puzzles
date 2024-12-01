pub fn main() {
    let gift_message = String::from("Merry Christmas! Enjoy your gift!");
    let result = attach_message_to_present(&gift_message);

    println!("{}", result);
    println!("{}", gift_message)
}

pub fn attach_message_to_present(message: &String) -> String {
    format!("The present now has this message: {}", message)
}
