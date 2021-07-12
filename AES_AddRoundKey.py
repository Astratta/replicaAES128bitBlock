class AddRoundKey:
	def RoundKey(self, E, k):
		estado = []
		for i in range(4):
			for j in range(4):
				estado.append(E[i][j])
		e = b''
		for i in range(16):
			e += bytes([estado[i] ^ k[i]])
		return e

	def AddKey(self, e, k):
		estado = []
		for i in range(16):
			estado.append(e[i])
		e = b''
		for i in range(16):
			e += bytes([estado[i] ^ k[i]])
		return e
