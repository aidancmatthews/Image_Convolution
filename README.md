# Image Convolution
## Goal
While browsing YouTube I found myself watching [But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA) by 3Blue1Brown. I was particularly interested in
the image processing section that covered, in part, the use of convolutions to blur an image. Through a few hours of a research and implementation, I have created this python
script for exactly this use.
## Requirements
- Python 3.*
- numpy
- Pillow
## Use
To run the provided script, navigate to the directory containing convolute_image.py and run
```console
> python ./convolute_image.py {image_file_path} {number_of_iterations}
```
This will generate a convolution of the provided image, processed according
to the provided iteration specifications, and open the image using the default
image viewer of the operating system.