
# 2️⃣ حفظ البيانات في ملف CSV أول مرة (محاكاة قراءة ملف)
df.to_csv("data.csv", sep=";", encoding="utf-8", index=False, line_terminator="\n")
print("✅ data.csv تم إنشاؤه")

# 3️⃣ قراءة الملف مع الخيارات (مثل skiprows لو حاب نتجاهل صفوف)
df = pd.read_csv(
    "data.csv",
    encoding="utf-8",
    sep=";",
    na_values=["NA", "N/A"],
    usecols=["Product", "Sales", "Cost", "Profit", "Date", "Notes"]
)