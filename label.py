import tkinter as tk

window = tk.Tk()
window.title("ilk deneme")
etiket = tk.Label(window,text = "merhaba dunya")
etiket.pack()
etiket1 = tk.Label(window,text="iki kısım calisti",fg = "red")
etiket1.pack()
etiket2 = tk.Label(window,text="3 kısım çalıştı",fg = "yellow",bg = "grey")
etiket2.pack()
etiket3 = tk.Label(window,text="4 etiket calisti",fg = "lime",bg ="black",font="times 22 italic")
etiket3.pack()
window.mainloop()

