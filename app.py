from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import dotenv as _
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_SENDER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_SENDER')

mail = Mail(app)


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

@app.route('/send', methods=['POST'])
def send_email():
    # Handle JSON data instead of form data
    data = request.get_json()
    
    if not data:
        return {"error": "No data received"}, 400
    
    # Validate required fields
    required_fields = ['name', 'email', 'subject']
    for field in required_fields:
        if not data.get(field):
            return {"error": f"Missing required field: {field}"}, 400
    
    info = f"""
    Nombre: {data['name']}
    Carrera: {data['subject']}
    Información relevante sobre el participante: {data.get('message', '')}
    """
    recipient = data['email']
    
    try:
        msg = Message("Inscripción al evento MTB Tandil 2025",
                      recipients=[recipient])
        msg.body = info
        mail.send(msg)
        return {"message": "Email sent successfully"}, 200
    except Exception as e:
        return {"error": f"Failed to send email: {str(e)}"}, 500

if __name__ == '__main__':
    app.run("localhost", port= 5000, debug=True)
