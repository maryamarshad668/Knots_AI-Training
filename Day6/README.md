# Day 6 — Neural Networks (CS50 AI)

Mini project covering backpropagation, fully-connected networks, and CNNs.

## Files

```
day6_project/
├── backprop_scratch.py   # Manual 2-layer neural net, no frameworks
├── mnist_classifier.py   # MNIST digit classifier with Keras
└── traffic_cnn.py        # Traffic sign CNN classifier
```

## backprop_scratch.py

Implements a 2-layer neural network (input → hidden ReLU → output Sigmoid) from scratch using only NumPy — forward pass, backward pass, and gradient updates via the chain rule.

- Xavier weight initialization
- Trained and tested on the XOR problem
- Run: `python backprop_scratch.py`

## mnist_classifier.py

Fully-connected network classifying MNIST handwritten digits with Keras.

- Dense(256) → Dropout(0.3) → Dense(128) → Dropout(0.3) → Dense(10, softmax)
- Adam optimizer, sparse categorical crossentropy
- EarlyStopping + ModelCheckpoint callbacks
- Saves misclassified examples to `misclassified.png`
- Target: >97% test accuracy
- Run: `python mnist_classifier.py`

## traffic_cnn.py

CNN classifier for traffic sign images (CIFAR-10 used as a GTSRB substitute — swap in real GTSRB data and set `num_classes = 43` if available).

- Conv2D(32) → MaxPool → Conv2D(64) → MaxPool → Flatten → Dense(128) → Dropout(0.5) → Dense(num_classes, softmax)
- Images resized to 30x30x3
- EarlyStopping + ModelCheckpoint callbacks
- Model saved to `traffic_model/`
- Target: >90% test accuracy
- Run: `python traffic_cnn.py`

## Requirements

```
tensorflow
numpy
matplotlib
```

Install with:

```
pip install tensorflow numpy matplotlib
```