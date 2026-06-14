import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
window = tk.Tk() #ini root

nama_1 = tk.StringVar()

def klik():
    print(nama_1.get())
    


window.geometry("300x400") #for setting the size of window
window.resizable(True,True) #the rule for ur window, if false, anyone can't resize it. Bool only (i think...)
window.title("daftar") #for ur window title

input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

label_nama = ttk.Label(input_frame,text='Masukan nama')
label_nama.pack(padx=97,pady=10,fill="x",expand=True)

nama_entry = ttk.Entry(input_frame,textvariable=nama_1)
nama_entry.pack(padx=10,pady=10,fill="x",expand=True)


    

button1 = ttk.Button(input_frame,text='sapa',command=klik)
button1.pack(padx=10,pady=10,fill='x',expand=True)


window.mainloop()