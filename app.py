from flask import Flask
from python_ocr import ler_texto_da_imagem

app = Flask(__name__)


@app.route("/")
def index():
    text = ler_texto_da_imagem()
    return f"Página Inicial {text}"
