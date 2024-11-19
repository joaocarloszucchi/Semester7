import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

def process_img(path):
    img = Image.open(path)
    
    gray_img = img.convert('L')
    
    gray_array = np.array(gray_img)

    normalized_array = gray_array / 255.0
    
    return normalized_array

def print_img(img):
    normalized_array = img
    
    fig, ax = plt.subplots()
    ax.imshow(normalized_array, cmap='gray', vmin=0, vmax=1)
    ax.axis('off')
    
    rows, cols = normalized_array.shape
    
    for i in range(rows + 1):
        ax.axhline(i - 0.5, color='red', linewidth=0.5)
    for j in range(cols + 1):
        ax.axvline(j - 0.5, color='red', linewidth=0.5)
    
    for i in range(rows):
        for j in range(cols):
            ax.text(j, i, f'{normalized_array[i, j]:.2f}', ha='center', va='bottom', color='red', fontsize=5)
    
    for i in range(rows):
        ax.text(-1, i, f'{i}', ha='center', va='center', color='black', fontsize=8)
    for j in range(cols):
        ax.text(j, -1, f'{j}', ha='center', va='center', color='black', fontsize=8)
    
    plt.show()

def plot_images(images):
    fig, axes = plt.subplots(1, len(images), figsize=(15, 5))
    
    for ax, img in zip(axes, images):
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.axis('off')
        
        rows, cols = img.shape
        
        for i in range(rows + 1):
            ax.axhline(i - 0.5, color='red', linewidth=0.5)
        for j in range(cols + 1):
            ax.axvline(j - 0.5, color='red', linewidth=0.5)
        
        for i in range(rows):
            for j in range(cols):
                ax.text(j, i, f'{img[i, j]:.2f}', ha='center', va='bottom', color='red', fontsize=5)
        
        for i in range(rows):
            ax.text(-1, i, f'{i}', ha='center', va='center', color='black', fontsize=8)
        for j in range(cols):
            ax.text(j, -1, f'{j}', ha='center', va='center', color='black', fontsize=8)
    
    plt.show()

def pooling_operation(input_array, kernel_size, stride, padding='valid', pool_mode='max'):
    input_height, input_width = input_array.shape
    kernel_height, kernel_width = kernel_size
    stride_y, stride_x = stride

    if padding == 'same':
        pad_height = max((input_height - 1) // stride_y + 1, input_height) * stride_y + kernel_height - input_height - stride_y
        pad_width = max((input_width - 1) // stride_x + 1, input_width) * stride_x + kernel_width - input_width - stride_x
        input_array = np.pad(input_array, 
                             ((pad_height // 2, pad_height - pad_height // 2),
                            (pad_width // 2, pad_width - pad_width // 2)),
                            mode='constant')

    input_height, input_width = input_array.shape
    output_height = (input_height - kernel_height) // stride_y + 1
    output_width = (input_width - kernel_width) // stride_x + 1
    output_array = np.zeros((output_height, output_width))

    for y in range(0, input_height - kernel_height + 1, stride_y):
        for x in range(0, input_width - kernel_width + 1, stride_x):
            region = input_array[y:y+kernel_height, x:x+kernel_width]
            if pool_mode == 'max':
                output_array[y // stride_y, x // stride_x] = np.max(region)
            elif pool_mode == 'average':
                output_array[y // stride_y, x // stride_x] = np.mean(region)

    return output_array

def multiple_pooling(input_array, kernel_size, stride, padding='valid', pool_mode='max', iterations=1):
    img = input_array
    i = 0
    while i < iterations:
        i+=1
        img = pooling_operation(img, kernel_size, stride, padding, pool_mode)

    return img

def filter_operation(input_array, kernel_size, stride, padding='valid', filter=[]):
    input_height, input_width = input_array.shape
    kernel_height, kernel_width = kernel_size
    stride_y, stride_x = stride

    if len(filter) == 0:
        filter = [[random.uniform(-1, 1) for _ in range(kernel_width)] for _ in range(kernel_height)]
    
    filter = np.array(filter)

    if padding == 'same':
        pad_height = max((input_height - 1) // stride_y + 1, input_height) * stride_y + kernel_height - input_height - stride_y
        pad_width = max((input_width - 1) // stride_x + 1, input_width) * stride_x + kernel_width - input_width - stride_x
        input_array = np.pad(input_array, ((pad_height // 2, pad_height - pad_height // 2),
                                           (pad_width // 2, pad_width - pad_width // 2)), mode='constant')

    input_height, input_width = input_array.shape
    output_height = (input_height - kernel_height) // stride_y + 1
    output_width = (input_width - kernel_width) // stride_x + 1
    output_array = np.zeros((output_height, output_width))

    for y in range(0, input_height - kernel_height + 1, stride_y):
        for x in range(0, input_width - kernel_width + 1, stride_x):
            region = input_array[y:y+kernel_height, x:x+kernel_width]
            output_array[y // stride_y, x // stride_x] = np.sum(region * filter)

    return output_array

def multiple_filter(input_array, kernel_size, stride, padding='valid', filter=[], iterations=1):
    img = input_array
    i = 0
    while i < iterations:
        i+=1
        img = filter_operation(img, kernel_size, stride, padding, filter)

    return img

img_path = "C:\\Users\\joaoc\\OneDrive\\Área de Trabalho\\7 semestre\\Inteligencia Artificial\\chap10\\apresentacao\\resized\\1.jpg"

img = process_img(path=img_path)
#print_img(img)

#img_max_pool = pooling_operation(img, (2, 2), (2, 1), 'valid', 'max')
#plot_images([img, img_max_pool])


#img_avg_pool = pooling_operation(img, (4, 4), (2, 2), 'same', 'average')
#plot_images([img, img_avg_pool])

#img_avg_pool5 = multiple_pooling(img, (2, 2), (1, 1), 'same', 'average', 5)
#plot_images([img, img_avg_pool5])

#img_max_pool5 = multiple_pooling(img, (2, 2), (1, 1), 'same', 'max', 4)
#plot_images([img, img_max_pool5])

img_filtered = filter_operation(img, (3,3), (1,1), 'same', [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
#plot_images([img, img_filtered])

img_filtered_pooled = multiple_pooling(img_filtered, (2, 2), (1, 1), 'same', 'average', 8)
plot_images([img_filtered, img_filtered_pooled])

#img_multi_filtered = multiple_filter(img, (2,2), (1,1), 'same', iterations=1)
#plot_images([img, img_multi_filtered])
