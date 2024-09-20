
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copiar o arquivo requirements.txt para o container
COPY requirements.txt ./

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o container
COPY . .

# Comando para rodar o Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
