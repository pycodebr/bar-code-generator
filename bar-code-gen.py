from barcode import EAN13
from barcode.writer import ImageWriter

# Gera o código de barras e salva no caminho desejado #
with open(r'D:\pycode\bar-code-generator\barcode.png', 'wb') as f:
    EAN13('123456789102', writer=ImageWriter()).write(f)