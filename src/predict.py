import numpy as np
from tensorflow.keras.preprocessing import image

def preprocess(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict(model, img_path):
    img = preprocess(img_path)
    preds = model.predict(img)
    return preds
