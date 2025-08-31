# import pandas as pd 
# import matplotlib.pyplot as plt 

# df = pd.read_csv("sales.csv")
# plt.bar(df["Product"], df["Sales"])
# plt.title("Sales per Product ")
# plt.xlabel("Product")
# plt.ylabel("Sales")

# plt.show()

# import pandas as pd 
# import matplotlib.pyplot as plt

# df = pd.read_csv("sales.csv")

# df["Profit"] = df["Sales"] - df["Cost"]

# x = range(len(df["Product"]))

# colors = ["red","blue","green","orange","purple"]

# bars_sales =  plt.bar([i - 0.2 for i in x], df["Sales"],width=0.4,label="Sales",color=colors)
# bars_profit = plt.bar([i + 0.2 for i in x], df["Profit"],width=0.4,label="Profit",color=colors)
# for bar in bars_sales:
#     yval = bar.get_height()   # ارتفاع العمود (قيمة Sales)
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 10, int(yval), ha="center", va="bottom", fontsize=8, color="blue")
# for bar in bars_profit:
#     yval = bar.get_height()   # ارتفاع العمود (قيمة Profit)
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 10, int(yval), ha="center", va="bottom", fontsize=8, color="red")


# plt.xticks(x, df["Product"],rotation=90)   # أسماء المنتجات على المحور X
# plt.xlabel("Products")
# plt.ylabel("Value")
# plt.title("Sales vs Profit per Product")
# plt.legend()

# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# # نقرأ البيانات
# df = pd.read_csv("sales.csv")

# # نفترض في ملف CSV عندنا عمود Date
# # لازم يكون العمود بصيغة تاريخ
# df["Date"] = pd.to_datetime(df["Date"])

# # نرسم خط للمبيعات حسب التاريخ
# plt.plot(df["Date"], df["Sales"], marker="o", label="Sales", color="blue")

# # إضافة بعض التفاصيل
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.title("Sales Over Time")
# plt.legend()
# plt.xticks(rotation=45)   # نلف التواريخ عشان أوضح
# plt.grid(True)            # نضيف شبكة خفيفة

# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("sales.csv")

# # تحويل العمود Date إلى نوع تاريخ
# df["Date"] = pd.to_datetime(df["Date"])

# plt.plot(df["Date"], df["Sales"], label="Sales")
# plt.xlabel("Date")
# plt.ylabel("Sales")
# plt.title("Sales Trend Over Time")
# plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# نقرأ البيانات
df = pd.read_csv("sales.csv")

# نضيف عمود تواريخ وهمي بنفس طول البيانات
df["Date"] = pd.date_range(start="2025-01-01", periods=len(df), freq="D")

# نرسم خط بسيط للمبيعات
plt.plot(df["Date"], df["Sales"], label="Sales", marker="o")

plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)   # تدوير التواريخ عشان تقرأها أوضح
plt.legend()
plt.show()
