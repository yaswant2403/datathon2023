import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data/train_mini.csv")
# chargeoffs_by_month = df.groupby(['mth_code']).agg({'charge_off': 'sum'})
# print(chargeoffs_by_month)
# print(f"Here are the different fico_score_ranges: {df["bank_fico_buckets_20"].unique()}, hi!")
scores = [(581,600),(721,740),(761,850),(661,680),(601,620), (701,720), (621,640), (561,580), (641,660), (741,760), (681,700),(560,300)]
medians = [(tup[0] + tup[1])/2 for tup in scores]
# print(medians)
ranges = { }
for mid in medians:
    fico_range = scores[medians.index(mid)]
    if (fico_range[0] == 560):
        ranges['<=560'] = mid
    elif (fico_range[0] == 761):
        ranges['761+'] = mid 
    else:
        key = str(fico_range[0]) + '-' + str(fico_range[1])
        ranges[key] = mid
ranges['Exception'] = 0
ranges['Missing'] = 0
df2 = df.replace({"bank_fico_buckets_20": ranges})
df2.to_csv("range.csv")
# print(df2["bank_fico_buckets_20"].unique())