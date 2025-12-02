class rekening:
    def __init__ (self, saldo):
        self.saldo = saldo
    def tambah_saldo (self):
        self.saldo += 500000
        print(f"saldo anda sekarang: {self.saldo}")
    def cek_saldo (self):
        print(f"saldo anda: {self.saldo}")
saldo1 = rekening (1000000)
saldo1.tambah_saldo()
saldo1.cek_saldo()