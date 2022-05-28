from interface.tugas_admin_jurusan import TugasAdminJurusan 

class AdminJurusan (TugasAdminJurusan) :
    
    def publikasi_jadwal(self) -> None :
        print ("Admin jurusan mempublikasi jadwal ujian")