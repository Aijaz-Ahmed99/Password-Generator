# Random Password Generator
import random
import string

# Character set: letters, digits, punctuation
char_set = string.ascii_letters + string.digits + string.punctuation

try:
    user_length = int(input("Enter the password length (1 to 15): "))
    if 1 <= user_length <= 15:
        password = ''.join(random.choice(char_set) for _ in range(user_length))
        print("Your Random Password is:", password)
    else:
        print("Please enter a number between 1 and 15.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
