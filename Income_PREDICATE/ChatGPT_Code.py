import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# -----------------------------
# Load Excel file
# -----------------------------
file_path = "people.xlsx"
df = pd.read_excel(file_path)

# -----------------------------
# Check required columns
# -----------------------------
required_columns = [
    "ID", "Name", "State", "Height", "Weight",
    "Hair Length", "Facial Age Estimate",
    "Education Level", "ID Type", "Income"
]

for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

# -----------------------------
# Feature selection
# -----------------------------
X = df.drop(columns=["Income", "ID", "Name"])  # Remove non-predictive fields
y = df["Income"]

# -----------------------------
# Encode target variable
# -----------------------------
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# -----------------------------
# Identify column types
# -----------------------------
numeric_features = ["Height", "Weight", "Hair Length", "Facial Age Estimate"]
categorical_features = ["State", "Education Level", "ID Type"]

# -----------------------------
# Preprocessing
# -----------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", "passthrough", categorical_features)
    ],
    remainder="drop"
)

# Convert categorical variables to dummy variables
X = pd.get_dummies(X, columns=categorical_features)

# -----------------------------
# Train/Test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# -----------------------------
# Model training
# -----------------------------
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Evaluate model
# -----------------------------
y_pred = model.predict(X_test)

print("\nModel Performance:\n")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# -----------------------------
# Example: Predict new person
# -----------------------------
new_person = pd.DataFrame([{
    "State": "CA",
    "Height": 170,
    "Weight": 70,
    "Hair Length": 5,
    "Facial Age Estimate": 30,
    "Education Level": "Bachelor",
    "ID Type": "Driver License"
}])

new_person = pd.get_dummies(new_person)
new_person = new_person.reindex(columns=X.columns, fill_value=0)

prediction = model.predict(new_person)
predicted_income = label_encoder.inverse_transform(prediction)

print("\nPredicted Income Level:", predicted_income[0])