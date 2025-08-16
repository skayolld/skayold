# import numpy as np ###
# # pip install numpy


# arr = np.array([500,3444,3234,2233])

# print (arr + 3434343)
# print (arr * 67)

import numpy as np

# arr_2d = np.array([[1,2,3],
#                    [4,5,6]])

# print(arr_2d)
# print("Shape ", arr_2d.shape)
# print("(ndim):", arr_2d.ndim)
# print(arr_2d[1, 2])  # العنصر في الصف 0 والعمود 1 → 2
# print (arr_2d * 5)

# zeros = np.zeros((3, 4))  # مصفوفة 3×4 مليانة أصفار
# ones = np.ones((2, 2))    # مصفوفة 2×2 مليانة آحاد

# print(zeros)
# print(ones)
# arr_3d = np.array([
#     [[1, 2, 3,4],
#      [4, 5, 6,5]],

#     [[7, 8, 9,5],
#      [10, 11, 12,5]]
# ])
# print (arr_3d)
# print (arr_3d.shape)
# print("Number of dimensions:", arr_3d.ndim)
# print (arr_3d[0,0,2]) 

# arr = np.array([1, 2, 3, 4, 5, 6])

# print("Sum:", np.sum(arr))
# print("Mean:", np.mean(arr))
# print("Max:", np.max(arr))
# print("Min:", np.min(arr))

# reshaped = np.reshape(arr, (2, 3))
# print("Reshaped:\n", reshaped)
# arr = np.array([1, 2, 3, 4, 5, 6])
# print("الأصلية:", arr)

# # نعيد ترتيبها لمصفوفة 2 صف × 3 أعمدة
# reshaped = arr.reshape(2, 3)
# print("بعد إعادة التشكيل:\n", reshaped)

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("المصفوفة الأصلية:\n", arr)
print("المصفوفة بعد flatten():", arr.flatten())
print("المصفوفة بعد transpose (T):\n", arr.T)