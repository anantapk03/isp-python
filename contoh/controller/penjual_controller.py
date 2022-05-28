from interface.penjual_operation import PenjualOperation

class PenjualController (PenjualOperation) :
    
    def menolak_peanan (self) -> None : 
        print ("Penjual menolak pesanan karena habis") 
    
    def menerima_pesanan (self) -> None :
        print ("penjual menyiapkan pesanan sesuai dengan pilihan pembeli") 
    
    