import numpy as np
from tensorflow.keras.preprocessing import image
from src.utils import decode_prediction

def preprocess(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_image(model, img_path):
    img = preprocess(img_path)
    pred = model.predict(img)
    label = decode_prediction(pred)
    return label, pred
