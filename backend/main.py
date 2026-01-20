import pandas as pd
from datetime import datetime

raw_data = {
    "t": [1726617600, 1726704000],
    "o": [100.5, 101.0],
    "h": [102.0, 103.5],
    "l": [99.5, 100.0],
    "c": [101.5, 102.5],
    "v": [1500, 1600],
}

df = pd.DataFrame(raw_data)

# Convert UNIX timestamps (seconds) to readable dates
df['Date'] = pd.to_datetime(df['t'], unit='s')

df.columns = ["Timestamp", "Open", "High", "Low", "Close", "Volume", "Date"]

# print(df['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

print(df)