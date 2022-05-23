import hashlib

with open('Test.png', 'rb') as f:
    file = f.read()

result = hashlib.sha256(file).hexdigest()
print(f'The Encrypted Image - {result}')