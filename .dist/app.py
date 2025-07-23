import customtkinter as ctk
import tkinter.messagebox
import database

def limpar_tela():
    for widget in app.winfo_children():
        widget.destroy()

# Função dos botões
def mostrar_texto():
    texto = database.texto()
    tkinter.messagebox.showinfo("Mensagem", f"{texto}")
    
def busco_emprego():
    limpar_tela()
    
    # Card principal (com borda e fundo escuro)
    card_frame = ctk.CTkFrame(
    app,
    fg_color="#2E2E2E",           # Cor de fundo
    border_width=2,               # Espessura da borda
    border_color="#4ECB71",       # Cor da borda (verde)
    corner_radius=10              # Cantos arredondados
    )
    card_frame.pack(pady=40, padx=300, fill="both", expand=True)

    # Título do card
    card_title = ctk.CTkLabel(
        card_frame,
        text="📝 Escolha uma Opção",
        font=("Arial", 16, "bold"),
        text_color="#4ECB71"  # Cor do texto
    )
    card_title.pack(pady=12)

    
    
# Configuração geral
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Site De Empregos")
app.geometry("800x450")

# Card principal (com borda e fundo escuro)
card_frame = ctk.CTkFrame(
    app,
    fg_color="#2E2E2E",           # Cor de fundo
    border_width=2,               # Espessura da borda
    border_color="#4ECB71",       # Cor da borda (verde)
    corner_radius=10              # Cantos arredondados
)
card_frame.pack(pady=40, padx=300, fill="both", expand=True)

# Título do card
card_title = ctk.CTkLabel(
    card_frame,
    text="📝 Escolha uma Opção",
    font=("Arial", 16, "bold"),
    text_color="#4ECB71"  # Cor do texto
)
card_title.pack(pady=12)



# Botões estilizados dentro do card
botao1 = ctk.CTkButton(
    card_frame,
    text="Busco Emprego",
    command=busco_emprego,
    fg_color="#3B8ED0",  # Azul
    hover_color="#1F6AA5",
    corner_radius=8
)
botao1.pack(pady=10, padx=20, fill="x")

botao2 = ctk.CTkButton(
    card_frame,
    text="Sou Empresa",
    command="abre uma nova aba",
    fg_color="#2E7D32",  # Verde
    hover_color="#1B5E20",
    corner_radius=8
)
botao2.pack(pady=10, padx=20, fill="x")

app.mainloop()