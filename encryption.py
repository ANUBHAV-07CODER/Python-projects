def encrypt(message, key):
    encrypted = ""

    for char in message:
        encrypted += chr(ord(char) + key)
    return encrypted


def decrypt(message, key):
    decrypted = ""

    for char in message:
        decrypted += chr(ord(char) - key)
    return decrypted

message = input("Enter your message: ")
key = int(input("Enter your key: "))

encrypted_message = encrypt(message, key)
print("\nEncrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)