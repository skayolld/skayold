# from sklearn.tree import DecisionTreeClassifier

# # بيانات التدريب (features): العمر، الوزن، الطول
# X = [
#     [25, 70, 175],
#     [30, 80, 180],
#     [22, 65, 170],
#     [35, 90, 185],
#     [28, 75, 178]
# ]

# # النتائج المتوقعة (labels): 1 تعني رياضي، 0 تعني غير رياضي
# y = [1, 1, 0, 1, 0]

# # إنشاء نموذج شجرة القرار
# model = DecisionTreeClassifier()

# # تدريب النموذج على البيانات
# model.fit(X, y)

# # اختبار النموذج على بيانات جديدة
# test_data = [[27, 72, 176]]
# prediction = model.predict(test_data)

# # print("Prediction:", prediction)  # يطبع 1 أو 0



# from sklearn.datasets import load_iris 
# # هذه الدالة تجيب لنا مجموعة بيانات جاهزة عن أزهار اسمها "Iris" (فيها مقاسات واسم نوع الزهرة).
# # بدون ما نروح نجمع بيانات من العالم الحقيقي، هي موجودة جاهزة.


# from sklearn.model_selection import train_test_split 
# #هنا نستورد أداة اسمها train_test_split، وظيفتها تقسيم البيانات إلى قسمين:

# # تدريب (Training): يتعلم منه الكمبيوتر.

# # اختبار (Testing): نستخدمه لاحقاً لقياس دقة النموذج.


# from sklearn.neighbors import KNeighborsClassifier  
# # هذا يستورد نموذج اسمه KNN (K-Nearest Neighbors).
# # فكرته: إذا جبت بيانات جديدة، يروح يشوف أقرب بيانات لها في التدريب، ويقرر نوعها.


# from sklearn.metrics import accuracy_score 
# #📌 هذه أداة لحساب الدقة (Accuracy) = كم بالمية النموذج جاوب صح.


# iris = load_iris()
# X = iris.data  
# y = iris.target 

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = KNeighborsClassifier(n_neighbors=3)

# model.fit(X_train, y_train)


# predictions = model.predict(X_test)


# accuracy = accuracy_score(y_test, predictions)
# print(f"Model Accuracy: {accuracy * 100:.2f}%")


# new_data = [[5.1, 3.5, 1.4, 0.2]]
# new_prediction = model.predict(new_data)
# print("Predicted class for new data:", new_prediction)

# 1- استيراد المكتبات
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score

# # 2- تحميل البيانات
# data = load_iris()
# X = data.data      # الميزات
# y = data.target    # التصنيفات

# # 3- تقسيم البيانات (80% تدريب، 20% اختبار)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # 4- إنشاء نموذج وتدريبه
# model = LogisticRegression(max_iter=200)
# model.fit(X_train, y_train)

# # 5- التنبؤ على بيانات الاختبار
# y_pred = model.predict(X_test)

# # 6- حساب الدقة
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# from sklearn.datasets import load_iris
# iris = load_iris()
# print(iris.data[:5])
# print(iris.target[:5])

# from sklearn.model_selection import train_test_split
# X = iris.data
# y = iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# print( len(X_train))
# print( len(X_test))

# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)

# from sklearn.metrics import accuracy_score
# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)
# print( accuracy * 100, "%")

# new_data = [[5.1, 3.5, 1.4, 0.2]]
# new_prediction = model.predict(new_data)
# print("الزهرة الجديدة تنتمي للفئة:", new_prediction)
# print("الاسم:", iris.target_names[new_prediction][0])

