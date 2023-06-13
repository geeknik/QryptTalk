import os

def secure_delete(data):
    for _ in range(3):
        os.urandom(len(data))
    del data
