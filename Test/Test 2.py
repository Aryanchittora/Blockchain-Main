
for nonce in range(1, 35): # set a range for iteration
	equation = 25-5+nonce
	if equation == 29:
		print("Verified & The Nonce is", nonce) #display as "verified" and mention the nonce value at which it got verified. 
		break
	else:
		print('Not Verified & The Number is', nonce)#display as " not verified"





