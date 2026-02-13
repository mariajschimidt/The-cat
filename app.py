from flask import Flask, render_template, request, redirect, flash
import requests #conectar API externa

ENDPOINT_API = "https://api.thecatapi.com/v1/images/search"

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template ("index.html")

# Rota para processar a solicitação
@app.route('/cat', methods=['GET', 'POST'])
def cat():
    if request.method == 'GET':
        return redirect('/')
    
    nome = request.form.get('nome', None)

    if not nome:
        erro = "ERRO! Você precisa digitar um nome!"
        return render_template('index.html', erro=erro)
                                                                                                                                  
    resposta = requests.get(ENDPOINT_API)

    if resposta.status_code == 200:
        dados = resposta.json() #Json para DIC
        url_imagem = dados[0]['url']
    else:
        flash("ERRO! Os gatos não estão disponíveis no momento. Tente novamente mais tarde.")
        return redirect('/')
    
    return render_template('index.html', nome=nome, url_imagem=url_imagem)

if __name__ == '__main__':
    app.run(debug=True)