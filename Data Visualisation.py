import pandas as pd
import numpy as np
import torch
import os
import torch.utils.data as data_utils
import matplotlib.pyplot as plt 
import seaborn as sns
from tqdm import tqdm

# Loading the data
td = pd.read_csv("C:\\Users\\lukvi\\Python Fun\\NBA-Data\\triple_doubles.csv") 
td["season"] = td["season"].astype("string").transform(lambda x: x[-2:])

# The leaders' TDs
td_counts = td["player"].value_counts()
td_leaders = td.groupby("player",as_index=True,sort=False).apply(lambda x: x)[["MIN","PTS","REB","AST","STL","BLK"]]
td_leaders = td_leaders.loc[td_counts.index[0:5].to_list()]
td_leaders = td_leaders.reset_index().drop("level_1",axis=1)

# TD stats for all TDs
td_stats = td.groupby("player",as_index=True,sort=False).apply(lambda x: x.describe())[["MIN","PTS","REB","AST","STL","BLK"]]
td_means = td_stats.reset_index()[td_stats.reset_index()["level_1"] == "mean"]

# TD leaders' means
td_top_5 = td_stats.loc[td_counts.index[0:5].to_list()]
td_top_5_means = td_top_5.reset_index()[td_top_5.reset_index()["level_1"]=="mean"]


# Boxplots comparing the means of all players TD stats
# sns.catplot(td_means,kind="box")
# plt.show()

# Boxplots comparing stats by person
# westbrook_td = td_leaders[td_leaders["player"]=="Russell Westbrook"]
# sns.catplot(westbrook_td,kind="violin")
# plt.show()

# Boxplot comparing players by category
# g = sns.FacetGrid()
# sns.catplot(data=td_leaders,x="player",y="PTS",hue="player",kind="box")
# plt.show()

# Boxplot comparing players along all categories
# Need to transform wide into long format
td_leaders_long = td_leaders.melt(id_vars=["player"],var_name="stat")
sns.catplot(td_leaders_long,x="player",hue="player",y="value",kind="box",col="stat",col_wrap=3,legend=True,palette="hls").set(xticklabels=[])
plt.show()