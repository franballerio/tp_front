Para installar las dependencias deberá correr en la terminal:
```
python -m venv .venv
source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
pip install -r requirements.txt
```

Además deberá definir las variables de entorno en un archivo `.env` en la raíz del proyecto:
```
EMAIL_SENDER
EMAIL_PASSWORD
FLASK_APP=app.py
FLASK_ENV=development
```