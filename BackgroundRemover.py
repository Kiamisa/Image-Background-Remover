from rembg import remove
from PIL import Image

#TODO: Ler imagens dadas pelo usuário através de uma interface
input = ''
#TODO: Gerar imagem no caminho do arquivo dado
output = ''

inp = Image.open(input)
output = remove(inp)

output.save(output)
Image.open("")

