# import csv 

# with open ("sales.csv", "r") as file :
#     reader = csv.reader(file)
    
#     for row in reader : 
#         print (row)



# another usage 

# i can use the pandas 

# import pandas  as pd  

# df = pd.read_csv("sales.csv")
# print (df.head())

# print (df.info())
# print(df.shape) 
# print (df.columns)
# print (df.describe())

# print (df["Product"])
# print(df["Sales"][:5])
# print (df.iloc[0])
# print (df.iloc[0:3,1:3])
# df.columns = df.columns.str.strip()


# df["Profit"] = df["Sales"] 
# print (df)

# high_sales = df[df["Sales"] > 400]
# print (high_sales)

# high_sales.to_csv("high_sales.csv", index=False)
# print(high_sales)

# df = df.drop("Profit", axis=1)
# print (df)

# df = df.drop(0, axis=0)
# print (df)

# df = df[df["Profit"] >= 50]
# print(df)
#df.reset_index(drop=True, inplace=True)
# import pandas as pd

# data = {
#     "Sales": [100, 200, 300],
#     "Cost": [50, 120, 180]
# }

# df = pd.DataFrame(data)
# df["Profit"] = df["Sales"] - df["Cost"]

# print("📌 DataFrame الأصلي:")
# print(df)

# # حذف عمود Cost
# df.drop("Cost", axis=1, inplace=True)

# print("\n📌 بعد الحذف:")
# print(df)
# 

# import pandas as pd

# df = pd.read_csv("sales.csv")

# # حذف الصف رقم 2 (تذكر أن العد يبدأ من الصفر)
# df.drop(2, axis=0, inplace=True)

# df.to_csv("sales.csv", index=False)

# print("✅ تم حذف الصف رقم 2 من الملف")

# import pandas as pd

# df = pd.read_csv("sales.csv")

# # شرط: إبقاء الصفوف اللي فيها Profit أكبر أو يساوي 50
# df = df[df["Profit"] >= 50]

# df.to_csv("sales.csv", index=False)

# print("✅ تم حذف الصفوف اللي Profit فيها أقل من 50")
# import pandas as pd

# # البيانات اللي نريد كتابتها في CSV
# data = {
#     "المنتج": ["هاتف", "لابتوب", "طابعة"],
#     "المبيعات": [200, 800, 300],
#     "التكلفة": [150, 600, 200],
#     "الربح": [50, 200, 100],
#     "التاريخ": ["2025-08-15", "2025-08-16", "2025-08-17"],
#     "ملاحظات": ["NA", "N/A", "تم التسليم"]
# }

# # نخلق DataFrame
# df = pd.DataFrame(data)

# # نكتب ملف CSV
# with open("data.csv", "w", encoding="utf-8") as f:
#     f.write("📊 تقرير المبيعات 2025\n")  # إضافة السطر الأول غير الضروري
#     df.to_csv(f, sep=";", index=False)

# print("✅ تم إنشاء ملف data.csv بنجاح!")

# import pandas as pd

# # نقرأ الملف مع كل الخيارات
# df = pd.read_csv(
#     "data.csv",
#     encoding="utf-8",         # لحل مشكلة اللغة العربية
#     sep=";",                  # لأنه مفصول بفاصلة منقوطة
#     skiprows=1,               # لتجاوز الصف الأول (العنوان)
#     na_values=["NA", "N/A"],  # للتعامل مع القيم الفارغة
#     usecols=["المنتج", "المبيعات", "الربح"]  # نقرأ أعمدة معينة فقط
# )

# print("📌 البيانات بعد المعالجة:")
# print(df)

