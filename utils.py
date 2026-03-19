# utils.py
import numpy as np

def cap_outliers(X):
    X = X.copy()
    num_cols = ['Air temperature [K]', 'Process temperature [K]',
                'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    for col in num_cols:
        Q1 = X[col].quantile(0.25)
        Q3 = X[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        X[col] = np.where(X[col] < lower, lower, X[col])
        X[col] = np.where(X[col] > upper, upper, X[col])
    return X
