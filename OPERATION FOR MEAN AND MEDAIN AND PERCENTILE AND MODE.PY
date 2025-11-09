# %%
import pandas as pd
import re
import numpy as np

# %%

# Read and clean the file more flexibly
df = pd.read_csv(
    "DATA.CSV",
    sep=r"[\s,]+",     
    engine="python",  
    names=["name", "income"],  
    skiprows=[0],        
)
print(df)
# %%

df.describe() 
# %%
df.income.quantile(0.25)
# %%
df.income.quantile(0.25,interpolation="lower")

# %%
df.income.quantile(0.25)

# %%
percentile_99=df.income.quantile(0.25)
percentile_99
# %%
