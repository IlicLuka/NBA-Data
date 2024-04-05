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

df_summary = df.head()
print(df_summary)

########################################################################
## Apply to https://www.align-alytics.com/contact once confy with SQL ##
########################################################################


# List players' doubledouble Blks and rebounds