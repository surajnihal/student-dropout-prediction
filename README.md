# Predicting College Dropout Risk with Machine Learning

A data analysis exploring college dropout patterns using academic, demographic, and economic data. If you're interested in the *why* behind this, [read the full story on Substack](https://open.substack.com/pub/databooai/p/why-dropouts-deserve-our-attention?r=5g7mt9&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true) for a deep dive.

![img](https://github.com/user-attachments/assets/22eaed90-dff2-40c7-80fe-911755551cfa)
<sub>Image courtesy of [Colossal](https://www.thisiscolossal.com)</sub>

## 📌 Overview

Every year, millions of students leave college without a degree. But what if we could predict who's most at risk — early enough to help?

This analysis explores that question using a dataset from a Portuguese university. By combining demographic, socioeconomic, academic, and macroeconomic features, and running a set of machine learning models, we try to identify students likely to drop out before it happens.

## 🧠 What This Project Covers

- **Exploratory Data Analysis (EDA)** using custom functions to understand student behavior  
- **Multicollinearity detection** to ensure clean model inputs  
- **Three time-stage datasets (S0, S1, S2)** for a longitudinal modeling approach  
- **Imbalanced classification problem** solved using data-level and algorithm-level techniques (e.g., SMOTE, Balanced Random Forest)  
- **Modeling with CatBoost, LightGBM, XGBoost, Random Forest, and Ensemble methods**  
- **Evaluation** using F1 scores and Balanced Accuracy  

## 📂 File Structure

```bash
├── data.csv                 # Cleaned student dataset
├── eda.ipynb                # Exploratory data analysis
├── datamodels.ipynb         # Modeling pipeline and results
├── helper.py                # Custom describe function for EDA
├── requirements.txt         # Python dependencies
└── README.md                # You're here!
```

# ⚙️ How to Run This Project

**Clone the repo**

Install dependencies:

```bash
pip install -r requirements.txt
```

## 📂 Open the Notebooks

- Start with `eda.ipynb` to explore the data  
- Then go to `datamodels.ipynb` to check out the modeling work  

Preferred Python version and packages are listed in `requirements.txt`.

---

## 📈 Key Findings *(Spoiler Alert)*

- **Academic performance** and **financial responsibility** were top predictors of dropout  
- **Dropout risk can be spotted early**, but prediction accuracy improves significantly after the **first semester**  
- **Balanced Random Forest (BRF)** delivered the most reliable results in this **imbalanced, three-class problem**

---

## 📝 Blog & Deep Dive

Want to understand the story behind the code? Why dropout prediction matters? What features made a difference? Check out the full blog post:

👉 **[Read it on Substack](https://open.substack.com/pub/databooai/p/why-dropouts-deserve-our-attention?r=5g7mt9&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true)**

---

## 🧾 License

This project is licensed under the **MIT License**.
