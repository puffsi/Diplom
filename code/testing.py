from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras

def test(test_dir, model_adr):
  datagen = ImageDataGenerator(rescale=1. / 255)
  img_width, img_height = 200, 250
  input_shape = (img_width, img_height, 3)
  batch_size = 32
  test_generator = datagen.flow_from_directory(
      test_dir,
      target_size=(img_width, img_height),
      batch_size=batch_size,
      class_mode='categorical')

  model = keras.models.load_model(model_adr)
  scores = model.evaluate_generator(test_generator, steps = len(test_generator))

  str = ("Аккуратность на тестовых данных: %.2f%%" % (scores[1]*100))
  return str