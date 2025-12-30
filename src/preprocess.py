import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import os

def preprocess():
    # Load data
    train_df = pd.read_csv('data/train.csv')
    test_df = pd.read_csv('data/test.csv')
    
    print(f"Original Train Shape: {train_df.shape}")
    print(f"Original Test Shape: {test_df.shape}")

    # Combine for consistent encoding
    train_len = len(train_df)
    test_id = test_df['Id']
    
    # Drop Id as it's not a feature
    train_df.drop('Id', axis=1, inplace=True)
    test_df.drop('Id', axis=1, inplace=True)

    # Separate target
    y_train = train_df['SalePrice']
    train_df.drop('SalePrice', axis=1, inplace=True)
    
    # Log transform target (to fix skewness)
    y_train = np.log1p(y_train)

    # Combine
    all_data = pd.concat([train_df, test_df], axis=0).reset_index(drop=True)

    # --- Missing Values ---
    # Numerical: Fill with 0 or Median
    # LotFrontage: Median by Neighborhood
    all_data['LotFrontage'] = all_data.groupby('Neighborhood')['LotFrontage'].transform(lambda x: x.fillna(x.median()))
    
    # Others commonly 0 (area, count)
    for col in ('MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath', 'GarageCars', 'GarageArea'):
        all_data[col] = all_data[col].fillna(0)

    # Categorical: Fill with "None" (meaning no feature) or Mode
    # "None" meaning no feature
    for col in ('PoolQC', 'MiscFeature', 'Alley', 'Fence', 'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'MasVnrType'):
        all_data[col] = all_data[col].fillna('None')

    # "Mode" imputation for others (Functional, Electrical, KitchenQual, Exterior, SaleType, Utilities, MSZoning)
    for col in ('Functional', 'Electrical', 'KitchenQual', 'Exterior1st', 'Exterior2nd', 'SaleType', 'Utilities', 'MSZoning'):
        all_data[col] = all_data[col].fillna(all_data[col].mode()[0])

    # GarageYrBlt: if no garage, fill with 0
    all_data['GarageYrBlt'] = all_data['GarageYrBlt'].fillna(0)

    # --- Feature Engineering ---
    # 1. Total Floor Area (TotalSF)
    # 地下、1階、2階の面積を合計して「家の総面積」を算出
    all_data['TotalSF'] = all_data['TotalBsmtSF'] + all_data['1stFlrSF'] + all_data['2ndFlrSF']

    # 2. House Age & Remodel Age
    # 「売れた年 - 建てられた年」で築年数を算出
    all_data['HouseAge'] = all_data['YrSold'] - all_data['YearBuilt']
    all_data['RemodAge'] = all_data['YrSold'] - all_data['YearRemodAdd']

    # 3. Total Bathrooms
    # バスルームの総数を計算（ハーフバスは0.5換算）
    all_data['TotalBath'] = (all_data['FullBath'] + (0.5 * all_data['HalfBath']) +
                             all_data['BsmtFullBath'] + (0.5 * all_data['BsmtHalfBath']))

    # 4. Total Porch Area
    # ポーチやデッキの面積を合計
    all_data['TotalPorchSF'] = (all_data['OpenPorchSF'] + all_data['3SsnPorch'] +
                                all_data['EnclosedPorch'] + all_data['ScreenPorch'] +
                                all_data['WoodDeckSF'])
    
    # --- Encoding ---
    # Label Encoding for ordinal/categorical features used in tree models
    # Retrieving all categorical cols
    categorical_cols = all_data.select_dtypes(include=['object']).columns
    
    for col in categorical_cols:
        lbl = LabelEncoder() 
        all_data[col] = lbl.fit_transform(list(all_data[col].values))

    # Split back
    X_train = all_data[:train_len]
    X_test = all_data[train_len:]

    print(f"Processed Train Shape: {X_train.shape}")
    print(f"Processed Test Shape: {X_test.shape}")

    # Ensure directory exists
    os.makedirs('data/processed', exist_ok=True)

    # Save
    X_train.to_csv('data/processed/train_x.csv', index=False)
    y_train.to_csv('data/processed/train_y.csv', index=False)
    X_test.to_csv('data/processed/test_x.csv', index=False)
    test_id.to_csv('data/processed/test_id.csv', index=False)
    
    print("Preprocessing completed. Files saved to data/processed/")

if __name__ == "__main__":
    preprocess()
