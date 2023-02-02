import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def busca_precios():
    # Obtener el nombre de la criptomoneda seleccionada en el combo
    selected = combo.get()

    # Lo buscamos en coinmarketcap
    url = f"https://coinmarketcap.com/currencies/{selected}/"
    response = requests.get(url)

    # Parseamos la respuesta para que sea legible por BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Nos quedamos con el precio de la criptomoneda si existe
    price_elem = soup.select_one(".priceValue")
    if price_elem:
        price = price_elem.text.strip()
    else:
        price = "Precio no disponible"

    # Mostramos el precio en el text (habilitamos el text, borramos el contenido, insertamos el precio y lo deshabilitamos)
    text.configure(state="normal")
    text.delete("1.0", "end")
    text.insert("1.0", f"Precio de {selected}: {price}")
    text.configure(state="disabled")

# Creamos la ventana y tamaño 600x400
root = tk.Tk()
root.geometry("600x400")
root.title("Precios de criptomonedas")

# Creamos el header
header = tk.Frame(root, bg="blue", height=50)
header.pack(side="top", fill="x")

# Creamos el título que irá en el header
title = tk.Label(header, text="", fg="white", font=("Helvetica", 16), bg="blue")
title.pack(side="top", padx=100)
title.configure(text="Consultar precios de criptomonedas")

# Creamos el combo (Por defecto, vendra bitcoin marcado) y el botón color azul(pady es el padding vertical entre widgets)
combo = ttk.Combobox(root, values=["Bitcoin", "Ethereum", "BNB", "Solana", "Polygon", "Polkadot", "Litecoin", "Dogecoin"], state="readonly")
combo.set("Bitcoin")
combo.pack(pady=20)
button = tk.Button(root, text="Buscar", command=busca_precios, bg="blue", fg="white")
button.pack(pady=20)

# Creamos el text (y lo deshabilitamos para que no se pueda escribir)
text = tk.Text(root, height=10, width=50, state="disabled")
# Lo expandimos para que ocupe todo el espacio disponible
text.pack(fill="both", expand=True)

# Mostramos la ventana
root.mainloop()