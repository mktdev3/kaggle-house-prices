import pandas as pd
import numpy as np
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import Ridge
import xgboost as xgb
import lightgbm as lgb
from sklearn.metrics import root_mean_squared_error
import os

def train():
    print("Loading processed data...")
    X_train = pd.read_csv('data/processed/train_x.csv')
    y_train = pd.read_csv('data/processed/train_y.csv').values.ravel()
    X_test = pd.read_csv('data/processed/test_x.csv')
    test_id = pd.read_csv('data/processed/test_id.csv')

    print(f"Train Shape: {X_train.shape}")
    print(f"Target Shape: {y_train.shape}")

    # K-Fold CV
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    def rmse_cv(model):
        rmse = np.sqrt(-cross_val_score(model, X_train, y_train, scoring="neg_mean_squared_error", cv=kf))
        return rmse

    # --- Models ---
    print("Initializing models...")
    
    # 1. Ridge Regression (Linear Model)
    ridge = Ridge(alpha=1.0) # alpha could be tuned
    
    # 2. XGBoost
    xgboost = xgb.XGBRegressor(
        objective='reg:squarederror',
        n_estimators=1000,
        learning_rate=0.05,
        max_depth=3,
        min_child_weight=1,
        gamma=0.0,
        subsample=0.7,
        colsample_bytree=0.7,
        nthread=-1,
        random_state=42,
        verbosity=0
    )

    # 3. LightGBM
    lightgbm = lgb.LGBMRegressor(
        objective='regression',
        num_leaves=31,
        learning_rate=0.05,
        n_estimators=1000,
        verbose=-1,
        random_state=42
    )

    # --- Evaluation ---
    print("Evaluating Ridge...")
    score_ridge = rmse_cv(ridge)
    print(f"Ridge RMSE: {score_ridge.mean():.4f} (std: {score_ridge.std():.4f})")

    print("Evaluating XGBoost...")
    score_xgb = rmse_cv(xgboost)
    print(f"XGBoost RMSE: {score_xgb.mean():.4f} (std: {score_xgb.std():.4f})")

    print("Evaluating LightGBM...")
    score_lgb = rmse_cv(lightgbm)
    print(f"LightGBM RMSE: {score_lgb.mean():.4f} (std: {score_lgb.std():.4f})")

    # --- Training & Ensemble ---
    print("Training models on full data...")
    ridge.fit(X_train, y_train)
    xgboost.fit(X_train, y_train)
    lightgbm.fit(X_train, y_train)

    print("Predicting...")
    # Weighted Average (Simple Ensemble)
    # Giving slightly more weight to Gradient Boosting models
    pred_ridge = np.expm1(ridge.predict(X_test))
    pred_xgb = np.expm1(xgboost.predict(X_test))
    pred_lgb = np.expm1(lightgbm.predict(X_test))

    final_pred = (0.2 * pred_ridge) + (0.4 * pred_xgb) + (0.4 * pred_lgb)

    # --- Submission ---
    submission = pd.DataFrame()
    submission['Id'] = test_id['Id']
    submission['SalePrice'] = final_pred

    submission.to_csv('data/submission.csv', index=False)
    print("Submission saved to data/submission.csv")

if __name__ == "__main__":
    train()
