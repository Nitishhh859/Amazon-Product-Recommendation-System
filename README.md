# 🛒 Amazon Product Recommendation System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/) 
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) 

---

Welcome to the **Amazon-style Product Recommender**! 🚀  

This Python project predicts products a user might **love or find interesting** based on their past ratings using **collaborative filtering** and **similarity-based recommendations**. Perfect for anyone who wants to explore **recommender systems** or build their own e-commerce recommendation engine. 💡✨

---

## 🌟 Features

- 🔹 Item-based collaborative filtering with **cosine similarity**  
- 🔹 Personalized product recommendations per user 🎯  
- 🔹 Weighted scores for better quality suggestions 🌟  
- 🔹 Supports both **CSV** and **Word table** datasets 📝  
- 🔹 Easy to extend for larger datasets 📈  
- 🔹 Saves recommendations automatically to `outputs/` 📄  

---

## 📂 Project Structure

amazon-recommender/
│
├── data/ # Dataset folder (CSV or Word file)
├── src/ # Python scripts
│ └── amazon_recommendation_system.py
├── outputs/ # Recommended products saved here
├── README.md # Project overview
└── requirements.txt # Python dependencies


---

## 🚀 Getting Started

1. **Clone this repository** 📥

```bash
git clone https://github.com/yourusername/amazon-recommender.git
cd amazon-recommender
```
2. **Install dependencies** ⚙️

```bash
pip install -r requirements.txt
```
3. **Add your dataset** 🗃️
   - CSV or Word file (.docx) containing:
  ```nginx
user_id | product_id | rating
```
 - Place it in the data/ folder

4. **Run the recommender** 🐍💻
   
```bash
 python src/amazon_recommendation_system.py
```
5. **View recommendations** 🎯
   
- Top recommendations will be saved in
```bash
  outputs/user_recommendations.csv
  ```
