import pandas as pd
import numpy as np
import torch
import os
import torch.utils.data as data_utils
import matplotlib.pyplot as plt 
import seaborn as sns
from tqdm import tqdm

df = pd.read_csv("C:\\Users\\lukvi\\Python Fun\\Data Visualisation\\NBA Data\\triple_doubles.csv")
df["season"] = df["season"].astype("string").transform(lambda x: x[-2:])
df_stats = df[["MIN","PTS","REB","AST","STL","BLK"]]
# print(df.head())

# TD leaders
df_counts = df.groupby("player",as_index=False).apply(lambda x: x)["player"].value_counts()
#df_leaders = df.loc[df_counts[0,:5]]
print(df_counts.head())

df_print = df.groupby("season",as_index=True,sort=False).apply(lambda x: x.count())
df_stats_print = df.groupby("player",as_index=True,sort=False).apply(lambda x: x.describe())[["MIN","PTS","REB","AST","STL","BLK"]]
# df_stats_leaders_summary = df_leaders.groupby("player",as_index=True,sort=False).apply(lambda x: x.describe())[["MIN","PTS","REB","AST","STL","BLK"]]
print(df_stats_print)

# sns.pairplot(df_stats)
# plt.show()

