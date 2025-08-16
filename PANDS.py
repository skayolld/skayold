


# data = {
#     "Name": ["Mohammad", "Ahmad", "Sara"],
#     "Age": [25, 30, 22],
#     "City": ["Amman", "Irbid", "Zarqa"]
# }


# df = pd.DataFrame(data)

# print(df)
# print(df["Name"])
# print(df.iloc[1])  # الصف الثاني (رقم 1 لأن العد يبدأ من 0)
# df.to_csv("mydata.csv", index=False)
# df2 = pd.read_csv("mydata.csv")
# print(df2)
# import pandas as pd

# data = {
#     "Name": ["Mohammad", "Ahmad", "Sara", "Omar"],
#     "Age": [25, 30, 22, 27],
#     "City": ["Amman", "Irbid", "Zarqa", "Amman"]
# }
# df = pd.DataFrame(data)
# filtered = df[df["Age"] > 25]
# print (filtered)
# أكبر من 25 ويسكن في عمان
# filtered = df[(df["Age"] > 25) & (df["City"] == "Amman")]
# print(filtered)

# أو يسكن في عمان أو إربد
# filtered = df[(df["City"] == "Amman") | (df["City"] == "Irbid")]
# print(filtered)
# الأشخاص اللي اسمهم يحتوي على 'a'
# filtered = df[df["Name"].str.contains("a", case=False)]
# print(filtered)
# عرض عمود الاسم فقط للأشخاص أكبر من 25 سنة
# result = df.loc[df["Age"] > 25, "Name"]
# print(result)
import pandas as pd  

# إنشاء بيانات تجريبية
data = {
    "City": ["Amman", "Amman", "Irbid", "Irbid", "Zarqa", "Zarqa"],
    "Product": ["Laptop", "Phone", "Laptop", "Phone", "Laptop", "Phone"],
    "Sales": [1200, 800, 1100, 700, 1000, 600],
    "Quantity": [3, 5, 2, 4, 3, 2]
}

df = pd.DataFrame(data)

print(df)
# city_sales = df.groupby("City")["Sales"].sum()
# print(city_sales)
# avg_quantity = df.groupby("Product")["Quantity"].mean()
# print(avg_quantity)
# stats = df.groupby("City").agg({
#     "Sales": ["sum", "mean", "max"],
#     "Quantity": "sum"
# })
# print(stats)
