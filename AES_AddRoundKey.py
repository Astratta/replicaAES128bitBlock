class AddRoundKey:
	def RoundKey(self, E, k):
		estado = b''
		for i in range(4):
			for j in range(4):
				estado += bytes([E[i][j] ^ k[4 * i + j]])
		return estado

	def AddKey(self, e, k):
		estado = b''
		for i in range(16):
			estado += bytes([e[i] ^ k[i]])
		return estado
