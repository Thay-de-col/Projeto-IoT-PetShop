from flask import Flask, render_template, jsonify, send_from_directory
from flask_cors import CORS
import random
import datetime

app = Flask(__name__)
CORS(app)  # libera o acesso do front-end

# Lista para guardar o histórico do dia
historico = []

# --- ROTA PARA SERVIR AS IMAGENS ----
@app.route('/imagens/<path:filename>')
def imagens(filename):
    return send_from_directory("static/imagens", filename)

# --- ROTA DA PÁGINA PRINCIPAL ----
@app.route('/')
def index():
    return render_template('index.html')

# --- ROTA DOS SENSORES ---
@app.route('/dados')
def dados():
    global historico

    # Simulação dos sensores
    temperatura = round(random.uniform(20, 30), 1)
    umidade = round(random.uniform(40, 80), 1)
    presenca = random.choice(["Detectada", "Não detectada"])

    # Horário atual
    horario = datetime.datetime.now().strftime("%H:%M:%S")

    # Salvar no histórico
    historico.append({
        "hora": horario,
        "temperatura": temperatura,
        "umidade": umidade,
        "presenca": presenca
    })

    # manter só os últimos 20
    if len(historico) > 20:
        historico.pop(0)

    # Enviar pro front-end
    return jsonify({
        "temperatura": temperatura,
        "umidade": umidade,
        "presenca": presenca,
        "historico": historico
    })

if __name__ == '__main__':
    app.run(debug=True)
