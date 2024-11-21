import numpy as np
import sys
from PIL import Image, UnidentifiedImageError
from scipy.ndimage import convolve

def process_image(img_array, iterations):
    kernel = np.ones((3, 3, 1), dtype=np.float32) / 9.0
    
    for _ in range(iterations):
        img_array = convolve(img_array, kernel, mode='constant', cval=0)
    
    return img_array

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            img = Image.open(sys.argv[1])
        except (FileNotFoundError, UnidentifiedImageError, ValueError, TypeError):
            raise Exception(
                "Please enter a valid image! The correct usage for this program is:\n"
                "\"python convolute_image.py {image_file_path} {iterations}\""
            )
        
        img_array = np.array(img, dtype=np.float32)

        try:
            iterations = int(sys.argv[2])
            if iterations < 1:
                raise ValueError
        except ValueError:
            raise Exception("Please enter a number greater than 0 for iterations")

        processed_array = process_image(img_array, iterations)
        processed_array = np.clip(processed_array, 0, 255).astype(np.uint8)

        # Create and display the processed image
        new_img = Image.fromarray(processed_array)
        new_img.show()
