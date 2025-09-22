# Imagem base com Python
FROM python:latest

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o requirements.txt
COPY requirements.txt .

# Instala as dependências (esta layer será cacheada)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia o resto dos arquivos
COPY . .

# Dá permissão de execução ao script
RUN chmod +x start.sh

# Porta padrão do Flask
EXPOSE 5000

# Comando padrão
CMD ["./start.sh"]






