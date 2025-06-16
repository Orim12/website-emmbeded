# server.py
# Flask-server die index.html serveert en een (gesimuleerde) temperatuur toont

from flask import Flask, render_template_string
from dht11_sensor import lees_sensor

app = Flask(__name__)

# Lees de inhoud van index.html


@app.route('/')
def home():
    temperatuur, _ = lees_sensor()
    if temperatuur is None:
        temperatuur = 'N/A'
    pagina = '</body>', f'<div style="position:fixed;top:10px;right:10px;background:#fff;padding:10px;border-radius:8px;box-shadow:0 0 8px #ccc;">Temperatuur: {temperatuur}°C</div></body>'
    return render_template_string(pagina)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
