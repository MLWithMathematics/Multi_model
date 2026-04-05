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

## 🌿 Try the Plant Disease Detection Model (Live Demo)

You can test the model directly using the deployed Streamlit app:

👉 **Live App:**   https://ml-prediction-system.streamlit.app/

---

### 🚀 How to Use the Web App

1. Open the live app using the link above.
2. From the sidebar, select **"Plant Disease Prediction"**.
3. Upload a plant leaf image.
4. Click on **Predict**.
5. View:

   * 🌱 Predicted disease class
   * 📊 Confidence score

---

### 🧪 Recommended Testing (Using Provided Dataset)

For consistent and verifiable results, use images from the repository:

```id="6y3z8k"
/test_images/
```

#### Steps:

1. Download or clone this repository:

```bash id="x1n9pd"
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Navigate to the `/test_images/` folder.

3. Choose any image from a class folder (e.g.):

```
test_images/Tomato___Early_blight/
```

4. Upload that image in the web app.

---

### ✅ Expected Results

* The prediction should match the **folder name (actual class)**.
* Confidence scores are typically **high (>80%)** for correct predictions.
* Occasional errors may occur due to model limitations.

---

### 📌 Example

| Image Source                           | Actual Class    | Expected Prediction |
| -------------------------------------- | --------------- | ------------------- |
| test_images/Apple___Black_rot/img1.jpg | Apple Black Rot | Apple Black Rot     |

---

### ⚠️ Notes

* Best results are obtained with:

  * Clear images
  * Single leaf in frame
* Avoid blurry or multiple-leaf images.
* External images may give less accurate results.

---

### 💡 Quick Tip

To quickly verify the model:

* Pick any random image from `/test_images/`
* Upload it to the app
* Check if prediction matches the folder name

---

### 🎯 What This Demonstrates

* Real-world usability via web interface
* Model accuracy on known test samples
* Reproducible and transparent evaluation

---

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
