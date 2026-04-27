# NASA Space Mission Classification AI
## Documentation

### 1. Introduction
This project builds a simple machine learning model that predicts whether a NASA mission is manned or unmanned. The goal is to demonstrate basic AI development skills using a small, synthetic dataset.

### 2. Dataset
The dataset is generated inside the code. It includes:
- Mission name
- Launch year
- Destination
- Mission goal
- Mission type (label)

### 3. Preprocessing
Categorical features are encoded using LabelEncoder. The target variable is also encoded.

### 4. Model
A RandomForestClassifier is used because it is simple, stable, and works well with small datasets.

### 5. Testing
The dataset is split 80/20. Accuracy is calculated on the test set.

### 6. Results
The model achieves high accuracy due to the small and clean dataset.

### 7. Limitations
- Small dataset
- Synthetic data
- Limited mission types

### 8. Future Work
- Add real NASA data
- Expand mission categories
- Add more features
