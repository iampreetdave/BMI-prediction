# ------------------------------
# KNN for BMI Classification
# ------------------------------

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#  Load dataset
df = pd.read_csv("bmi.csv")

# Separate features (X) and target (y)
X = df[['Height', 'Weight']]  # Features
y = df['Index']               # Target category

#  Encode target labels (e.g., "Normal" → 0, "Overweight" → 1, etc.)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Create & train the KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f" KNN Model Accuracy: {accuracy:.2f}")


# Example prediction
example_height = 175
example_weight = 70
predicted_class = knn.predict([[example_height, example_weight]])[0]
predicted_label = label_encoder.inverse_transform([predicted_class])[0]
print(f"Example: Height={example_height}cm, Weight={example_weight}kg → {predicted_label}")
