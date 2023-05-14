import random
import numpy as np
import torch
import torchvision.transforms as transforms
from PIL import Image
#i = 1

#while i <= 1000:
def color_change(input_path, output_path):
  image = Image.open(input_path)
  b = random.uniform(0,1)
  c = random.uniform(0,1)
  s = random.uniform(0,1)
  h = random.uniform(0,0.5)
  transform = transforms.ColorJitter(
    brightness=b, contrast=c, saturation=s, hue=h)
  img = transform(image)
  img.save(output_path)
  return 0
  #i += 1