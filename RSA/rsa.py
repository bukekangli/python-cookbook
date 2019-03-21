from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash.SHA256 import SHA256Hash
from base64 import b64decode, b64encode

public_key_local = '/Users/shanglikang/.ssh/id_rsa.pub'
private_key_local = '/Users/shanglikang/.ssh/id_rsa'


def create_sign(private_key_loc, data):
    with open(private_key_loc, 'r') as f:
        rsa_private_key = RSA.importKey(f.read())
    digist = SHA256Hash(data.encode())
    signer = PKCS1_v1_5.new(rsa_private_key)
    bin_sign = signer.sign(digist)
    return b64encode(bin_sign)


def verify_sign(public_key_loc, signature, data):
    '''
    Verifies with a public key from whom the data came that it was indeed
    signed by their private key
    param: public_key_loc Path to public key
    param: signature String signature to be verified
    return: Boolean. True if the signature is valid; False otherwise.
    '''
    pub_key = open(public_key_loc, "r").read()
    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256Hash(data.encode())
    # Assumes the data is base64 encoded to begin with
    if signer.verify(digest, b64decode(signature)):
        return True
    return False


if __name__ == '__main__':
    data = 'slk'
    sign = create_sign(private_key_local, data)
    print(sign)
    print(verify_sign(public_key_local, sign, data))