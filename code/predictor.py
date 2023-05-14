from tensorflow import keras
from IPython.display import Image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
from PIL import  Image

def predictior(img_path, model_adr):
  image = Image.open(img_path)
  new_image = image.resize((200,250))
  new_image.save(img_path)
  model = keras.models.load_model(model_adr, compile = False)
  classes = ['office', 'everyday', 'sport', 'party']
  img = load_img(img_path, color_mode="rgb")
  x = img_to_array(img)
  x = x.reshape(1, 200, 250, 3)
  prediction = model.predict(x)
  prediction = np.argmax(prediction)
  guess = ("It's a " + str(classes[prediction] + " style."))
  image.close()
  new_image.close()
  return guess