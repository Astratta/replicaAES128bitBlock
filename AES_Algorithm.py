from AES_SubBytes import SubByte
from AES_ShiftRows import ShiftRow
from AES_MixColumn import MixColumn
from AES_Key_Schedule import KeySchedule
from AES_AddRoundKey import AddRoundKey

SubByteLayer = SubByte()
ShiftRowLayer = ShiftRow()
MixColumnLayer = MixColumn()
KeyExpansion = KeySchedule()
AddRoundKey = AddRoundKey()

dados_bytes = open("Arquivo editado.txt", "rb")
dadosCompleto = dados_bytes.read()

chave_bytes = open("chave.txt", "rb")
chave = chave_bytes.read()

###################################Lendo arquivos para as operações########################################

dados = b'' #Variável de leitura, com ela montamos o Estado do AES

#Calcular as chavez de cada round
chaveRound = []
for i in range(10):
	if i == 0:
		chaveRound.append(KeyExpansion.Key_Expansion(chave, i))
	else:
		chaveRound.append(KeyExpansion.Key_Expansion(chaveRound[i-1], i))

while True:
	resp = input("Encriptar ou decriptar? (E) ou (D)")

	if resp.upper() == "E":
		#Encriptar
		textoCifrado = b''

		while True:
			if len(dadosCompleto) % 16 == 0:
				break
			else:
				dadosCompleto += b' '

		for byte in range(len(dadosCompleto)):
			dados += bytes([dadosCompleto[byte]]) #Lendo um bloco para decriptar
			if len(dados) == 16:
				#Adicionar chave antes do round 1
				estado = AddRoundKey.AddKey(dados, chave)

				#Os rounds se iniciam
				for r in range(10):
					if r != 9:
						estado = SubByteLayer.SubByte_Layer(estado)
						mEstado = ShiftRowLayer.ShiftRow_Layer(estado)
						mEstado = MixColumnLayer.MixColumn_Layer(mEstado)
						estado = AddRoundKey.RoundKey(mEstado, chaveRound[r])
					else:
						estado = SubByteLayer.SubByte_Layer(estado)
						mEstado = ShiftRowLayer.ShiftRow_Layer(estado)
						estado = AddRoundKey.RoundKey(mEstado, chaveRound[r])

				textoCifrado+=estado #Incrementamos o resultado nessa variável para escrever o arquivo cifrado
				dados = b''          #Necessário deixar essa variável vazia para que possamos ler outro bloco


		novo_arquivo = open("Arquivo editado.txt", "wb")
		novo_arquivo.write(textoCifrado)
		novo_arquivo.close()
		break

	elif resp.upper() == "D":
		#Decriptar
		textoPlano = b''
		for byte in range(len(dadosCompleto)):
			dados += bytes([dadosCompleto[byte]]) #Lendo um bloco para decriptar
			if len(dados) == 16:
				for r in range(9, -1, -1):

					#Os rounds se iniciam
					if r == 9:
						mEstado = AddRoundKey.Inv_RoundKey(dados, chaveRound[r])
						estado = ShiftRowLayer.Inv_ShiftRow_Layer(mEstado)
						estado = SubByteLayer.Inv_SubByte_Layer(estado)
					else:
						mEstado = AddRoundKey.Inv_RoundKey(estado, chaveRound[r])
						mEstado = MixColumnLayer.Inv_MixColumn_Layer(mEstado)
						estado = ShiftRowLayer.Inv_ShiftRow_Layer(mEstado)
						estado = SubByteLayer.Inv_SubByte_Layer(estado)

				estado = AddRoundKey.AddKey(estado, chave) #Adicionar chave após os rounds

				textoPlano+=estado #Incrementamos o resultado nessa variável para escrever o arquivo decriptado
				dados = b''        #Necessário deixar essa variável vazia para que possamos ler outro bloco

		textoPlano = textoPlano.rstrip(b' ')

		novo_arquivo = open("Arquivo.txt", "wb")
		novo_arquivo.write(textoPlano)
		novo_arquivo.close()
		break

	else:
		print(" \"E\" para encriptar e \"D\" para decriptar, nada além.")