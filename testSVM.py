# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:09:53 2019

@author: Qiong
"""
import tensorflow as tf
from sklearn import datasets 
 
sess = tf.Session()
iris = datasets.load_iris()
x_vals = np.array([[x[0], x[3]] for x in iris.data])
y_vals = np.array([1 if y==0 else -1 for y in iris.target])

#Split the training data and testing data.
train_indices = np.random.choice(len(x_vals), round(len(x_vals)*0.8), replace=False)
test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))
x_vals_train = x_vals[train_indices]
x_vals_test = x_vals[test_indices]
y_vals_train = y_vals[train_indices]
y_vals_test = y_vals[test_indices]

#Create the placeholder and Variable .
batch_size = 100
x_data = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
A = tf.Variable(tf.random_normal(shape=[2,1]))
b = tf.Variable(tf.random_normal(shape=[1,1]))

#Declare the model output.
model_output = tf.subtract(tf.matmul(x_data, A), b)
#Declare the necessary components for the maximum margin loss.
l2_norm = tf.reduce_sum(tf.square(A))
alpha = tf.constant([0.1])
classification_term = tf.reduce_mean(tf.maximum(0., tf.subtract(1.,tf.multiply(model_output, y_target))))
loss = tf.add(classification_term, tf.multiply(alpha, l2_norm))

#Declare the prediction and accuracy functions.
prediction = tf.sign(model_output)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, y_target),tf.float32))

## Create the epsilon and set 0.5.
#epsilon = tf.constant([0.5])
#loss = tf.reduce_mean(tf.maximum(0., tf.subtract(tf.abs(tf.subtract(model_output, y_target)), epsilon)))
##Declare the optimizer.
#my_opt = tf.train.GradientDescentOptimizer(0.075)
#train_step = my_opt.minimize(loss)
#init = tf.initialize_all_variables()
#sess.run(init)

#Declare the optimizer.
my_opt = tf.train.GradientDescentOptimizer(0.01)
train_step = my_opt.minimize(loss)
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

#Train.
loss_vec = []
train_accuracy = []
test_accuracy = []
for i in range(500):
    rand_index = np.random.choice(len(x_vals_train), size=batch_size)
    X = x_vals_train[rand_index]
    Y = np.transpose([y_vals_train[rand_index]])
    sess.run(train_step, feed_dict={x_data: X, y_target: Y})
    temp_loss = sess.run(loss, feed_dict={x_data: X, y_target: Y})
    loss_vec.append(temp_loss)
    train_acc_temp = sess.run(accuracy, feed_dict={x_data: x_vals_train, y_target: np.transpose([y_vals_train])})
    train_accuracy.append(train_acc_temp)
    test_acc_temp = sess.run(accuracy, feed_dict={x_data: x_vals_test, y_target: np.transpose([y_vals_test])})
    test_accuracy.append(test_acc_temp)