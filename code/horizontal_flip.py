#!pip install --ignore-installed Pillow==9.3.0
import cv2
# i = 1
# while i <= 430:

def horizontal_flip(input_path, output_path):
    img = cv2.imread(input_path)
    img1 = cv2.flip(img, 1)
    cv2.imwrite(output_path, img1)
    return 0

# i += 1