# Landing Page de carrera MTB en Tandil 2025

Para correr la aplicación web localmente deberá:
1. Clonar el repositorio en su máquina local
2. Navegar al directorio del proyecto
3. Verificar que tenga instalado Python 3.8 o superior
4. Correr el script run.sh en la terminal

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
