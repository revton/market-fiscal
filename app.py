from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    text = ler_texto_da_imagem()
    return "Página Inicial"

app.run()



