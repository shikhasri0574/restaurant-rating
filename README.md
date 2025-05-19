# 🍽️ Restaurant Rating ML Project

This project uses machine learning techniques to analyze and predict restaurant ratings based on features such as city, cuisines, price range, delivery availability, and more. It also includes a content-based recommendation system and a cuisine classification model.

## 📌 Project Objectives

1. **Rating Prediction:**  
   Predict a restaurant's aggregate rating using regression models.

2. **Recommendation System:**  
   Recommend restaurants based on user preferences such as cuisine and city.

3. **Cuisine Classification:**  
   Classify restaurants into cuisine categories using classification algorithms.

---

## 📂 Dataset

- **Source:** `Dataset.csv`  
- **Contains features:**  
  - City, Cuisines, Currency, Price Range, Online Delivery, Table Booking, etc.
  - Aggregate rating (target for regression)

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn (optional for visualization)
- [Weights & Biases](https://wandb.ai/) (for experiment tracking)

---

## 🧠 Models Used

| Task                  | Model(s)                  |
|-----------------------|---------------------------|
| Rating Prediction     | Linear Regression, Decision Tree Regressor |
| Recommendation System | Content-Based Filtering   |
| Cuisine Classification| Random Forest Classifier  |

---

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shikhasri0574/restaurant-rating.git
   cd restaurant-rating
