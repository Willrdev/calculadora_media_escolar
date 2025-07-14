from flask import Flask, render_template, request
from random import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', random=random)

@app.route('/calcular_media', methods=['POST'])
def calcular_media():
    nome = request.form['nome']
    nota1 = float(request.form['nota1'])
    nota2 = float(request.form['nota2'])
    nota3 = float(request.form['nota3'])

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        mensagem = 'Aprovado'
        classe_mensagem = 'mensagem-aprovado'
    elif media >= 5:
        mensagem = 'Recuperação'
        classe_mensagem = 'mensagem-recuperacao'
    else:
        mensagem = 'Reprovado'
        classe_mensagem = 'mensagem-reprovado'

    return render_template(
        'index.html',
        nome=nome,
        media=media,
        mensagem=mensagem,
        classe_mensagem=classe_mensagem,
        random=random
    )

if __name__ == '__main__':
    app.run(debug=True)
