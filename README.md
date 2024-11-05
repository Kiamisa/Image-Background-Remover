# Remoção de Fundo de Imagens com Python

Este projeto é um aplicativo simples em Python que permite selecionar uma imagem e remover seu fundo automaticamente, salvando o resultado em um novo arquivo.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Tkinter**: Utilizado para criar a interface gráfica e selecionar a imagem.
- **Pillow (PIL)**: Biblioteca para manipulação de imagens.
- **rembg**: Biblioteca de remoção de fundo automático de imagens.

## Pré-requisitos

Antes de executar o código, você precisa instalar as bibliotecas necessárias. Para fazer isso, execute os seguintes comandos no terminal:

```bash
pip install rembg
pip install pillow
```

## Como Usar

1. **Clone ou Baixe o Projeto**: Baixe o arquivo `.py` para o seu ambiente local.
2. **Execute o Código**:
   - No terminal, navegue até o diretório do arquivo `.py` e execute:
     ```bash
     python nome_do_arquivo.py
     ```
3. **Selecione a Imagem**:
   - Uma janela aparecerá para que você selecione a imagem da qual deseja remover o fundo. Selecione uma imagem nos formatos `.jpg`, `.jpeg` ou `.png`.
4. **Processamento da Imagem**:
   - A imagem será processada e salva no mesmo diretório com o sufixo `_sem_fundo` no nome do arquivo.
5. **Notificação**:
   - Uma mensagem de conclusão aparecerá após o processamento.


## Funcionalidades

- Selecionar uma imagem da sua máquina.
- Remover o fundo da imagem selecionada.
- Salvar a imagem resultante com fundo transparente.

## Observações

- **Formato de Saída**: A imagem sem fundo será salva em formato `.png` para preservar a transparência.
- **Compatibilidade**: Certifique-se de que as bibliotecas estão instaladas no mesmo ambiente de execução do código.

## Problemas Comuns

- **Erro de Importação**: Caso ocorra algum erro de importação, verifique se todas as bibliotecas estão instaladas e se o ambiente Python está configurado corretamente.
- **Imagem Não Carregada**: Certifique-se de que o arquivo selecionado está em um formato compatível (`.jpg`, `.jpeg`, ou `.png`).

## Licença

Este projeto é de livre uso para fins educacionais e experimentais. Sinta-se à vontade para modificar e melhorar conforme necessário.

---

Este é um exemplo simples de uso de `Tkinter`, `Pillow` e `rembg` para remoção de fundo de imagens em Python.
