from hashlib import sha256

logo  = "     ____  ___)                       \n"
logo += "    (, /   /         /)               \n"
logo += "      /---/  _   _  (/  _    _ _   __ \n"
logo += "   ) /   (__(_(_/_)_/ )_(_(_/ (_(_/ (_\n"
logo += "  (_/                                 \n"

b58check = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

# http://rosettacode.org/wiki/Bitcoin/address_validation#Python
def decodeBase58(bc, length):
	n = 0
	for char in bc:
		n = n * 58 + b58check.index(char)
	return n.to_bytes(length, 'big')

def checkAddr(bc):
	try:
		bcb = decodeBase58(bc, 25)
		return bcb[-4:] == sha256(sha256(bcb[:-4]).digest()).digest()[:4]
	except Exception:
		return False