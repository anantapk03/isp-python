from interface.tugas_mahasiswa import TugasMahasiswa 

class Mahasiswa (TugasMahasiswa) :
    def mencatat_kehadiran (self) -> None :
        super().mencatat_kehadiran()
    
    def mengerjakan_ujian(self) -> None :
        print("Mahasiswa sedang mengerjakan ujian")
        