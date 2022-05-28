from interface.driver_operation import DriverOperation 

class DriverController(DriverOperation) :
    def menolak_pesanan (self) -> None :
        print ("Driver menolak pesanan karena lokasi tidak terjangkau") 
    
    def mengantar_pesanan (self) -> None :
        print ("Driver mengantar pesanan dari penjual ke pembeli") 
    
    
    