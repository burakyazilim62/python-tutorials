import tkinter as tk

window = tk.Tk()
window.title("ilk deneme")
window.mainloop()

import tkinter as tk
window2 = tk.Tk()
window = tk.Tk()
window.title("ilk deneme")
etikett = tk.Label(window2, text="butona tiklandi")
def tikla():
    etikett.pack()


buton = tk.Button(window,text="tikla",command=tikla)
buton.pack()

window.mainloop()


import tkinter as tk
import random
window = tk.Tk()
window.title("kaydet")
window.geometry("500x500")
giris=tk.Entry()
def uret():
    giris.delete(0,tk.END)
    a = random.randint(1,100)
    giris.insert(0,a)

def kaydet():
    with open("tkinterr.txt", "a", encoding="utf-8") as file:
        file.write(giris.get())
    giris.delete(0,tk.END)
def sil():
    giris.delete(0,tk.END)



giris.pack()

buton = tk.Button(window,text="kaydet",command=kaydet)
buton1 = tk.Button(window,text="sil",command=sil)
buton2 = tk.Button(window,text="uret",command=uret)
buton2.pack()
buton.pack()
buton1.pack()
window.mainloop()


import tkinter as tk
root = tk.Tk()
root.title("grid")
label1 = tk.Label(root,text="1.kisim",bg="red",fg="black")
label2 = tk.Label(root,text="2.kisim",bg="yellow",fg="purple")
label3 = tk.Label(root,text="3.kisim",bg="blue",fg="pink")
label4 = tk.Label(root,text="4.kisim",bg="white",fg="brown")
label1.grid(row=0,column=1)
label2.grid(row=2,column=3)
label3.grid(row=4,column=5)
label4.grid(row=6,column=7)
root.mainloop()