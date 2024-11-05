from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def select_image(root):
    file_path = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagens", "*.jpg *.jpeg *.png")])
    if file_path:
        output_path = file_path.rsplit('.', 1)[0] + '_sem_fundo.png'
        process_image(file_path, output_path)

def process_image(input_path, output_path):
    try:
        inp = Image.open(input_path)
        output = remove(inp)
        output.save(output_path)
        print(f"Imagem processada e salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")
    finally:
        messagebox.showinfo("Processo Concluído", "A imagem foi processada e salva.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    select_image(root)