from AES_SubBytes import SubByte

subByte = SubByte()

rCon = [[1, 2, 4, 8, 16, 32, 64, 128, 27, 54],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

class KeySchedule:

	def gerar_matriz(self):
		m = []
		for i in range(4):
			linha = []
			for i in range(4):
				linha.append(0)
			m.append(linha)
		return m

	def rotword(self, x):
		aux = x[0]
		for i in range(3):
			x[i] = x[i+1]
		x[3] = aux
		return x

	def pegar_coluna(self, x, coluna):
		z = []
		for i in range(4):
			z.append(x[i][coluna])
		return z

	def subbyte(self, x):
		y = b''
		for byte in x:
			y += bytes([byte])
		y = subByte.SubByte_Layer(y)
		for i in range(4):
			x[i] = y[i]
		return x

	def calc_primeira_coluna(self, K, KR, Rcon):
		K_last_Column = self.pegar_coluna(K, 3)
		K_last_Column = self.rotword(K_last_Column)
		K_last_Column = self.subbyte(K_last_Column)

		for i in range(4):
			KR[i][0] = K_last_Column[i] ^ K[i][0] ^ Rcon[i]
		return KR

	def calc_demais_colunas(self, K, KR):
		for col in range(1, 4):
			for lin in range(4):
				KR[lin][col] = KR[lin][col-1] ^ K[lin][col]
		return KR

	def transform_Key(self, K):
		mKey = self.gerar_matriz()
		for i in range(4):
			for j in range(4):
				mKey[i][j] = K[4 * i + j]
		return mKey


	def Key_Expansion(self, K, r):
		Key = self.transform_Key(K)
		KR = self.gerar_matriz()
		KR = self.calc_primeira_coluna(Key, KR, self.pegar_coluna(rCon, r))
		KR = self.calc_demais_colunas(Key, KR)
		keyRound = b''
		for i in range(4):
			for j in range(4):
				keyRound += bytes([KR[i][j]])
		return keyRound



