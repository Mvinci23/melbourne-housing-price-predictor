# 🏠 Melbourne Housing Price Prediction

A machine learning project that predicts housing prices in Melbourne using multiple regression algorithms and advanced feature engineering techniques.

This project includes **data cleaning, feature engineering, model comparison, hyperparameter tuning, and model interpretation**.

---

# 📌 Project Overview

The goal of this project is to build a machine learning model capable of predicting house prices in Melbourne using property attributes such as:

- Rooms
- Distance from city
- Property type
- Landsize
- Building area
- Region
- Bathroom count
- Geographic coordinates
- And other property characteristics

The project evaluates multiple regression models and selects the best-performing model using cross-validation and hyperparameter tuning.

---

# 📂 Dataset



The dataset contains **34,857 records and 21 variables** describing properties in Melbourne.

### Key Details of Variables
Suburb
Address
Rooms: Number of rooms
Price: Price in Australian dollars, target variable
Method:
S = property sold
SP = property sold prior
PI = property passed in
PN = sold prior not disclosed
SN = sold not disclosed
NB = no bid
VB = vendor bid
W = withdrawn prior to auction
SA = sold after auction
SS = sold after auction price not disclosed
N/A = price or highest bid not available.
Type:
br = bedroom(s)
h = house,cottage,villa, semi,terrace
u = unit, duplex
t = townhouse
dev site = development site
o res = other residential.
SellerG: Real Estate Agent
Date: Date sold
Distance: Distance from CBD in Kilometres
Regionname: General Region (West, North West, North, North east ...etc)
Propertycount: Number of properties that exist in the suburb.
Bedroom2 : Scraped # of Bedrooms (from different source)
Bathroom: Number of Bathrooms
Car: Number of carspots
Landsize: Land Size in Metres
BuildingArea: Building Size in Metres
YearBuilt: Year the house was built
CouncilArea: Governing council for the area
Lattitude
Longtitude

Target Variable: 
- Price


---

# 🔧 Data Preprocessing

Several preprocessing steps were performed.

### Handling Missing Values

- Median imputation for numerical features
- Mode imputation for categorical features

### Feature Engineering

New features were created:

- Month_Sold
- Year_Sold
- Day_Sold
- Building_Age

These were derived from **Date** and **YearBuilt** columns.

### Outlier Handling

- Log transformation for skewed features
- IQR-based capping for extreme values

### Feature Removal

Columns removed:
- Address
- Date
- YearBuilt


---

# ⚙️ Machine Learning Pipeline

A Scikit-Learn pipeline was used for preprocessing and model training.

Preprocessing
│
├── Numerical Pipeline
│ ├── Median Imputation
│ └── StandardScaler
│
└── Categorical Pipeline
├── Mode Imputation
└── OneHotEncoder


---

# 🤖 Models Evaluated

The following regression models were trained and compared:

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Gradient Boosting
- AdaBoost
- XGBoost
- LightGBM
- CatBoost

---

# 📊 Model Performance

After evaluation, the top-performing models were:

| Model | RMSE | R² |
|------|------|------|
| **CatBoost** | **0.190** | **0.863** |
| LightGBM | 0.198 | 0.853 |
| XGBoost | 0.198 | 0.852 |
| Random Forest | 0.205 | 0.842 |

The **CatBoost model achieved the best performance**.

---

# 🔍 Hyperparameter Tuning

Two techniques were used:

### GridSearchCV
Used for structured parameter tuning.

### RandomizedSearchCV
Used for faster optimization with random parameter sampling.

Best model parameters (CatBoost):
- iterations = 1000
- depth = 9
- learning_rate = 0.1


---

# 📈 Feature Importance

Top predictive features include:

1. Regionname  
2. Distance  
3. Property Type  
4. Rooms  
5. Postcode  

These features have the highest impact on house price prediction.

---

# 📊 Final Model Performance

Cross-validation results:
- R² : 0.859 ± 0.015
- MAE : 0.141 ± 0.012
- RMSE : 0.192 ± 0.014
  

