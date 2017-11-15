import tensorflow as tf

# matrix = [[3.,3.]]

# print(matrix[0])

matrix1 = tf.constant([[3., 3.]])

matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)

sess = tf.Session()

result = sess.run(product)

print(result)

sess.close()

################################


sess = tf.InteractiveSession()

x = tf.Variable([1.0, 2.0])
a = tf.constant([3.0, 3.])

x.initializer.run()

sub = tf.subtract(x, a)

print(sub.eval())

## 变量

state = tf.Variable(0)

one = tf.constant(1)

new_value = tf.add(state, one)

update = tf.assign(state, new_value)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(state))
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

# print(bin(ord('S')))
# print(bin(ord('B')))

# Fetch

input1 = tf.constant(3.)
input2 = tf.constant(2.)
input3 = tf.constant(5.)
intermed = tf.add(input1, input2)
mul = tf.multiply(input1, intermed)

with tf.Session() as sess:
    result = sess.run([mul, intermed])
    print(result)

# Feed

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run([output], feed_dict={input1: [7.], input2: [2.]}))
