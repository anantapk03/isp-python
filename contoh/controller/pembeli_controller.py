from interface.pembeli_operation import PembeliOperation

class PembeliController (PembeliOperation) :
    def memesan_pesanan (self) -> None :
        print ("Pembeli melakukan pemesanan")