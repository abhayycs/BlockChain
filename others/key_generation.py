from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
# ARGUMENTS: 1) KEY_LENGTH, 2) RANDOM NUMBER GENERATOR
key = RSA.generate(1024, random_generator)

print('key:\t',key)
# WRITE DOWN PUBLIC AND PRIVATE KEY IN A FILE
with open('mykey.pem','wb') as file:
	file.write(key.exportKey('PEM')) 	# private key
	file.write(b"\n")					# new line in binary form
	file.write(key.publickey().exportKey('PEM'))

# PUBLIC KEY
#Public Key can be changed after each transaction
print('public key:\t',key.publickey().exportKey('PEM'))
# A matching RSA public key.
public_key = key.publickey()

# Size of the RSA modulus in bits
# print("Size of key:\t", key.size_in_bits())
# The minimal amount of bytes that can hold the RSA modulus.
# print("Size:\t", key.size_in_bytes())

print("key.can_encrypt",key.can_encrypt())
print("key.can_sign",key.can_sign())
#  Whether this is an RSA private key
print("key.has_private",key.has_private())

enc_data = public_key.encrypt('This is great!', 32)
print("Encrypted data is : ",enc_data)
print("Decrypted data is ",key.decrypt(enc_data))

