import os
from PIL import Image

'''
Used to resize the images dimensions. sometimes when saving from paint, the dimensions aren't 28x28, so this script fix it
'''

source_dir = "C:\\Users\\joaoc\\OneDrive\\Área de Trabalho\\7 semestre\\Inteligencia Artificial\\chap10\\apresentacao"
dest_dir = "C:\\Users\\joaoc\\OneDrive\\Área de Trabalho\\7 semestre\\Inteligencia Artificial\\chap10\\apresentacao\\resized"

os.makedirs(dest_dir, exist_ok=True)

new_size = (28, 28)

for filename in os.listdir(source_dir):
    if filename.endswith('.jpg'):
        with Image.open(os.path.join(source_dir, filename)) as img:
            resized_img = img.resize(new_size)
            resized_img.save(os.path.join(dest_dir, filename))

print("Image resizing completed.")
