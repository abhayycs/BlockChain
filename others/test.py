from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto import Random


def compute_hash(plain_text):
	return SHA256.new(plain_text).digest()

def digital_sign(hash_value, key):
	hash_salt = " "
	return key.sign(hash_value, hash_salt)

def key_generate(key, key_length=1024, random_generator=True):
    # ARGUMENTS: 1) KEY 2) KEY_LENGTH, 3) RANDOM NUMBER GENERATOR
	if random_generator:
		from Crypto import Random
	    random_generator = Random.new().read
    	key = RSA.generate(key_length, random_generator)
    else:
    	key = RSA.generate(key_length)
    return key

def store_keys(key, path='mykey.pem'):
	STORE_TYPE = 'PEM'
	with open(path,'wb') as file:
	    file.write(key.exportKey(STORE_TYPE))    # private key
	    file.write(b"\n")                   # new line in binary form
	    file.write(key.publickey().exportKey(STORE_TYPE))
