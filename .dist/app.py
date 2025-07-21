import customtkinter as ctk
import tkinter.messagebox

# Configuração geral
ctk.set_appearance_mode("dark")  # "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

# Janela principal
app = ctk.CTk()
app.title("Exemplo CustomTkinter")
app.geometry("400x250")

# Label
label = ctk.CTkLabel(app, text="Digite algo:", font=("Arial", 16))
label.pack(pady=10)

# Campo de entrada
entry = ctk.CTkEntry(app, placeholder_text="Seu texto aqui...")
entry.pack(pady=10)

# Função do botão
def mostrar_texto():
    texto = entry.get()
    tkinter.messagebox.showinfo("Texto digitado", f"Você digitou: {texto}")

# Botão
botao = ctk.CTkButton(app, text="Mostrar Texto", command=mostrar_texto)
botao.pack(pady=20)

# Iniciar loop
app.mainloop()
