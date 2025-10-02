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

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "Dependencias instaladas y entorno virtual activado.

flask run --port=5000

echo "Corriendo aplicación Flask en http://localhost:5000"