# 🧠 Image Classifier using Deep Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 📌 Overview

This project implements an **Image Classification System** using three powerful deep learning architectures:

* 🔹 MobileNetV2
* 🔹 VGG16
* 🔹 Xception (**Best Performing Model**)

The models are trained on a custom dataset and evaluated using accuracy, loss, and confusion matrix.

---

## 🖼️ Sample Workflow

<p align="center">
  <img src="https://via.placeholder.com/600x300.png?text=Upload+Image+→+Prediction+→+Result" alt="workflow">
</p>

---

## 🤖 Model Performance

| Model       | Accuracy | Notes              |
| ----------- | -------- | ------------------ |
| MobileNetV2 | ⭐⭐⭐⭐☆    | Lightweight & fast |
| VGG16       | ⭐⭐⭐⭐☆    | Deep architecture  |
| Xception    | ⭐⭐⭐⭐⭐    | Best accuracy      |

---

## 📥 Download Trained Models

Due to GitHub size limits, models are hosted externally:
* 📦 jsonfiles → [Download](PASTE_LINK_1)
* 📦 MobileNetV2 → [Download](https://drive.google.com/file/d/1aRjUF3QG3hB8h84V3MH5nInaLZxXejrq/view?usp=sharing)
* 📦 VGG16 → [Download](https://drive.google.com/file/d/1VWrufmeoylh1RA3HWFiyOD5-0ZZu_9id/view?usp=sharing)
* 📦 Xception → [Download](https://drive.google.com/file/d/1m_lFpgepqfLXKdkLl98DpuaIdMOFsLRd/view?usp=sharing)

---

## 🚀 How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ssreeshanth/image_classifier.git
cd image_classifier
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup Models

* Download models from above links
* Place them inside:

```
models/
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

---

## 📁 Project Structure

```
image_classifier/
│── notebooks/
│   └── final_model.ipynb
│── src/
│   ├── model_loader.py
│   ├── predict.py
│   └── utils.py
│── models/            # Add downloaded .h5 models here
│── app.py
│── requirements.txt
│── README.md
```

---

## 📊 Outputs

* ✅ Image Classification Results
* 📉 Loss & Accuracy Graphs
* 📊 Confusion Matrix

---

## ☁️ Run on Google Colab

Prefer quick testing?

1. Open Google Colab
2. Upload `final_model.ipynb`
3. Set dataset paths
4. Run all cells

---

## ⚠️ Important Notes

* Python **3.10** is recommended
* TensorFlow must be installed
* Update dataset paths before running

---

## 🔮 Future Improvements

* 🌐 Deploy as a web app (Streamlit)
* 📱 Convert to mobile app
* ⚡ Optimize inference speed

---

## 👨‍💻 Author

**Sreeshanth**
📌 Passionate about AI & Deep Learning

---

## ⭐ Show Your Support

If you like this project:

* ⭐ Star this repository
* 🍴 Fork it
* 🧠 Explore and improve it

---

<p align="center">
  🚀 Built with Deep Learning & Passion
</p>
