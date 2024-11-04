from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# Função para abrir uma imagem através de um diálogo de seleção de arquivos
def select_image():
    file_path = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagens", "*.jpg *.jpeg *.png")])
    if file_path:
        output_path = file_path.rsplit('.', 1)[0] + '_sem_fundo.png'  # Definindo o nome da imagem de saída
        process_image(file_path, output_path)
        print(f"Imagem processada e salva em: {output_path}")

# Função para processar e salvar a imagem sem fundo
def process_image(input_path, output_path):
    inp = Image.open(input_path)
    output = remove(inp)
    output.save(output_path)

# Interface para seleção de imagem
root = tk.Tk()
root.withdraw()  # Oculta a janela principal do Tkinter
select_image()

# Interface para seleção de imagem
root = tk.Tk()
root.withdraw()  # Oculta a janela principal do Tkinter
select_image()