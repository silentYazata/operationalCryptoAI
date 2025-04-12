import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import numpy as np

class TradeModel:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def preprocess_data(self):
        # Example preprocessing: fill missing values and create features
        self.data.fillna(method='ffill', inplace=True)
        self.data['price_change'] = self.data['close'].pct_change()
        self.data['volume_change'] = self.data['volume'].pct_change()
        self.data.dropna(inplace=True)

    def train(self):
        self.preprocess_data()
        X = self.data[['price_change', 'volume_change']]
        y = self.data['close'].shift(-1).dropna()
        X = X.iloc[:-1]  # Align X with y

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model trained with MSE: {mse}')

    def save_model(self, filename='trade_model.pkl'):
        joblib.dump(self.model, filename)

    def load_model(self, filename='trade_model.pkl'):
        self.model = joblib.load(filename)

    def predict(self, features):
        return self.model.predict(np.array(features).reshape(1, -1))

# Example usage:
# data = pd.read_csv('historical_trade_data.csv')  # Load your historical data
# trade_model = TradeModel(data)
# trade_model.train()
# trade_model.save_model()