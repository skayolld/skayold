import pandas as pd

# 1️⃣ إنشاء بيانات تجريبية مباشرة في الكود
data = {
    "Product": ["Phone", "Laptop", "Printer"],
    "Sales": [200, 800, 300],
    "Cost": [150, 600, 200],
    "Profit": [50, 200, 100],
    "Date": ["2025-08-15", "2025-08-16", "2025-08-17"],
    "Notes": ["NA", "N/A", "Delivered"]
}

df = pd.DataFrame(data)

# 2️⃣ حفظ البيانات في ملف CSV أول مرة (محاكاة قراءة ملف)
df.to_csv("data.csv", sep=";", encoding="utf-8", index=False, )
print("✅ data.csv تم إنشاؤه")

# 3️⃣ قراءة الملف مع الخيارات (مثل skiprows لو حاب نتجاهل صفوف)
df = pd.read_csv(
    "data.csv",
    encoding="utf-8",
    sep=";",
    na_values=["NA", "N/A"],
    usecols=["Product", "Sales", "Cost", "Profit", "Date", "Notes"]
)

print("\n📌 Data after reading:")
print(df)

# 4️⃣ إنشاء عمود جديد: Net_Profit = Profit - Cost
df["Net_Profit"] = df["Profit"] - df["Cost"]

# 5️⃣ حذف أي صف Net_Profit < 100
df = df[df["Net_Profit"] >= 100]

# 6️⃣ حذف عمود "Cost"
df.drop("Cost", axis=1, inplace=True)

# 7️⃣ إعادة ترتيب الفهرس
df.reset_index(drop=True, inplace=True)

# 8️⃣ حفظ الملف النهائي
df.to_csv("data_processed.csv", sep=";", encoding="utf-8", index=False)
print("\n✅ data_processed.csv تم حفظه بعد المعالجة")
print("\n📌 Final DataFrame:")
print(df)
