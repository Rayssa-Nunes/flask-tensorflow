#!/bin/bash

echo "Criando pasta uploads..."
mkdir -p uploads

echo "Carregando imagens do Fashion-MNIST..."
python load_images.py

echo "Iniciando o servidor Flask..."
python app.py