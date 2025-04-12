import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

class FakeVolumeDetector:
    def __init__(self, volume_data):
        self.volume_data = volume_data
        self.model = IsolationForest(contamination=0.1)

    def preprocess_data(self):
        # Convert volume data to DataFrame for processing
        df = pd.DataFrame(self.volume_data, columns=['timestamp', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
        return df

    def detect_fake_volume(self):
        df = self.preprocess_data()
        # Fit the model
        self.model.fit(df[['volume']])
        # Predict anomalies
        df['anomaly'] = self.model.predict(df[['volume']])
        # Mark fake volumes as -1
        fake_volumes = df[df['anomaly'] == -1]
        return fake_volumes

    def get_fake_volume_alerts(self):
        fake_volumes = self.detect_fake_volume()
        alerts = []
        for index, row in fake_volumes.iterrows():
            alerts.append(f"Fake volume detected: {row['volume']} at {index}")
        return alerts

# Example usage:
# volume_data = [(timestamp1, volume1), (timestamp2, volume2), ...]
# detector = FakeVolumeDetector(volume_data)
# alerts = detector.get_fake_volume_alerts()
# for alert in alerts:
#     print(alert)