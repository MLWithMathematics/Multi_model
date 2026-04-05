# 🌿 Multi-Model ML Web App (Plant Disease + House Price Prediction)

## 🚀 Overview

This project is a **Streamlit-based web application** that integrates **two machine learning models** into a single interface:

1. 🌱 **Plant Disease Recognition Model (CNN - TensorFlow)**
2. 🏠 **California House Price Prediction Model (Regression - Scikit-learn)**

The app allows users to:

* Upload plant leaf images and detect diseases
* Enter housing data and predict house prices

---
## 🌿 Testing Plant Disease Model (Using Provided Test Dataset)

To ensure consistent and verifiable results, this project includes a curated **test dataset** of plant leaf images inside the repository. Users are encouraged to test the model using only these images to reproduce expected outputs.

---

### 📁 Test Dataset Location

```
/test_images/
    ├── Apple___Black_rot/
    ├── Tomato___Early_blight/
    ├── Potato___Late_blight/
    └── ...
```

Each folder represents the **true class label** of the images it contains.

---
---

### 🧪 How to Test (Step-by-Step)

1. Launch the Streamlit app.
2. Navigate to **"Plant Disease Prediction"** from the sidebar.
3. Upload an image from the `/test_images/` folder.
4. Click on **Predict**.
5. Observe:

   * Predicted disease class
   * Confidence score

---

### ✅ Expected Behavior

* The predicted class should match the **folder name** (ground truth).
* Confidence scores should generally be **high (>80%)** for correct predictions.
* Minor misclassifications may occur due to model limitations.

---

### 📊 Example Test Case

| Image Path                                 | Actual Class        | Predicted Class     | Confidence |
| ------------------------------------------ | ------------------- | ------------------- | ---------- |
| test_images/Tomato___Early_blight/img1.jpg | Tomato Early Blight | Tomato Early Blight | 92.4%      |

---

### ⚠️ Important Notes

* Only use images from the provided `/test_images/` directory for consistent results.
* External images may produce unpredictable results due to domain differences.
* Ensure images are clear and contain a **single leaf**.

---

### 💡 Tip for Reviewers

For quick validation:

* Pick any random image from a folder
* Upload it in the app
* Verify if prediction matches folder name

This ensures **transparent and reproducible evaluation** of the model.

---

---

### 🎯 Goal

This testing setup demonstrates:

* Model reliability
* Real-world usability
* Reproducibility of results

---


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
