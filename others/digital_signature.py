from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA 
from Crypto import Random

random_generator = Random.new().read

key = RSA.generate(1024,random_generator)
# key = RSA.generate(1024)

pk = key.publickey()

plainText = "hello World!"
hashA = SHA256.new(plainText).digest()

DigSig = key.sign(hashA, "")


print("HAS A:" + repr(hashA) + "\n")
print("Digital Signature: " + repr(DigSig) + "\n")


plainText = "hell World!"
hashB = SHA256.new(plainText).digest()
print("HAS B:" + repr(hashB) + "\n")

if(pk.verify(hashB, DigSig)):
	print("match")
else:
	print("no")