import pandas as pd
import numpy as np
df = pd.read_csv('./CO2 Emissions_Canada.csv')
df.info()

df = df.rename(columns={
    'Make': 'make', 'Vehicle Class': 'vehicle_class', 'Engine Size(L)': 'engine_size',
    'Cylinders': 'cylinders', 'Fuel Type': 'fuel_type', 'Transmission': 'transmission',
    'CO2 Emissions(g/km)': 'co2'
})

num_cols = ['engine_size', 'cylinders']
cat_cols = ['make', 'vehicle_class', 'transmission', 'fuel_type']
for col in cat_cols:
    df[col] = df[col].astype('category')
X = df[num_cols + cat_cols]
Y = df['co2']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)



import optuna
from lightgbm import LGBMRegressor, early_stopping
optuna.logging.set_verbosity(optuna.logging.WARNING)
def objective(trial):
    from sklearn.model_selection import KFold
    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    cv_r2_scores = []
    best_iterations = []
    for train_idx, val_idx, in cv.split(X_train, Y_train):
        X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        Y_tr, Y_val = Y_train.iloc[train_idx], Y_train.iloc[val_idx]
        model = LGBMRegressor(
            n_estimators=1000,
            learning_rate=trial.suggest_float('learning_rate', 0.01, 0.1),
            num_leaves=trial.suggest_int('num_leaves', 10, 30),
            max_depth=trial.suggest_int('max_depth', 3, 10),
            min_child_samples=trial.suggest_int('min_chlid_samples', 10, 50),
            subsample=trial.suggest_float('subsample', 0.6, 1.0),
            subsample_freq=1, verbose=-1, random_state=42, n_jobs=-1,
            colsample_bytree=trial.suggest_float('colsample_bytree', 0.6, 1.0),
        )
        model.fit(X_tr, Y_tr, eval_set=[(X_val, Y_val)], callbacks=[early_stopping(stopping_rounds=30, verbose=False)])
        r2 = model.score(X_val, Y_val)
        cv_r2_scores.append(r2)
        best_iterations.append(model.best_iteration_)
    trial.set_user_attr('best_n_estimators', int(np.mean(best_iterations)))
    return np.mean(cv_r2_scores)

sampler = optuna.samplers.TPESampler(seed=42)
study = optuna.create_study(direction='maximize', sampler=sampler)
study.optimize(objective, n_trials=20)
print('best params:', study.best_params)
print('cv r2:', study.best_value)
optimal_model = study.best_trial.user_attrs['best_n_estimators']

final_model = LGBMRegressor(
    random_state=42, verbose=-1, n_jobs=-1,
    **study.best_params,
    n_estimators=optimal_model
)
final_model.fit(X_train, Y_train)
print('train r2:', final_model.score(X_train, Y_train))
print('test r2:', final_model.score(X_test, Y_test))

r2 = final_model.score(X_test, Y_test)

import joblib
joblib.dump(final_model, './co2_model.pkl')
joblib.dump(r2, './co2_model_R2.pkl')
