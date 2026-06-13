# 🛒 Product Recommendation System

A machine learning-based product recommendation system built using **TF-IDF Vectorization and Cosine Similarity**, deployed using Streamlit.

🔗 GitHub Repo:  
https://github.com/adheela/product-recommendation-system

---

# 🚀 Live Demo

https://product-recommendation-system-bsy1.onrender.com/

Deployed using Render:
https://render.com

---

# 📌 Features

- Product recommendation based on similarity
- TF-IDF + Cosine Similarity model
- Interactive Streamlit UI
- Dropdown product selection
- Fast and efficient recommendations

---

# 🧠 Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Pickle

---

# 📁 Project Structure

product-recommendation-system/
│
├── app.py
├── df.pkl
├── similarity.pkl
├── requirements.txt
├── README.md

---

# ⚙️ How It Works

1. Load product dataset
2. Combine product features (name, category, description)
3. Convert text into TF-IDF vectors
4. Compute cosine similarity matrix
5. Recommend similar products based on input selection

---

# 💻 Run Locally

## 1. Clone the repository
git clone https://github.com/adheela/product-recommendation-system.git
cd product-recommendation-system

## 2. Install dependencies
pip install -r requirements.txt

## 3. Run Streamlit app
streamlit run app.py

App runs at:
http://localhost:8501

---

# 📦 Required Files

Make sure these files exist in the repository:

- app.py
- df.pkl
- similarity.pkl
- requirements.txt

---

# 🌐 Deployment on Render

This project is deployed using Render.

## Step 1: Push code to GitHub
git add .
git commit -m "final project"
git push origin main

## Step 2: Create Web Service
- Go to https://render.com
- Click "New Web Service"
- Connect GitHub repository
- Select this project

## Step 3: Configure

Build Command:
pip install -r requirements.txt

Start Command:
streamlit run app.py --server.port 10000 --server.address 0.0.0.0

## Step 4: Deploy
Click Deploy and wait for live link.

---

# ⚠️ Common Issues

## FileNotFoundError
Make sure df.pkl and similarity.pkl are uploaded to GitHub

## App not loading
Check Start Command in Render settings

---

# 👨‍💻 Author

Adheela Farzana  
GitHub: https://github.com/adheela

---

# 📌 Future Improvements

- Add search bar instead of dropdown
- Improve UI design
- Add filters for better recommendations
- Deploy using Docker
