import pandas as pd

data = pd.read_csv("sales.csv")
# print(data)
city_sales = data.groupby("City")["Sales"].sum()

# print(city_sales)
# # نجمع البيانات حسب عمود "Product" ونحسب متوسط "Sales" لكل منتج
# product_avg = data.groupby("Product")["Sales"].mean()

# print(product_avg)

# top_cities = city_sales.sort_values(ascending=False).head(2)
# print (top_cities)
city_name = input("Enter a city name : ")

city_date = data[data["City"] == city_name]
print (city_date)