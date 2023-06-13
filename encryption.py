import nacl.utils
from nacl.public import PrivateKey, Box

def generate_ephemeral_key_pair():
    return PrivateKey.generate(), PrivateKey.generate().public_key

def encrypt_message(message, their_public_key, my_private_key):
    ephemeral_private_key, ephemeral_public_key = generate_ephemeral_key_pair()
    box = Box(ephemeral_private_key, their_public_key)
    encrypted_message = box.encrypt(message.encode())
    return encrypted_message, ephemeral_public_key

def decrypt_message(encrypted_message, their_public_key, my_private_key):
    box = Box(my_private_key, their_public_key)
    message = box.decrypt(encrypted_message).decode()
    return message
