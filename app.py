import os
from src.model_loader import load_models
from src.predict import predict_image

def main():
    print("🧠 Image Classifier")
    print("-------------------")

    models = load_models()

    if not models:
        print("❌ No models loaded. Check your /models folder.")
        return

    img_path = input("📂 Enter image path: ").strip()

    if not os.path.exists(img_path):
        print("❌ Image not found!")
        return

    print("\n🔍 Predictions:\n")

    for name, model in models.items():
        label, pred = predict_image(model, img_path)
        print(f"{name.upper()} → {label}")

if __name__ == "__main__":
    main()
