print("\n***  CAESAR CIPHER ENCRYPTION APP    ***\n")

start_char = ord('A')
end_char = ord('Z')
char_len = end_char - start_char + 1


def ciphar(message,shift):
    result = ""
    for letter in message.upper():
        if letter.isalpha():
            asci_char = ord(letter)             # letter --> assci code
            new_char = asci_char + shift        # adding assci code to shift key
            # to encrypt
            if new_char > end_char:
                new_char -= char_len            # if new char exceeds 'Z', wrap around to 'A'
            # to decrypt    
            if new_char < start_char:
                new_char += char_len            # if new char goes below 'A', wrap around to 'Z'
            result += chr(new_char)             # assci code --> new letter

        else:
            result += letter
    return result

print("1. Press e to encrypt\n2. Press d to decrypt\n3. Press q to quit")

while True:
    user_choice = input("\nChoose one operation: ")
    if user_choice.lower() == "q":
        print("See you later, user :)\n")
        quit()
    user_input = input("Enter the message: ")
    user_key = int(input("Enter the shift key: "))
    print(ciphar(user_input, user_key))
