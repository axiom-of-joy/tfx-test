import tensorflow as tf
from tensorflow.keras.applications import efficientnet

model = efficientnet.EfficientNetB7()
#preds = model.predict(efficientnet.preprocess(image))
#print(efficientnet.decode_predictions(preds))

print('Hello world')
