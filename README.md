# Removedor de Fundo

Este projeto fornece um script simples para remover fundos de imagens utilizando a biblioteca `rembg` e a `PIL` (Python Imaging Library). A ferramenta é projetada para ser amigável e pode ser expandida com uma interface gráfica de usuário (GUI) para facilitar a entrada e saída de imagens.

## Requisitos

Para executar este código, você precisará instalar as seguintes bibliotecas:

- `rembg`
- `Pillow`

Você pode instalar esses pacotes usando pip:

```bash
pip install rembg Pillow
```

## Uso

A implementação atual é um script básico que processa imagens para remoção de fundo. É necessário especificar o caminho da imagem de entrada e o caminho da imagem de saída.

1. Defina a variável `input` com o caminho da imagem que deseja processar.
2. Defina a variável `output` com o caminho desejado para a imagem de saída.

### Exemplo

```python
from rembg import remove
from PIL import Image

# Caminho para a imagem de entrada
input = 'caminho/para/sua/imagem/entrada.jpg'

# Caminho para a imagem de saída
output = 'caminho/para/sua/imagem/saida.png'

# Abre a imagem de entrada
inp = Image.open(input)

# Remove o fundo
output_image = remove(inp)

# Salva a imagem de saída
output_image.save(output)

# Opcional: abre a imagem salva
Image.open(output)
```

## TODO

- Implementar uma interface de usuário para permitir que os usuários selecionem imagens facilmente.
- Adicionar tratamento de erros para operações de arquivos.
- Suportar múltiplos formatos de entrada e processamento em lote.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

- [rembg](https://github.com/danielgatis/rembg) pela funcionalidade de remoção de fundo.
- [Pillow](https://python-pillow.org/) pelo processamento de imagens.

```
