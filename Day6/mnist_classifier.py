import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 784).astype("float32") / 255.0
X_test = X_test.reshape(-1, 784).astype("float32") / 255.0
model = keras.Sequential([
    keras.layers.Dense(256, activation="relu", input_shape=(784,)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation="softmax"),
])
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss="sparse_categorical_crossentropy", metrics=["accuracy"])
callbacks = [
    keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
    keras.callbacks.ModelCheckpoint("best_model.h5", save_best_only=True),
]
history = model.fit(X_train, y_train, validation_split=0.1, epochs=10, batch_size=32, callbacks=callbacks)
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")
preds = np.argmax(model.predict(X_test), axis=1)
wrong = np.where(preds != y_test)[0][:5]
fig, axes = plt.subplots(1, 5, figsize=(10, 2))
for ax, idx in zip(axes, wrong):
    ax.imshow(X_test[idx].reshape(28, 28), cmap="gray")
    ax.set_title(f"P:{preds[idx]} T:{y_test[idx]}")
    ax.axis("off")
plt.savefig("misclassified.png")
plt.show()