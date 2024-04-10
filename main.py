import re

def validate_credit_card(card_number):
    # Define the regex pattern for a valid credit card number
    pattern = r'^[4-6]\d{3}(-?\d{4}){3}$'

    # Check if the card number matches the pattern
    if re.match(pattern, card_number):
        # Remove hyphens from the card number
        card_number = card_number.replace('-', '')

        # Check if there are no consecutive repeated digits
        for i in range(len(card_number) - 3):
            if card_number[i] == card_number[i+1] == card_number[i+2] == card_number[i+3]:
                return False
        
        return True
    else:
        return False

# Example usage
card_numbers = [
    "4253625879615786",
    "4424424424442444",
    "5122-2368-7954-3214",
    "42536258796157867",
    "4424444424442444",
    "5122-2368-7954 - 3214",
    "44244x4424442444 ",
    "0525362587961578",
    
]

for card_number in card_numbers:
    if validate_credit_card(card_number):
        print(f"{card_number} is valid")
    else:
        print(f"{card_number} is not valid")
