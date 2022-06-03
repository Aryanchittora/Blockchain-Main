import hashlib

PB_current_hash = "573de6af99199bdc7ae9534891d512afbc2b1473f2f6a5784e0c078d67a60bf9"
text = 'Alice sends James 5 Eth amount'

current_hash = hashlib.sha256(text.encode()).hexdigest()

if PB_current_hash == current_hash:
    print('Verified!')
else:
    print('Failed!')