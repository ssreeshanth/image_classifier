from tensorflow.keras.models import load_model
import os

MODEL_PATHS = {
    "mobilenet": "models/MobileNetV2.h5",
    "vgg16": "models/VGG16.h5",
    "xception": "models/Xception.h5"
}

def load_models():
    models = {}
    for name, path in MODEL_PATHS.items():
        if not os.path.exists(path):
            print(f"⚠️ Model not found: {path}")
            continue
        models[name] = load_model(path)
        print(f"✅ Loaded {name}")
    return models
