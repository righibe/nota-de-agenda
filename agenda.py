import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO = "contatos.json"

def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_contatos():
    with open(ARQUIVO, "w") as f:
        json.dump(contatos, f, indent=2)

def atualizar_lista():
    lista_contatos.delete(0, tk.END)
    for c in contatos:
        lista_contatos.insert(tk.END, f"{c['nome']} | {c['telefone']} | {c['email']}")

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if not nome or not telefone or not email:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
        return

    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos()
    atualizar_lista()
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def remover_contato():
    selecionado = lista_contatos.curselection()
    if not selecionado:
        messagebox.showinfo("Remover", "Selecione um contato para remover.")
        return
    index = selecionado[0]
    contatos.pop(index)
    salvar_contatos()
    atualizar_lista()


contatos = carregar_contatos()

root = tk.Tk()
root.title("Agenda de Contatos")


tk.Label(root, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(root, width=30)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Telefone").grid(row=1, column=0)
entry_telefone = tk.Entry(root, width=30)
entry_telefone.grid(row=1, column=1)

tk.Label(root, text="Email").grid(row=2, column=0)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1)


tk.Button(root, text="Adicionar", command=adicionar_contato).grid(row=3, column=0, pady=10)
tk.Button(root, text="Remover", command=remover_contato).grid(row=3, column=1)


lista_contatos = tk.Listbox(root, width=50)
lista_contatos.grid(row=4, column=0, columnspan=2)

atualizar_lista()
root.mainloop()