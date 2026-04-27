from tensorflow.keras.models import load_model

def load_models():
    models = {
        "mobilenet": load_model("models/MobileNetV2.h5"),
        "vgg16": load_model("models/VGG16.h5"),
        "xception": load_model("models/Xception.h5")
    }
    return models
