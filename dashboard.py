import pandas as pd

data = pd.read_csv("data_dashboard_large - data_dashboard_large.csv")
data['Date_Transaction'] = pd.to_datetime(data['Date_Transaction'])





