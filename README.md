# 🧠 Image Classifier using Deep Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow">
  <img src="https://img.shields.io/badge/Models-MobileNetV2%20|%20VGG16%20|%20Xception-blueviolet">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
</p>

---

## 📌 Overview

This project implements an **Image Classification System** using three deep learning architectures:

* 🔹 MobileNetV2
* 🔹 VGG16
* 🔹 Xception (**Recommended – highest accuracy**)

The models are trained on a custom dataset and evaluated using:

* 📊 Accuracy & Loss
* 📉 Confusion Matrix

---

## 🖼️ Project Report

<p align="center">
  * 📦 Report → [Download](https://drive.google.com/file/d/1rYlUIJyN2EXxqa37S4E9spXZRwltxiZe/view?usp=sharing)
</p>

---

## 🤖 Trained Models

Due to GitHub file size limits, models are hosted externally:
* 📦 jsonfiles → [Download](https://drive.google.com/drive/folders/1jCjmUnZ-htvHyaP1yQcev0iMWI8-ZLVX?usp=sharing)
* 📦 MobileNetV2 → [Download](https://drive.google.com/file/d/1aRjUF3QG3hB8h84V3MH5nInaLZxXejrq/view?usp=sharing)
* 📦 VGG16 → [Download](https://drive.google.com/file/d/1VWrufmeoylh1RA3HWFiyOD5-0ZZu_9id/view?usp=sharing)
* 📦 Xception → [Download](https://drive.google.com/file/d/1m_lFpgepqfLXKdkLl98DpuaIdMOFsLRd/view?usp=sharing)

* 📦 ALL SAVED MODELS → [Download](https://drive.google.com/drive/folders/1FoseDMUss-tn7ktupO1bZk9pmaJQBwHv?usp=sharing)
📌 After downloading, place them inside:

```id="6ydy1h"
models/
```

---

## 🚀 Running the Project (VS Code)

### 1️⃣ Clone the Repository

```bash id="jptb0i"
git clone https://github.com/ssreeshanth/image_classifier.git
cd image_classifier
```

---

### 2️⃣ Setup Environment

Install Python **3.10** and create virtual environment:

```bash id="v9qg6z"
python -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash id="v1z6x9"
pip install tensorflow numpy matplotlib
```

---

### 4️⃣ Run the App

```bash id="w9c5ns"
python app.py
```

👉 Enter image path when prompted:

```id="4q0j4z"
sample.jpg
```

---

## 📁 Project Structure

```id="tbpt3l"
image_classifier/
│── notebooks/
│   └── final_model.ipynb
│── src/
│   ├── model_loader.py
│   ├── predict.py
│   └── utils.py
│── models/            # Place downloaded .h5 files here
│── app.py
│── README.md
│── requirements.txt
```

---

## 📊 Output

* ✅ Predicted Class Label
* 📉 Accuracy & Loss Graphs
* 📊 Confusion Matrix

---

## ☁️ Run in Google Colab (Easy Mode)

1. Open Google Colab
2. Upload `final_model.ipynb`
3. Download dataset
4. Update paths
5. Run all cells

---

## ⚠️ Important Notes

* Use **Python 3.10** (required for TensorFlow compatibility)
* Update dataset/model paths if running locally
* Ensure `.h5` models are inside `/models` folder

---

## 🔮 Future Improvements

* 🌐 Deploy as web app (Streamlit)
* 📱 Convert to mobile app
* ⚡ Optimize inference speed

---

## 👨‍💻 Author

**Sreeshanth**
AI & Deep Learning Enthusiast

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🚀 Build on top of it

---

<p align="center">
  🚀 Built with Deep Learning & Passion
</p>
