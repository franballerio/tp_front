#!/bin/bash
set -e

if ! command -v python3 &> /dev/null; then
    echo "Instalando Python3..."
    sudo apt update && sudo apt install -y python3
fi

if ! command -v pip3 &> /dev/null; then
    echo "Instalando pip3..."
    sudo apt install -y python3-pip
fi

if ! python3 -m venv --help &> /dev/null; then
    echo "Instalando módulo venv..."
    sudo apt install -y python3-venv
fi

echo "Creando estructura de proyecto Flask..."
mkdir -p templates static/css static/images
touch app.py

python3 -m venv .venv


pip install Flask


echo "Estructura de Flask creada y entorno virtual activado.
Para activar el entorno virtual, usa: source .venv/bin/activate"