from tensorflow.keras.datasets import fashion_mnist
import imageio.v2 as imageio
import os

# Garante que a pasta 'uploads/' existe
os.makedirs('uploads', exist_ok=True)

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

for i in range(5):
    imageio.imwrite(f'uploads/{i}.png', x_test[i])

print("Imagens salvas com sucesso na pasta 'uploads/'!")
