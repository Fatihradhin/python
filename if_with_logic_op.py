#selain menggunakan comparation kita bisa pakai logical function.
#1, and. as you guys know, and bisa true apabla kedua opsnnya true
nilai1 = int(input("masukan umur anda: "))
nilai2 = input("Apakah anda sudah berkeluarga? (ya/tidak): ")

if nilai1 >18 and nilai2 == "tidak":
    print("kamu dapat ikut misi ini, sepertinya")
else:
    print("maaf, tapi lebih baik kamu mencari pekerjaan lain.")
    exit()
#or, salah satu true == true
nilai3 = input("Pandai/bisa mendominasi situasi? (ya/tidak):")
nilai4 = int(input("pengalaman berapa tahun di bidang ini? (Masukan angka): "))

if nilai3 == "ya" or nilai4 >2:
    print("Baiklah, tunggu informasi lebih lanjut...")
else:
    print("Maaf, kamu tidak diterima.")
    exit()
#not, membalikan fungsi  logika

nilai5 = input("Bisa bela diri? (ya/tidak): ")

if not(nilai5 == "ya"):
    print("Kamu harus bisa, setidaknya jika ingin tetap hidup")
else:
    print("kamu diterima...")

#btw disana aku tambahin exit biar lebih seru HAHAHAH