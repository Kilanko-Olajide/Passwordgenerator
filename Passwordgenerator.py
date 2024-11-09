import random
import string

def generate_a_password(minimum_length, numberinside = True, characterinside = True):
    letters = string.ascii_letters
    characters = string.punctuation
    digit = string.digits

    password_generator = letters
    if numberinside:
        password_generator += digit
    if characterinside:
        password_generator += characters
    
    password = ""

    meets_criteria = False
    has_number = False
    has_character = False

    while not meets_criteria and len(password) < minimum_length:
        single_character = random.choice(password_generator)
        password += single_character
        if single_character in digit:
            has_number = True
        if single_character in characters:
            has_character = True


            
            if numberinside:
                meets_criteria = True
                meets_criteria = has_number
            if characterinside:
                meets_criteria = meets_criteria and has_character
    return password

number = input("Do you want a number: ") == "yes"
character = input("Do you want a character: ") == "yes"

password = generate_a_password(10)
print(password)
