# http://www.jianshu.com/p/05314e94cee9
import matplotlib.pyplot as plt
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# plt.imshow(x_train[0], cmap=plt.get_cmap("PuBuGn_r"))
# plt.show()

x_train = x_train.reshape()