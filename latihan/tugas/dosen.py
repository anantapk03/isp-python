from interface.tugas_dosen import TugasDosen 

class Dosen(TugasDosen):
    def mencatat_kehadiran (self) -> None :
        super().mencatat_kehadiran()
    
    def membuat_ujian(self) -> None :
        print("Dosen sedang membuat ujian")
    