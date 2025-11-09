# %%
import pandas as pd

df = pd.read_csv("AB_NYC_2019.csv")
print(df.head())
# %%
df.price.describe()

# %%
Q1 = df.price.quantile(0.25)
Q3 = df.price.quantile(0.75)
Q1,Q3
# %%
IQR = Q3 - Q1
IQR
# %%
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
lower_limit, upper_limit

# %%
df_clean = df[(df.price > lower_limit) & (df.price < upper_limit)]
df_clean.shape

# %%
df.price.describe()
df_clean.price.describe()
