from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA 
from Crypto import Random

random_generator = Random.new().read

key = RSA.generate(1024,random_generator)
# key = RSA.generate(1024)

pk = key.publickey()

def hashA(plainText):
    return SHA256.new(plainText).digest()
def DigSig(hashA):
    return key.sign(hashA, "")

def hashB(plainText):
    return SHA256.new(plainText).digest()

hashA = hashA("hello World!")
print(repr(hashA))
Signature = DigSig(hashA)
print("Digital Signatgure :" + repr(Signature) + "\n")
hashB = hashB("hello World!")
print("\n" + repr(hashB))
if(pk.verify(hashB, Signature)):
    print("match")
else:
    print(" Not match")