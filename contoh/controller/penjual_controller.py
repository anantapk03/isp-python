from interface.penjual_operation import PenjualOperation

class PenjualController (PenjualOperation) :
    
    def menolak_pesanan (self) -> None : 
        print ("Penjual menolak pesanan karena habis") 
    
    def menyiapkan_pesanan (self) -> None :
        print ("penjual menyiapkan pesanan sesuai dengan pilihan pembeli") 
    
    