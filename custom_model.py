import numpy as np
import tensorflow as tf

# https://www.tensorflow.org/get_started/mnist/beginners
def model_fn(features, labels, mode):
    W = tf.get_variable("W", [1], dtype=tf.float64)
    b = tf.get_variable("b", [1], dtype=tf.float64)
    y = W * features['x'] + b

    loss = tf.reduce_sum(tf.square(y - labels))

    global_step = tf.train.get_global_step()
    optimizer = tf.train.GradientDescentOptimizer(0.01)

    train = tf.group(optimizer.minimize(loss),
                     tf.assign_add(global_step, 1))

    return tf.estimator.EstimatorSpec(
        mode=mode,
        predictions == y,
        loss=loss,
        train_op=train)

estimator = tf.estimator.Estimator(model_fn=model_fn)


# define our data sets
x_train = np.array([1., 2., 3., 4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7., 0.])