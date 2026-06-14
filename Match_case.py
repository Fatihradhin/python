#ini adalah fitur alternate buat elif yang banyak, jadi terkesan lebih "rapih"
print("ini adalah alat pengecek musim")
variable0 = input("ketik e untuk lanjut: ").lower() 

variable1 = input("Masukan nama bulan: ").capitalize()

match variable1: #Match can't Stand alone.
    case "Oktober" | "November" | "Desember" | "Januari" | "Februari" | "Maret": #Garis panjang (|) itu dibaca atau
        print("Musim hujan")
    case "April" | "Mei" | "Juni" | "Juli" | "Agustus" | "September":
        print("Musim kemarau")
    case _: #else nya case, tambahkan underscore
        print("Nama bulan tidak valid.")
        
