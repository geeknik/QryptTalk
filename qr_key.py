import oqs

def generate_qr_key_pair():
    k = oqs.KeyEncapsulation('Kyber512')
    public_key = k.public_key
    secret_key = k.secret_key
    return public_key, secret_key
