# https://www.tensorflow.org/get_started/mnist/beginners

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# None 表示不定多少张图, 784 为一张图的(像素)大小
x = tf.placeholder(tf.float32, [None, 784])

# 784 为一张图片的每个像素个数对于某个数字的权重,
# 如[784][0] 表示数字0对于每个像素的权重
# 如[784][1] 表示数字1对于每个像素的权重
W = tf.Variable(tf.zeros([784, 10]))
# 每个数字的偏移值
b = tf.Variable(tf.zeros([10]))

# y = w*x+b
y = tf.nn.softmax(tf.matmul(x, W) + b)

# 对应于变量x 的具体数,如1,2,3等
y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()

tf.global_variables_initializer().run()

for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


################################
