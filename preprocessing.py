import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/forecast_starting_data.csv")
print(df['mth_code'].unique())
chargeoffs_by_month = df.groupby(['mth_code']).agg({'charge_off': 'sum'})
print(chargeoffs_by_month)
# print(df["mth_code"])