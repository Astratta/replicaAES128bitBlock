from AES_Sbox import Sbox

gf = Sbox()

class MixColumn:
	def gerar_matriz(self):
		m = []
		for i in range(4):
			linha = []
			for i in range(4):
				linha.append(0)
			m.append(linha)
		return m

	def produto_escalar(self, x, y):
		z = 0
		for i in range(4):
			z ^= gf.AES_field_mult(x[i], y[i])
		return z

	def pegar_coluna(self, x, coluna):
		z = []
		for i in range(4):
			z.append(x[i][coluna])
		return z

	def matriz_mult(self, X, estado):
		z = self.gerar_matriz()
		for i in range(4):
			for j in range(4):
				z[i][j] = self.produto_escalar(X[i], self.pegar_coluna(estado, j))
		return z

	def MixColumn_Layer(self, estado):
		X = [[2, 3, 1, 1], 
			 [1, 2, 3, 1], 
			 [1, 1, 2, 3], 
			 [3, 1, 1, 2]]
		return self.matriz_mult(X, estado)

	def Inv_MixColumn_Layer(self, estado):
		X = [[14, 11, 13, 9],
			 [9, 14, 11, 13],
			 [13, 9, 14, 11],
			 [11, 13, 9, 14]]
		return self.matriz_mult(X, estado)



