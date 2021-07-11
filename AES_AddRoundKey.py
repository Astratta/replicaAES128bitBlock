class AddRoundKey:
	def RoundKey(self, E, k):
		estado = b''
		for i in range(4):
			for j in range(4):
				estado[4 * i + j] = E[i][j]
		return estado ^ k

	def AddKey(self, e, k):
		return e ^ k
