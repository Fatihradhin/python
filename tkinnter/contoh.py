import tkinter as tk
from tkinter import messagebox

def tampilkan_pesan():
    nama = entry_nama.get()
    if nama == "":
        messagebox.showwarning("Peringatan", "Masukkan nama dulu!")
    else:
        label_hasil.config(text=f"halo, {nama}! selamat datang")

root = tk.Tk()
root.title("Jendela sapaan")
root.geometry("300x200")

label_judul = tk.Label(root, text="Form Input Nama", font=("Arial", 14))
label_judul.pack(pady=10)


entry_nama = tk.Entry(root)
entry_nama.pack(pady=5)


btn_submit = tk.Button(root, text="Submit", command=tampilkan_pesan)
btn_submit.pack(pady=10)

label_hasil = tk.Label(root, text="")
label_hasil.pack(pady=10)

root.mainloop()