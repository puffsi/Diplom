from tensorflow import keras
from IPython.display import Image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
from PIL import  Image

def predictior(img_path, model_adr):
  image = Image.open(img_path)
  new_image = image.resize((150,150))

  new_image.save(img_path)
  model = keras.models.load_model(model_adr, compile = False)
  classes = ['office', 'everyday', 'sport',  'party']
  img = load_img(img_path, color_mode="rgb")
  x = img_to_array(img)
  x = x/255
  x = x.reshape(1, 150, 150, 3)
  prediction = model.predict(np.array(x))
  print(prediction)
  prediction = np.expand_dims(prediction,axis=0)
  #print(prediction)
  #prediction = np.argmax(prediction)
  #print(prediction)


  guess = str(prediction)

  image.close()
  new_image.close()
  return guess