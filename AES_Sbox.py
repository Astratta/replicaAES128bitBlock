class Sbox:  
    def mult_int_as_poly(self, x,y):
        if x==0 or y==0:
            return 0
        else:
            z=0
            while x != 0:
                if x & 1 == 1:
                    z ^= y
                y <<= 1
                x >>= 1
            return z

    def number_of_bits(self, x):
        if x == 0:
            return 1
        else:
            nb = 0
            while x != 0:
                nb+=1
                x >>= 1
            return nb
        
    def mod_int_as_poly(self, x,m):
        nbm = self.number_of_bits(m)
        while True:
            nbx = self.number_of_bits(x)
            if nbx - nbm < 0:
                return x
            else:
                x ^= m << (nbx - nbm)

    def AES_field_mult(self, x,y):
        z = self.mult_int_as_poly(x,y)
        m = int("100011011", 2)
        return self.mod_int_as_poly(z,m)

    def mult_inverse(self, x):
        if x == 0:
            return 0
        else:
            for i in range(1, 256):
                if self.AES_field_mult(x, i) == 1:
                    return i

    def produto_escalar(self, x,y):
        z = x & y
        if z == 0:
            return 0
        else:
            pEscalar = 0
            while z != 0:
                pEscalar ^= z & 1
                z >>= 1
            return pEscalar

    def transformacao_afim(self, A, x, b):
        y = 0
        for i in range(7, -1, -1):
            linha = (A >> 8 * i) & 0b11111111
            bit = self.produto_escalar(linha, x)
            y ^= (bit << i)
        return y ^ b

    def AES_Sbox(self, x):
        A = int("1111100001111100001111100001111110001111110001111110001111110001", 2)
        b = int("01100011", 2)
        xinv = self.mult_inverse(x)
        return self.transformacao_afim(A, xinv, b)

    def mostrar_Sbox(self):
        for row in range(16):
            for col in range(16):
                x = 16 * row + col
                hexstring = format(self.AES_Sbox(x), "02x")
                print(hexstring, end = " ")
            print()
    












