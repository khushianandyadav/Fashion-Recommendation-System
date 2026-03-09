import tensorflow as tf
print("TensorFlow version:", tf.__version__)

from tensorflow.keras.applications.resnet50 import ResNet50
model = ResNet50(weights='imagenet', include_top=False, input_shape=(224,224,3))
print("ResNet50 loaded successfully")
