# Caesar Cipher program
# Name: Aasim Khan
# Student ID: 2407702

def welcome():
    """function to display welcome message"""
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    """to ask user if to encrypt or decrypt"""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else 'decrypt')).upper()
        shift_key = input("What is the shift number: ")

        if not shift_key.isdigit():
            print("Invalid Shift input. Please enter a numeric value.")
        elif not 0 <= int(shift_key) <= 25:
            print("Invalid Shift. Please enter a value between 0 and 25.")
        else:
            break

    return mode, message, int(shift_key)


def encrypt(message, shift_key):
    """function to encrypt the given input"""
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - base + shift_key) % 26 + base)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message, shift_key):
    """function to decrypt the given input"""
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_message += chr((ord(char) - base - shift_key) % 26 + base)
        else:
            decrypted_message += char
    return decrypted_message


def is_file(file_name):
    """error handling to check if filename is valid or not"""
    try:
        open(file_name, 'r')
        return True
    except FileNotFoundError:
        return False


def write_messages(messages):
    """function that creates new file for the output of the encrypted or decrypted text"""
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message.upper() + '\n')
    print("Output written to results.txt")


def process_file(file_name, mode):
    """function if user chooses to enter filename for the program"""
    messages = []
    while True:
        try:
            shift_key = int(input("What is the shift number: "))
            if 0 <= shift_key <= 25:
                break
            else:
                print("Invalid Shift. Please enter a value between 0 and 25.")
        except ValueError:
            print("Invalid Shift input. Please enter a numeric value.")

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            messages.append(encrypt(line, shift_key) if mode == 'e' else decrypt(line, shift_key))
    write_messages(messages)


def message_or_file():
    """ function to ask user to encrypt or decrypt the text and to give the output from file or the console"""
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Source")

    if source == 'f':
        while True:
            file_name = input("Enter a filename: ")
            if is_file(file_name):
                break
            else:
                print("Invalid Filename")

        return mode, None, file_name
    else:
        message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else 'decrypt')).upper()
        return mode, message, None


def main():
    """in this function all the function like welcome function, messsage or file function, process file function, encrypt function and decrypt function are used to run the program."""
    welcome()
    while True:
        mode, message, file_name = message_or_file()

        if file_name:
            messages = process_file(file_name, mode)
        else:
            while True:
                try:
                    shift_key = int(input("What is the shift number: "))
                    if 0 <= shift_key <= 25:
                        break
                    else:
                        print("Invalid Shift. Please enter a value between 0 and 25.")
                except ValueError:
                    print("Invalid Shift input. Please enter a numeric value.")

            messages = [encrypt(message, shift_key)] if mode == 'e' else [decrypt(message, shift_key)]

            print('\n'.join(messages).upper())

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message != 'y':
            print("Thanks for using the program, goodbye!")
            break

main()