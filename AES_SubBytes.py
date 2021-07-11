from AES_Sbox import Sbox

sbox = Sbox()

class SubByte:
	def SubByte_Layer(self, x):
		y = b''
		for byte in x:
			sboxByte = sbox.AES_Sbox(byte)
			y += bytes([sboxByte])
		return y