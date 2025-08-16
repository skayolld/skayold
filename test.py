import hashlib

word = "mohammed"
hashed = hashlib.sha3_256(word.encode()).hexdigest()
print (hashed)