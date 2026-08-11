import tensorflow as tf
from tensorflow import keras
import numpy as np
IMG_SIZE = 30
(X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()
X_train = tf.image.resize(X_train, (IMG_SIZE, IMG_SIZE)).numpy().astype("float32") / 255.0
X_test = tf.image.resize(X_test, (IMG_SIZE, IMG_SIZE)).numpy().astype("float32") / 255.0
y_train = y_train.flatten()
y_test = y_test.flatten()
num_classes = 10
model = keras.Sequential([
    keras.layers.Conv2D(32, (3,3), activation="relu", padding="same", input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(64, (3,3), activation="relu", padding="same"),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(num_classes, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
callbacks = [
    keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
    keras.callbacks.ModelCheckpoint("best_traffic_model.h5", save_best_only=True),
]
history = model.fit(X_train, y_train, validation_split=0.1, epochs=20, batch_size=64, callbacks=callbacks)
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
model.save("traffic_model")