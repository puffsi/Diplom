import torchvision.transforms as transforms
from PIL import Image
#i = 1

#while i <= 1000:
def color_change(input_path, output_path, b,c,s,h):
  image = Image.open(input_path)
  if b == '':
    b = 0
  if c == '':
    c = 0
  if s == '':
    s = 0
  if h == '':
    h = 0
  transform = transforms.ColorJitter(
    brightness=float(b), contrast=float(c), saturation=float(s), hue=float(h))
  img = transform(image)
  img.save(output_path)
  return 0
  #i += 1