# 🏏 IPL Win Predictor

> Predict the winning probability of an IPL team during a live match using machine learning and real-time match inputs.

---

## 🚀 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![RandomForest](https://img.shields.io/badge/Random%20Forest-Model-green?style=for-the-badge)

---

## 📊 Project Overview

This project predicts the probability of a team winning an IPL match based on real-time inputs like score, overs, wickets, and playing teams. It’s built as an interactive **Streamlit** web app and uses a **Random Forest Classifier** trained on historical IPL data.

---

---

## 🔍 Workflow Summary

### 1. 🧮 Data Collection
- Source: Kaggle IPL dataset
- Focused on key match data per delivery

### 2. 🧼 Data Cleaning & Preprocessing
- Removed nulls, irrelevant data
- Engineered features: CRR, RRR, remaining balls/wickets
- Encoded categorical variables

### 3. 🧠 Model Building
- Tried Logistic Regression, Decision Trees, Random Forests
- Final model: RandomForestClassifier with tuned hyperparameters

### 4. 🔧 Model Tuning
- Best score: **99.79%** with:
  ```python
  n_estimators = 200
  max_depth = 20
  min_samples_split = 2
  ````

### 5. ⚙️ Final Optimization

* Deployed version uses `n_estimators=50` for faster runtime with negligible performance loss

---

## 🖼️ Screenshots

| Match Input Page                | Prediction Output                 |
| ------------------------------- | --------------------------------- |
| ![Screenshot 2025-06-10 130749](https://github.com/user-attachments/assets/0fcb074c-5945-4526-8d76-ce537ec93d32 | ![Screenshot 2025-06-10 130808](https://github.com/user-attachments/assets/7ddab97a-34e9-46c7-879a-53253cb1b68d) |



---

## 🧪 How to Use

1. **Clone the Repo**

   ```bash
   git clone https://github.com/Phoenixarjun/IPL-Probability-Predictor/
   cd IPL-Probability-Predictor
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**

   ```bash
   streamlit run app.py
   ```

4. **Use the Interface**

   * Select the **Batting** and **Bowling** team
   * Choose the **City** of the match
   * Enter:

     * Target Score
     * Current Score
     * Overs completed
     * Wickets lost
   * Click **Predict Probabilities**
   * View win probabilities, CRR, RRR, and match insights

---



## ✨ Author

**Naresh B A** – Full Stack Developer & ML Enthusiast
Connect: [LinkedIn](www.linkedin.com/in/naresh-b-a-1b5331243) 

---


