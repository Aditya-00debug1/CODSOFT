import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    
    letters = string.ascii_letters   
    digits = string.digits           
    symbols = string.punctuation     

    
    all_chars = letters + digits + symbols


    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


try:
    user_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(user_length)
    print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")