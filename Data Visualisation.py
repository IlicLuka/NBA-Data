import pandas as pd
import numpy as np
import torch
import os
import torch.utils.data as data_utils
import matplotlib.pyplot as plt 
import seaborn as sns
from tqdm import tqdm

td = pd.read_csv("C:\\Users\\lukvi\\Python Fun\\NBA-Data\\triple_doubles.csv")
td["season"] = td["season"].astype("string").transform(lambda x: x[-2:])
td_stats = td.groupby("player",as_index=True,sort=False).apply(lambda x: x.describe())[["MIN","PTS","REB","AST","STL","BLK"]]
print(td_stats.head())

# TD leaders
td_counts = td["player"].value_counts()
td_top_5 = td_stats.loc[td_counts.index[0:5].to_list()]
print(td_top_5.index)

# sns.pairplot(df_stats)
# plt.show()
