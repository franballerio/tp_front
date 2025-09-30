from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    evento = {
        1: {
            "nombre": "Rally MTB 2025",
            "organizador": "Club Social y Deportivo Unidos por el Deporte",
            "descripcion": "Carrera de MTB rural en dos modalidades 30km y 80km …",
            "fecha": "Domingo 02 de NOVIEMBRE de 2025",
            "horario": "8am",
            "lugar": "Tandil, Buenos Aires",
            "tipo_carrera": "MTB rural",
            "email": "UnidosPorElDeporte@gmail.com",
            "numero_contacto": "010-010-0220",
            "modalidad_costo": {
                1: {"nombre": "Corta", "valor": "100"},
                2: {"nombre": "Larga", "valor": "200"}
            },
            "Auspiciantes": ["Gatorade", "Adidas","Cruz roja"]
        }
    }
    return render_template('index.html', info=evento[1])

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run("localhost", port= 5000, debug=True)
