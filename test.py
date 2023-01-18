from cryptography.fernet import Fernet

cipher = Fernet(b'LXcJ0NlNh9hPlNDkTfy1DKLh0BYJxElfuDJ7xnm2RW8=')

encoded_text = cipher.encrypt('heello'.encode())
decoded_text = cipher.decrypt(encoded_text)

print(decoded_text.decode())
