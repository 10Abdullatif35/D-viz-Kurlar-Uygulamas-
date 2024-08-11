import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def verileri_guncelle():
    url = "https://www.doviz.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    gold = soup.find("span", {"data-socket-key": "gram-altin"}).text
    dolar = soup.find("span", {"data-socket-key": "USD"}).text
    eur = soup.find("span", {"data-socket-key": "EUR"}).text
    sterlin = soup.find("span", {"data-socket-key": "GBP"}).text
    bist = soup.find("span", {"data-socket-key": "XU100"}).text
    bitcoin = soup.find("span", {"data-socket-key": "bitcoin"}).text

    dolar2 = float(dolar.replace(",", "."))
    eur2 = float(eur.replace(",", "."))
    sterlin2 = float(sterlin.replace(",", "."))
    bist2 = float(bist.replace(".", "").replace(",", "."))
    bitcoin2 = float(bitcoin.replace("$", ""))
    return gold, dolar2, eur2, sterlin2, bist2, bitcoin2

def update_values():
    values = verileri_guncelle()
    gold_var.set(values[0])
    dolar_var.set(values[1])
    eur_var.set(values[2])
    sterlin_var.set(values[3])
    bist_var.set(values[4])
    bitcoin_var.set(values[5])

window = tk.Tk()
window.geometry("300x350")
window.title("DÖVİZ KURLARI")
window.configure(background="#f0f0f0")

title_label = tk.Label(window, text="Borsa Bilgileri", font=("Helvetica", 20), bg="#a6a6a6", padx=10, pady=5)
title_label.pack(fill=tk.X)

labels_frame = tk.Frame(window, bg="#f0f0f0")
labels_frame.pack(pady=10)

labels = [
    ("Gram Altın(TL):", "arial 14"),
    ("Dolar(TL):", "arial 14"),
    ("Euro(TL):", "arial 14"),
    ("Sterlin(TL):", "arial 14"),
    ("BIST:", "arial 14"),
    ("Bitcoin($):", "arial 14"),
]

gold_var = tk.StringVar()
dolar_var = tk.DoubleVar()
eur_var = tk.DoubleVar()
sterlin_var = tk.DoubleVar()
bist_var = tk.DoubleVar()
bitcoin_var = tk.DoubleVar()

vars_list = [gold_var, dolar_var, eur_var, sterlin_var, bist_var, bitcoin_var]

for i, (label_text, font) in enumerate(labels):
    label = tk.Label(labels_frame, text=label_text, font=(font, 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

    value_label = tk.Label(labels_frame, textvariable=vars_list[i], font=(font, 12), bg="#d9d9d9")
    value_label.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W+tk.E)

# İlk değerleri almak için güncelleme fonksiyonunu çağır
update_values()

# Oval buton oluşturma ve efekt ekleme
style = ThemedStyle(window)
style.set_theme("radiance")

update_button = ttk.Button(window, text="Değerleri Güncelle", command=update_values, style="TButton", cursor="hand2")
update_button.pack(pady=10, ipadx=10, ipady=5)

window.mainloop()
