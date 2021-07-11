from AES_SubBytes import SubByte
from AES_ShiftRows import ShiftRow
from AES_MixColumn import MixColumn
from AES_Key_Schedule import KeySchedule
from AES_AddRoundKey import AddRoundKey
#from AES_Sbox import Sbox

SubByteLayer = SubByte()
ShiftRowLayer = ShiftRow()
MixColumnLayer = MixColumn()
KeyExpansion = KeySchedule()
AddRoundKey = AddRoundKey()
#Sbox = Sbox()

dados_bytes = open("arquivo.txt", "rb")
dados = dados_bytes.read()


#Adicionar chave antes do round 1
estado = AddRoundKey.AddKey(dados, chave)

#Os rounds se iniciam
for r in range(10):
	if r != 9:
		estado = SubByteLayer.SubByte_Layer(estado)
		mEstado = ShiftRowLayer.ShiftRow_Layer(estado)
		#A partir daqui, estado agora é de fato um matriz 4x4
		mEstado = MixColumnLayer.MixColumn_Layer(mEstado)
		#Calcula chave do round
		chave = KeyExpansion.Key_Expansion(chave, r)
		#Adicionar chave do round correspondente
		estado = AddRoundKey.RoundKey(mEstado, chave)
	else:
		estado = SubByteLayer.SubByte_Layer(estado)
		mEstado = ShiftRowLayer.ShiftRow_Layer(estado)
		#Calcula chave do round
		chave = KeyExpansion.Key_Expansion(chave, r)
		#Adicionar chave do round correspondente
		estado = AddRoundKey.RoundKey(mEstado, chave)



#Sbox.mostrar_Sbox()
#print(KeyExpansion.Key_Expansion(KeyExpansion.gerar_matriz(), 0))
