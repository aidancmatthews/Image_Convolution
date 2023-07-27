import numpy as np
import time
import sys
from PIL import Image, UnidentifiedImageError

def get_neighbors(im, i, j):
    return im[max(i-1, 0):min(i+2, im.shape[0]), max(j-1, 0):min(j+2, im.shape[1])]

def calc_new_val(neighbors):
    num_pixels = neighbors.size // 3
    new_val = np.floor_divide(neighbors.sum(axis=(0, 1)), num_pixels)
    return new_val

if len(sys.argv) == 3:
    try:
        img = Image.open(sys.argv[1])
    except (FileNotFoundError, UnidentifiedImageError, ValueError, TypeError):
        raise Exception("Please enter a valid image! The correct usage for this program is in the form \"python convolute_image.py {image_file_path} {iterations}\"")
    img_array = np.array(img)

    iterations = int(sys.argv[2])

    if (iterations < 1):
        raise Exception("Please enter a number greater than 0")
    
    for i in range(iterations):
        neighbors_array = np.zeros_like(img_array)
        for row in range(img_array.shape[0]):
            for col in range(img_array.shape[1]):
                neighbors = get_neighbors(img_array, row, col)
                neighbors_array[row, col] = calc_new_val(neighbors)

        img_array = neighbors_array

    new_img = Image.fromarray(np.uint8(img_array))
    new_img.show()