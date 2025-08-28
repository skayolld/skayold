import pandas as pd 
df = pd.read_csv("sales.csv")
print (df.head())

total_sales = df["Sales"].sum()
print (total_sales)

df["Profit"] = df ["Sales"] - df["Cost"]

# print (df)

top_sales = df[df["Sales"] > 1000]
print (top_sales)

top_sales.to_csv("top_sales.csv",index=False)
print ("top_sales.csv")