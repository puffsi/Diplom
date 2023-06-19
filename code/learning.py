from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Flatten, Dense
from tensorflow import keras


def learning (train_dir, val_dir, where_to_save):
        train_samples =1134
        val_samples = 330
        datagen = ImageDataGenerator(rescale=1. / 255)
        img_width, img_height = 150, 150
        input_shape = (img_width, img_height, 3)
        epochs = 20
        batch_size = 90

        train_generator = datagen.flow_from_directory(
            train_dir,
            target_size=(img_width, img_height),
            batch_size=batch_size,
            class_mode='categorical')

        val_generator = datagen.flow_from_directory(
            val_dir,
            target_size=(img_width, img_height),
            batch_size=batch_size,
            class_mode='categorical')

        model = Sequential()

        model.add(Conv2D(32, (5, 5), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(32, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(64, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3), input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(128))
        model.add(Activation('relu'))
        model.add(Dense(4))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy', keras.metrics.Recall(), keras.metrics.Precision()])

        model.fit_generator(
            train_generator,
            steps_per_epoch=train_samples // batch_size,
            validation_data=val_generator,
            validation_steps=val_samples // batch_size,
            epochs=epochs
        )


        model.save(where_to_save)
        return 0