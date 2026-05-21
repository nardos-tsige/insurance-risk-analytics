\"\"\"Statistical modeling for risk-based pricing\"\"\"
 
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler, LabelEncoder 
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier 
from sklearn.linear_model import LinearRegression, LogisticRegression 
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, f1_score, precision_score, recall_score 
 
def prepare_features(df): 
    \"\"\"Prepare features for modeling\"\"\" 
    df_model = df.copy() 
    categorical_cols = ['Gender', 'Province', 'VehicleType'] 
    for col in categorical_cols: 
        if col in df_model.columns: 
            le = LabelEncoder() 
            df_model[col + '_encoded'] = le.fit_transform(df_model[col].astype(str)) 
    feature_cols = ['Age', 'AnnualIncome', 'RiskScore', 'PastClaims', 'AnnualPremium'] 
    feature_cols += [col + '_encoded' for col in categorical_cols if col in df_model.columns] 
    feature_cols = [col for col in feature_cols if col in df_model.columns] 
    return df_model, feature_cols 
 
def train_severity_model(df, feature_cols): 
    \"\"\"Train model to predict claim amount\"\"\" 
    claims_df = df[df['TotalClaims'] 
    X = claims_df[feature_cols].fillna(claims_df[feature_cols].median()) 
    y = claims_df['TotalClaims'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
    scaler = StandardScaler() 
    X_train_scaled = scaler.fit_transform(X_train) 
    X_test_scaled = scaler.transform(X_test) 
    model = RandomForestRegressor(n_estimators=100, random_state=42) 
    model.fit(X_train_scaled, y_train) 
    y_pred = model.predict(X_test_scaled) 
    r2 = r2_score(y_test, y_pred) 
    rmse = np.sqrt(mean_squared_error(y_test, y_pred)) 
    return model, scaler, r2, rmse 
 
def train_frequency_model(df, feature_cols): 
    \"\"\"Train model to predict claim probability\"\"\" 
    X = df[feature_cols].fillna(df[feature_cols].median()) 
    y = df['HasClaim'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
    scaler = StandardScaler() 
    X_train_scaled = scaler.fit_transform(X_train) 
    X_test_scaled = scaler.transform(X_test) 
    model = RandomForestClassifier(n_estimators=100, random_state=42) 
    model.fit(X_train_scaled, y_train) 
    y_pred = model.predict(X_test_scaled) 
    f1 = f1_score(y_test, y_pred) 
    accuracy = accuracy_score(y_test, y_pred) 
    return model, scaler, f1, accuracy 
 
def calculate_risk_premium(prob_claim, severity): 
    \"\"\"Calculate risk-based premium\"\"\" 
    expense_loading = 0.15 
    profit_margin = 0.10 
    return prob_claim * severity * (1 + expense_loading + profit_margin) 
