from PIL import Image
from rembg import remove

#input_path – путь к изображению
#output_path – путь к предобработанному изображению
def delete_background(input_path, output_path):
 # i = 1
  #while i <= 2000:
    input = Image.open(input_path)# +  '.jpg')
    output = remove(input)
    output.save(output_path)# +  '.png')
    return 0
    #i += 1