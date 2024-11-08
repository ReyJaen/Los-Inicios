import tkinter as tk
from tkinter import PhotoImage
import subprocess

root = tk.Tk()
root.title("Robot")
root.geometry("900x800")

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

left_frame = tk.Frame(main_frame)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

right_frame = tk.Frame(main_frame)
right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)

conversation = tk.Text(right_frame, wrap=tk.WORD, state=tk.DISABLED)
conversation.pack(expand=True, fill=tk.BOTH)

bottom_frame = tk.Frame(right_frame)
bottom_frame.pack(fill=tk.X, pady=5)

input_box = tk.Entry(bottom_frame)
input_box.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

send_button = tk.Button(bottom_frame, text="Enviar", command=lambda: enviar_texto())
send_button.pack(side=tk.RIGHT, padx=5)

try:
    avatar_img = PhotoImage(file="robot2.png")  
    avatar_label = tk.Label(left_frame, image=avatar_img)
    avatar_label.pack()
except Exception as e:
    print(f"Error al cargar la imagen: {e}")

ruta_ollama = r"C:\Users\reymi\AppData\Local\Programs\Ollama\ollama.exe"

def responder_ia(texto_entrada):
    try:
        respuesta = subprocess.check_output(
            [ruta_ollama, "run", "llama3.2:1b", texto_entrada],
            text=True, encoding="utf-8"
        ).strip()
        print("Respuesta de Ollama:", respuesta) 
    except subprocess.CalledProcessError as e:
        print("Error en Ollama:", e.stderr)  
        respuesta = "Lo siento, hubo un problema al generar la respuesta."
    except Exception as e:
        print("Error al ejecutar Ollama:", e)  
        respuesta = "Lo siento, hubo un problema al generar la respuesta."
    
    return respuesta

def enviar_texto():
    texto_entrada = input_box.get()
    if texto_entrada:
        agregar_texto(f"Tú: {texto_entrada}")
        
        respuesta = responder_ia(texto_entrada)
        
        agregar_texto(f"Alexa la Aventurera: {respuesta}")
        
        input_box.delete(0, tk.END)

def agregar_texto(texto):
    conversation.config(state=tk.NORMAL)
    conversation.insert(tk.END, texto + "\n")
    conversation.config(state=tk.DISABLED)
    conversation.see(tk.END)

root.mainloop()
