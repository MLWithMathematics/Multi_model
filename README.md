# 🌿 Multi-Model ML Web App (Plant Disease + House Price Prediction)

## 🚀 Overview

This project is a **Streamlit-based web application** that integrates **two machine learning models** into a single interface:

1. 🌱 **Plant Disease Recognition Model (CNN - TensorFlow)**
2. 🏠 **California House Price Prediction Model (Regression - Scikit-learn)**

The app allows users to:

* Upload plant leaf images and detect diseases
* Enter housing data and predict house prices

---
🌿 Plant Disease Model – Test Dataset Validation
📌 Purpose

To ensure reproducibility and transparency, this project includes a curated test image dataset. Users can validate model performance using these predefined samples and compare predicted outputs with actual labels.

📂 Test Dataset Location
project/
│
├── test_images/
│   ├── Apple___Black_rot/
│   │   ├── img1.jpg
│   │   ├── img2.jpg
│   │
│   ├── Tomato___Healthy/
│   │   ├── img3.jpg
│   │   ├── img4.jpg
│   │
│   └── ...

👉 Each folder name represents the true class label.

▶️ How to Run the App
streamlit run Web.py
🧪 How to Test Using Provided Dataset
Open the app in your browser
Navigate to 🌿 Plant Disease Prediction from the sidebar
Upload an image from the test_images/ folder
Observe:
✅ Predicted Class
📊 Confidence Score
📊 Expected Behavior
The predicted label should match the folder name (ground truth)
High confidence (>80%) is expected for most samples
Some misclassifications may occur due to:
Similar disease patterns
Image quality variations
✅ Example Test Case
Image Path	Actual Label	Predicted Label	Confidence
Apple___Black_rot/img1.jpg	Black Rot	Black Rot	92.4%
Tomato___Healthy/img3.jpg	Healthy	Healthy	97.1%
⚠️ Notes
  Images are resized to 128×128 before inference
  Model was trained on 38 plant disease classes
  Ensure good lighting and clear leaf visibility for best results

## 🧠 Models Used

### 🌱 Plant Disease Model

* Type: Convolutional Neural Network (CNN)
* Framework: TensorFlow / Keras
* Input: Image (128x128)
* Output: 38 plant disease classes
* File: `Trained_my_Model.h5`

---

### 🏠 House Price Model

* Type: Regression (HistGradientBoostingRegressor)
* Framework: Scikit-learn
* Pipeline Includes:

  * Missing value imputation
  * Standard scaling
  * One-hot encoding
* File: `house_price_model.pkl`

---

## 📁 Project Structure

```
project/
│
├── Web.py                      # Main Streamlit app
├── requirements.txt           # Dependencies
├── house_price_model.pkl      # House price model
├── PD.jpg                     # Home page image
├── .gitignore
└── assets/ (optional)
```

> ⚠️ Note: Large model (`Trained_my_Model.h5`) is NOT included in repo. It is downloaded at runtime.

---

## ⚙️ Features

* ✅ Multi-model support in one UI
* ✅ Image upload & prediction
* ✅ Structured input form for regression
* ✅ Confidence score display
* ✅ Clean and user-friendly interface
* ✅ Works locally and deployable online

---

## 🖥️ Run Locally (Windows)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\\Scripts\\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Streamlit App

```bash
streamlit run Web.py
```

---

### 5️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📦 Handling Large Model (Important)

The plant disease model (~120MB) is downloaded automatically using:

```python
import gdown
```

Make sure:

* Internet connection is available
* Google Drive link is correct

---

## 🧾 Requirements

```
streamlit
tensorflow
numpy
pandas
scikit-learn
joblib
matplotlib
opencv-python-headless
gdown
```

---

## ⚠️ Common Issues & Fixes

### ❌ Model not loading

* Check file path
* Ensure `.h5` file downloaded properly

---

### ❌ Git push rejected

```bash
git pull origin main --rebase
git push origin main
```

---

### ❌ Large file issue (>100MB)

* Use Google Drive / HuggingFace
* Add to `.gitignore`

---

## 🌍 Deployment

You can deploy this project on:

* Streamlit Cloud
* Hugging Face Spaces
* Render / Railway

---


---

## 👨‍💻 Author

**Shubhankar**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

---
