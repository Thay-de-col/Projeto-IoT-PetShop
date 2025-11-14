from flask import Flask, render_template, jsonify
from flask_cors import CORS
import random
import datetime

app = Flask(__name__)
CORS(app)  # 👈 adiciona essa linha

# Lista para guardar o histórico do dia
historico = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dados')
def dados():
    global historico

    temperatura = round(random.uniform(20, 30), 1)
    umidade = round(random.uniform(40, 80), 1)
    presenca = random.choice(["Detectada", "Não detectada"])

    horario = datetime.datetime.now().strftime("%H:%M:%S")

    historico.append({
        "hora": horario,
        "temperatura": temperatura,
        "umidade": umidade,
        "presenca": presenca
    })
    if len(historico) > 20:
        historico.pop(0)

    return jsonify({
        "temperatura": temperatura,
        "umidade": umidade,
        "presenca": presenca,
        "historico": historico
    })

if __name__ == '__main__':
    app.run(debug=True)
