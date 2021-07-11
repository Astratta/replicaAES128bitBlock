class ShiftRow:
	def gerar_matriz(self):
		m = []
		for i in range(4):
			linha = []
			for i in range(4):
				linha.append(0)
			m.append(linha)
		return m

	def transform_estado(self, x):
		mEstado = self.gerar_matriz()
		for linha in range(4):
			for col in range(4):
				mEstado[linha][col] = x[4 * linha + col]
		return mEstado

	def mostrar_estado(self, x):
		#estado = self.transform_estado(x)
		for i in range(4):
			for j in range(4):
				valor = bytes([x[i][j]])
				print(valor, end = ' ')
			print()

	def trocar_posicao(self, x):
		aux = x[0]
		for i in range(3):
			x[i] = x[i+1]
		x[3] = aux
		return x

	def ShiftRow_Layer(self, x):
		estado = self.transform_estado(x)
		for i in range(1, 4):
			for j in range(i):
				estado[i] = self.trocar_posicao(estado[i])
		return estado



