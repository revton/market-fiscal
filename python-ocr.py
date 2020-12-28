from PIL import Image
import pytesseract


def ler_texto_da_imagem():
    return pytesseract.image_to_string(Image.open('img/imagem-teste-com-ocr.jpg'), lang='eng')

print(ler_texto_da_imagem())