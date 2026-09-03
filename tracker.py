import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

SOUBOR = "historie.json"
historie = []

if os.path.exists(SOUBOR):
    try:
        with open(SOUBOR, "r") as f:
            historie = json.load(f)
    except:
        historie = []

def uloz():
    with open(SOUBOR, "w") as f:
        json.dump(historie, f, indent=2)

def vypocitej():
    try:
        h = float(e1.get())
        v = float(e2.get())
        k_text = e3.get()
        km = float(k_text) if k_text else 0

        kch = v / h
        
        zaznam = {
            "datum": datetime.now().strftime("%d.%m %H:%M"),
            "kc_h": round(kch, 2),
            "vydelano": v
        }
        historie.append(zaznam)
        uloz()

        if kch >= 333:
            vysledek.config(text=f"GOD MODE! {kch:.0f} Kc/h")
        else:
            vysledek.config(text=f"{kch:.0f} Kc/h")

        aktualizuj()
    except Exception as e:
        messagebox.showerror("Chyba", str(e))

def aktualizuj():
    box.delete(0, tk.END)
    total = sum([z["vydelano"] for z in historie])
    for z in reversed(historie[-15:]):
        box.insert(tk.END, f'{z["datum"]} - {z["kc_h"]} Kc/h - {z["vydelano"]} Kc')
    label_celkem.config(text=f"Celkem: {total:.0f} Kc | Smen: {len(historie)}")

def graf():
    if len(historie) < 1:
        messagebox.showinfo("Graf", "Zadne zaznamy!")
        return
    
    top = tk.Toplevel(okno)
    top.title("Graf")
    top.geometry("350x400")
    tk.Label(top, text="HISTORIE Kc/h", font=("Arial", 12, "bold")).pack()
    
    for z in historie:
        sirka = min(int(z["kc_h"] / 6), 40)
        cara = "#" * sirka
        barva = "red" if z["kc_h"] >= 333 else "blue"
        tk.Label(top, text=f'{z["datum"]} {z["kc_h"]} {cara}', fg=barva, font=("Courier", 9), anchor='w').pack()

okno = tk.Tk()
okno.title("Wolt Tracker V4.2")
okno.geometry("400x600")

tk.Label(okno, text="WOLT TRACKER V4.2", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(okno, text="Hodiny:").pack()
e1 = tk.Entry(okno, justify='center')
e1.pack()

tk.Label(okno, text="Vydelano Kc:").pack()
e2 = tk.Entry(okno, justify='center')
e2.pack()

tk.Label(okno, text="Km (volitelne):").pack()
e3 = tk.Entry(okno, justify='center')
e3.pack()

tk.Button(okno, text="VYPOCTITAT + ULOZIT", command=vypocitej, bg="#00D1FF").pack(pady=10)
vysledek = tk.Label(okno, text="", font=("Arial", 14, "bold"))
vysledek.pack()

tk.Button(okno, text="UKAZ GRAF", command=graf, bg="gold").pack(pady=5)

tk.Label(okno, text="Posledni smeny:").pack(pady=(10,0))
box = tk.Listbox(okno, width=50)
box.pack()

label_celkem = tk.Label(okno, text="", font=("Arial", 10, "bold"))
label_celkem.pack(pady=10)

aktualizuj()
okno.mainloop()
