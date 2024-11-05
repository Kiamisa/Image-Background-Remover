from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import requests
from io import BytesIO


def select_local_img():
    file_path = filedialog.askopenfilename(title = "Selecione uma imagem", filetypes = [("Imagens", "*.jpg *jpeg *.png")])
    if file_path:
        output_path = file_path.rsplit('.',1)[0] + '_clean.png'
        process_img(file_path, output_path)

def download_img(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        img  = Image.open(img_data)
        return img
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Não foi possível baixar a imagem: {e}")
        return None

def process_img(file_path, output_path):
    try:
        inp = Image.open(file_path)
        output = remove(inp)
        output.save(output_path)
        messagebox.showinfo("Sucesso!", f"Imagem salva em: {output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar: {e}")

def process_web_img(url):
    img = download_img(url)
    if img:
        output_path = "clean_image.png"
        try:
            output = remove(img)
            output.save(output_path)
            messagebox.showinfo("Sucesso!", f"Imagem salva em: {output_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar: {e}")

def select_image_source():
    # Janela para o usuário escolher entre imagem local ou URL
    top = tk.Toplevel(root)
    top.title("Selecionar Fonte da Imagem")

    def local_image():
        top.destroy()
        select_local_img()

    def web_image():
        top.destroy()
        prompt_url()

    ttk.Button(top, text="Imagem Local", command=local_image).pack(padx=10, pady=10)
    ttk.Button(top, text="Imagem da Web (URL)", command=web_image).pack(padx=10, pady=10)

def prompt_url():
    # Janela para o usuário inserir uma URL
    url_window = tk.Toplevel(root)
    url_window.title("Inserir URL da Imagem")

    tk.Label(url_window, text="Insira a URL da imagem:").pack(padx=10, pady=10)
    url_entry = tk.Entry(url_window, width=50)
    url_entry.pack(padx=10, pady=10)

    def process_url():
        url = url_entry.get()
        url_window.destroy()
        process_web_img(url)

    ttk.Button(url_window, text="Processar", command=process_url).pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Remoção de Fundo de Imagem")
    root.geometry("400x200")

    ttk.Button(root, text="Selecionar Imagem", command=select_image_source).pack(padx=20, pady=50)

    root.mainloop()

