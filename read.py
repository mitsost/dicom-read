import os
import pydicom  # pydicom is a package for working with DICOM files
from pydicom import dcmread
import numpy as np
from PIL import Image

file_list = os.listdir('images')
e = len(file_list)
# print(file_list)

# Loop through the images in the directory
image_count = 0
for i in range(0, e):
    try:
        ds = pydicom.dcmread(f'images/{file_list[i]}')
        print(ds)
        new_image = ds.pixel_array.astype(float)
        scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0
        scaled_image = np.uint8(scaled_image)
        final_image = Image.fromarray(scaled_image)
        # final_image.show()
        final_image.save(f'final_images/{file_list[i]}.png')
        image_count += 1
    except FileNotFoundError:
        print(f"File {file_list[i]} not found.")
        break

print(f"Total images processed: {image_count}")