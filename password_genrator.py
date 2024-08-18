import random
import string

def generate_password(length):
    if length < 1:
        print("Password length should be at least 1")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length < 1:
                print("Password length should be at least 1. Please try again.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")

def main():
    length = get_user_input()
    password = generate_password(length)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
