import tkinter
from tkinter import *

ekran = tkinter.Tk()
ekran.title("VKE HESAPLAMA")
ekran.geometry("500x300")
FONT = ("Arial", 10, "bold")

def hesaplama():
    boy = boy_giris.get()
    kilo = kilo_giris.get()

    if boy == "" or kilo == "":
        sonuc.config(text="Bilgileri tam giriniz!")
    else:
        vke_sonuc= float(kilo) / (float(boy) * float(boy)) * 10000
        if vke_sonuc <= 18.5:
            sonuc.config(text=f"Vucut kitle endeks oranınız: {vke_sonuc}", bg="black",fg="white",font=("Arial", 15, "bold"))
            obezite.config(text="ZAYIFSINIZ", bg="black",fg="white",font=("Arial", 15, "bold"))
        elif vke_sonuc <= 25:
            sonuc.config(text=f"Vucut kitle endeks oranınız: {vke_sonuc}", bg="black",fg="white",font=("Arial", 15, "bold"))
            obezite.config(text="NORMALSİNİZ", bg="black", fg="white", font=("Arial", 15, "bold"))
        elif vke_sonuc <= 30:
            sonuc.config(text=f"Vucut kitle endeks oranınız: {vke_sonuc}", bg="black", fg="white",font=("Arial", 15, "bold"))
            obezite.config(text="KİLOLUSUNUZ", bg="black", fg="white", font=("Arial", 15, "bold"))
        else:
            sonuc.config(text=f"Vucut kitle endeks oranınız: {vke_sonuc}", bg="black", fg="white",font=("Arial", 15, "bold"))
            obezite.config(text="O B E Z S İ N İ Z", bg="black", fg="white", font=("Arial", 15, "bold"))

        # sonuc.config(text=f"Vucut kitle endeks oranınız: {vke_sonuc}")


kilo_giris_label = tkinter.Label(text="Kilo giriniz(kg)", bg="white", fg="black")
kilo_giris_label.pack()

kilo_giris = tkinter.Entry(width=15)
kilo_giris.pack()

boy_giris_label = tkinter.Label(text="Boy giriniz(cm)", bg="white", fg="black")
boy_giris_label.pack()

boy_giris = tkinter.Entry(width=15)
boy_giris.pack()

sonucButton = tkinter.Button(text="Hesapla", command=hesaplama)
sonucButton.pack()

sonuc = tkinter.Label()
sonuc.pack()

obezite = tkinter.Label()
obezite.pack()

ekran.mainloop()
