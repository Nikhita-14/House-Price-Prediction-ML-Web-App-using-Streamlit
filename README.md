# 🏡 House Price Prediction Web App using Streamlit

A simple and interactive machine learning web app to predict house prices based on area, number of bedrooms, and bathrooms. Built using **Python**, **scikit-learn**, and **Streamlit**.

---

## 📌 Features

- 📈 Predicts house prices using a Linear Regression model  
- 🧮 Takes user input for area (sqft), bedrooms, and bathrooms  
- 📊 Displays a bar chart of average price by number of bedrooms  
- 🖥️ Interactive UI with Streamlit  

---

## 🛠️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Nikhita-14/House-Price-Prediction-ML-Web-App-using-Streamlit.git
cd House-Price-Prediction-ML-Web-App-using-Streamlit
```
### 2. Create Virtual Environment (Optional)
```bash
python -m venv venv
```
**On Windows:**  
```bash
venv\Scripts\activate
```
**On macOS/Linux:**  
```bash
source venv/bin/activate
```
---

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---

## 🚀 Run the Application

Make sure `house_price_model.pkl` is available in the project directory.
```bash
streamlit run app.py
```
The app will open automatically at: 
```bash
http://localhost:8501
```
---

## 📦 Requirements
```bash
- Python 3.7+
- streamlit
- pandas
- scikit-learn
- joblib
```
To install them:
```bash
pip install -r requirements.txt
```
---

## 🧠 How the Model Works

- Trained using Linear Regression from scikit-learn  
- Uses `Area_sqft`, `Bedrooms`, and `Bathrooms` as features  
- Model is saved with `joblib`  
- App loads the model and predicts based on user input
