# 🚀 Api Flask com TensorFlow

O objetivo do projeto é aprender como disponibilizar um modelo de classificação de imagens na web utilizando Flask e TensorFlow. 
A aplicação recebe o número da imagem via requisição HTTP e retorna a classe prevista pelo modelo treinado.

---

## 🛠️ Tecnologias utilizadas
- Flask: Framework web em Python
- TensorFlow: Biblioteca de aprendizado de máquina
- Docker: Containerização da aplicação
  
---

## ⚙️ Como executar

1. Crie a imagem Docker:
   ```
   docker build -t flask-tf .
   ```
2. Rode o container:
   ```
   docker run -d -p 5000:5000 --rm -v "$(pwd)/uploads:/app/uploads" --name flast-tf-container flask-tf
   ```
3. Teste a API com uma imagem:
   ```
   curl -X POST http://localhost:5000/0.png
   ```
