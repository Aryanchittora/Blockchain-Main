import hashlib

txt = 'Hello World!'
result = hashlib.sha3_256(txt.encode())
print('The Hash Code -', result.hexdigest())

txt1 = 'He gave me Rs 100'
result = hashlib.sha3_256(txt1.encode())
print('The Hash Code of Txt1 -', result.hexdigest())

txt2 = 'I gave him Rs 200'
result = hashlib.sha3_256(txt2.encode())
print('The Hash Code of Txt2 -', result.hexdigest())

txt3 = 'She gave him Rs 200 on 25th April, 2022'
result = hashlib.sha3_256(txt3.encode())
print('The Hash Code of Txt3 -', result.hexdigest())

txt4 = 'She gave him Rs 200 on 26th April, 2022'
result = hashlib.sha3_256(txt4.encode())
print('The Hash Code of Txt4exit -', result.hexdigest())