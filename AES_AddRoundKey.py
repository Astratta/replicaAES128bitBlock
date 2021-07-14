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

	def gerar_matriz(self):
		m = []
		for i in range(4):
			linha = []
			for i in range(4):
				linha.append(0)
			m.append(linha)
		return m

	def Inv_RoundKey(self, e, k):
		mEstado = self.gerar_matriz()
		for i in range(4):
			for j in range(4):
				mEstado[i][j] = e[4 * i + j] ^ k[4 * i + j]
		return mEstado
