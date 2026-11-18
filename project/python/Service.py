import pandas as pd
import joblib

cat_cols = ['make', 'vehicle_class', 'transmission', 'fuel_type']

class Service:
    def __init__(self):
        self.model = joblib.load('./co2_model.pkl')
        self.r2 = joblib.load('./co2_model_R2.pkl')
    def predict(self, data) :
        sample = pd.DataFrame([{
            'engine_size': float(data['engine_size']),
            'cylinders' : int(data['cylinders']),
            'make': str(data['make']),
            'vehicle_class' : str(data['vehicle_class']),
            'transmission': str(data['transmission']),
            'fuel_type': str(data['fuel_type'])
        }])
        for col in cat_cols:
            sample[col] = sample[col].astype('category')
        pred = self.model.predict(sample)[0]
        return {'prediction': round(float(pred), 2), 'r2': round(float(self.r2), 4)} 
service = Service()
