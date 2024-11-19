import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import os

model = load_model("C:\\Users\\joaoc\\OneDrive\\Área de Trabalho\\7 semestre\\Inteligencia Artificial\\chap10\\LeNet5.keras")

def load_images_from_folder(folder_path, target_size=(28, 28)):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            img_path = os.path.join(folder_path, filename)
            img = load_img(img_path, color_mode='grayscale', target_size=target_size)
            img_array = img_to_array(img)
            img_array = img_array.astype('float32') / 255.0
            images.append(img_array)
    return np.array(images)

folder_path = "C:\\Users\\joaoc\\OneDrive\\Área de Trabalho\\7 semestre\\Inteligencia Artificial\\chap10\\apresentacao\\resized"
x_test = load_images_from_folder(folder_path)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

predictions = model.predict(x_test)

print("Predictions:")
for i, pred in enumerate(predictions):
    print(f"Image {i+1}: Predicted label: {np.argmax(pred)}")
