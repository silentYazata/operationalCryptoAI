import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import requests

class OrderFlowPrediction:
    def __init__(self, api_url):
        self.api_url = api_url
        self.model = RandomForestClassifier()
        self.data = None

    def fetch_order_flow_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.data = pd.DataFrame(response.json())
        else:
            raise Exception("Failed to fetch data from API")

    def preprocess_data(self):
        # Assuming the data has columns 'price', 'volume', 'timestamp', etc.
        self.data['price_change'] = self.data['price'].diff()
        self.data['volume_change'] = self.data['volume'].diff()
        self.data.dropna(inplace=True)

    def train_model(self):
        features = self.data[['price_change', 'volume_change']]
        labels = (self.data['price_change'] > 0).astype(int)  # 1 if price goes up, else 0
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def predict(self, new_data):
        return self.model.predict(new_data)

if __name__ == "__main__":
    api_url = "https://api.example.com/order_flow"  # Replace with actual API URL
    order_flow_predictor = OrderFlowPrediction(api_url)
    order_flow_predictor.fetch_order_flow_data()
    order_flow_predictor.preprocess_data()
    order_flow_predictor.train_model()