phone = input("Insert you phone number: ")

digits = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "tree",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

for dig in phone:
    print(digits[dig], end=" ")