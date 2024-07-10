import random
import string

def generate_password(length):
    # Define the character sets to use in generating the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
