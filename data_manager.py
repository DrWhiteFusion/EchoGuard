import pandas as pd
import os
from datetime import datetime

CSV_FILE = 'alert_log.csv'

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=['Timestamp', 'Alert Type', 'Confidence Score'])
        df.to_csv(CSV_FILE, index=False)

def log_alert(alert_type, confidence):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_row = pd.DataFrame({
        'Timestamp': [timestamp],
        'Alert Type': [alert_type],
        'Confidence Score': [confidence]
    })
    new_row.to_csv(CSV_FILE, mode='a', header=False, index=False)

def get_alerts_df():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=['Timestamp', 'Alert Type', 'Confidence Score'])

# Initialize the CSV if it doesn't exist
initialize_csv()