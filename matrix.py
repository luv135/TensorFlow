import numpy as np

# 2-D array: 2 x 3
two_dim_matrix_one = np.array([[1, 2, 3], [4, 5, 6]])
# 2-D array: 3 x 2
two_dim_matrix_two = np.array([[1, 2], [3, 4], [5, 6]])
two_multi_res = np.dot(two_dim_matrix_one, two_dim_matrix_two)
print('two_multi_res: %s' % (two_multi_res))


x_data = np.float32(np.random.rand(2, 5))  # 随机输入
print(x_data)
y_data = np.dot([0.100, 0.200], x_data) + 0.300
print(y_data)