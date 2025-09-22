# Etapa 1: Importação das bibliotecas
import numpy as np
import tensorflow as tf

import imageio.v2 as imageio
from flask import Flask, jsonify

# print(tf.__version__)

# Etapa 2: Carregamento do modelo pré-trainado
with open('fashion_model.json', 'r') as f:
    model_json = f.read()

model = tf.keras.models.model_from_json(model_json)
model.load_weights('fashion_model.weights.h5')
# model.summary()

# Etapa 3: Criação da API em Flask
app = Flask(__name__)

# Função para classificação de imagens
@app.route('/<string:img_name>', methods=['POST'])
def classify_image(img_name):
    upload_dir =  'uploads/'
    image = imageio.imread(upload_dir + img_name)

    classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    
    # [1, 28, 28] -> [1, 784]
    prediction = model.predict([image.reshape(1, 28 * 28)])

    return jsonify({'object_identified': classes[np.argmax(prediction[0])]})


# Iniciando a aplicação Flask
app.run(host='0.0.0.0', port=5000, debug=True)
