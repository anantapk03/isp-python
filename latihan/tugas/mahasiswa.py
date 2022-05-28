from interface.tugas_mahasiswa import TugasMahasiswa

class Mahasiswa (TugasMahasiswa) :
    
    def mengerjakan_ujian(self) -> None :
        print("Mahasiswa sedang mengerjakan ujian")
        