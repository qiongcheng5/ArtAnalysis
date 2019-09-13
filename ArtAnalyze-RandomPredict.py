# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:33:13 2019

@author: qcheng1
"""

import pandas as pd
import os # File/directory operations
import xlsxwriter # Writing to an excel file using Python
import xlrd # Reading an excel file using Python
import cv2 # Read, display, write an image, using OpenCV
import tensorflow as tf #
import torch # convert a Python list object into a PyTorch tensor using the tensor operation. 
import inspect # inspection
import numpy as np #NumPy’s main object is the homogeneous multidimensional array. 
from skimage import io, filters #Scikit-image is an image processing toolbox for SciPy https://scikit-image.org/
import pandas as pd
import scipy as sp
import sklearn as sk
#from sklearn.model_selection import train_test_split #Mahalanobis Distance for Classification Problems

def msqrt(X):
    '''Computes the square root matrix of symmetric square matrix X.'''
    (L, V) = np.linalg.eig(X)
    return V.dot(np.diag(np.sqrt(L))).dot(V.T) 

def zca_whitening_matrix(X):
    """
    Function to compute ZCA whitening matrix (aka Mahalanobis whitening).
    INPUT:  X: [M x N] matrix.
        Rows: Variables
        Columns: Observations
    OUTPUT: ZCAMatrix: [M x M] matrix
    """
    # Covariance matrix [column-wise variables]: Sigma = (X-mu)' * (X-mu) / N
    sigma = np.cov(X, rowvar=True) # [M x M]
    # Singular Value Decomposition. X = U * np.diag(S) * V
    U,S,V = np.linalg.svd(sigma)
        # U: [M x M] eigenvectors of sigma.
        # S: [M x 1] eigenvalues of sigma.
        # V: [M x M] transpose of U
    # Whitening constant: prevents division by zero
    epsilon = 1e-5
    # ZCA Whitening matrix: U * Lambda * U'
    ZCAMatrix = np.dot(U, np.dot(np.diag(1.0/np.sqrt(S + epsilon)), U.T)) # [M x M]
    return np.dot(ZCAMatrix, X)

def tensorFFNN(featurefilename, outfile):
    # To open Workbook 
    wb = xlrd.open_workbook(momafilename) 
    sheet = wb.sheet_by_index(0)

# Kaze Feature extractor  
def kaze_extract_features(image_path, vector_size=32):
    image = cv2.imread(image_path, 0)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        if dsc is None:
            ##print(image_path)
            return None
        else:
            dsc = dsc.flatten()
            # Making descriptor of same size
            # Descriptor vector size is 64
            needed_size = (vector_size * 64)
            if dsc.size < needed_size:
                # if we have less the 32 descriptors then just adding zeros at the
                # end of our feature vector
                dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: %s'% e)
        return None

    return dsc

def extractFeatures(images_path, vector_size=32):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    featuresW = []
    cols = 0
    for imagefile in files:
        # To get image feature for an image
        # print(str.format("ImageFile: %r" % str.format(imagefile)))
        
        #image = cv2.imread(imagefile, 0) # Read an image C->
        #features = filters.sobel(image)    # C1-Scikit-image sobel
        #features = cv2.Canny(image, 100, 100)   # Or C2-Canny Edge Detection
        
        features = kaze_extract_features(imagefile)
        
        if features is None:
            ##print(imagefile)
            a = 1
        else:
            edgeFeatures = features.flatten()
            cols = len(edgeFeatures)
            ##print(cols)
            featuresW.append(edgeFeatures)
        
    return featuresW, len(featuresW), cols

def tensorFFNNImages(images_path, vector_size=32):
    batchSz = 100
    
    # extract image features
    featuresW, rowsW, colsW = extractFeatures(images_path) 
     
    # mimic prediction
    y_anss = np.random.random(rowsW)
    anss = np.array([1 if y >0.5 else 0 for y in y_anss])

    print('#1 Declare variables')
    W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW))
    B = tf.Variable(tf.random.normal ([1], stddev = .1))
    
    print('#2 Decalre placeholder')
    img = tf.compat.v1.placeholder(tf.float32, [batchSz, colsW])
    ans = tf.compat.v1.placeholder(tf.float32, [batchSz])
    
    print('#3' )
    prbs = tf.nn.softmax(tf.matmul(img, W) + B)
    xEnt = tf.reduce_mean(-tf.reduce_sum(ans * tf.math.log(prbs), reduction_indices =[1]))
    
    print('#4')
    train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(xEnt)
    numCorrect = tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans))
    accuracy = tf.reduce_mean(tf.cast(numCorrect, tf.float32))

    print('#5')
    sess = tf.compat.v1.Session()
    sess.run(tf.global_variables_initializer())
    
    sumacc = 0
    for i in range(int(rowsW/batchSz)):
        indexL = i * batchSz
        indexH = (i+1) * batchSz  if rowsW >=(i+1) * batchSz else rowsW
        #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
        imgnp = featuresW[indexL:indexH]
        tanss = np.transpose(anss[indexL:indexH])
        sess.run(train, feed_dict={img: imgnp, ans: tanss})
        acc = sess.run(accuracy, feed_dict={img: imgnp, ans: tanss})
        print("Train Accuracy: %d %r" % (i, acc))
        sumacc += acc
    print("Train Accuracy:%r" % (sumacc/int(rowsW/batchSz)))
    #sumAcc = 0
    #sumAcc+= sess.run(accuracy, feed_dict={img: img, ans: ans})
    
def tensorFFNNImagesBaggingPreTrain(images_path, timesMax, preTrainBagMax, vector_size=32):
    batchSz = 100
    
    # extract image features
    featuresW0, rowsW, colsW = extractFeatures(images_path) 
    featuresW = zca_whitening_matrix(featuresW0)
    train_avg_acc = []
    test_avg_acc = []
    for times in range(timesMax):
        #Split the training data and testing data.
        train_indices = np.random.choice(len(featuresW), round(len(featuresW)*0.5), replace=False)
        test_indices = np.array(list(set(range(len(featuresW))) - set(train_indices)))
        x_vals_train = np.array(featuresW)[train_indices]
        x_vals_test = np.array(featuresW)[test_indices]
        
        # mimic prediction
        y_anss = np.random.random(rowsW)
        anss = np.array([1 if y >0.5 else 0 for y in y_anss])
        y_vals_train = anss[train_indices]
        y_vals_test = anss[test_indices]

        #print('#1 Declare variables')
        W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW))
        B = tf.Variable(tf.random.normal ([1], stddev = .1))
        
        #print('#2 Decalre placeholder')
        img = tf.compat.v1.placeholder(tf.float32, [None, colsW])
        ans = tf.compat.v1.placeholder(tf.float32, [None,1])
        
        #print('#3' )
        prbs = tf.nn.softmax(tf.matmul(img, W) + B)
        xEnt = tf.reduce_mean(-tf.reduce_sum(ans * tf.math.log(prbs), reduction_indices =[1]))
        
        #print('#4')
        train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(xEnt)
        numCorrect = tf.equal(tf.math.argmax(prbs, 1), tf.math.argmax(ans))
        accuracy = tf.reduce_mean(tf.cast(numCorrect, tf.float32))
    
        #print('#5')
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())
        
        train_accuracy = []
        test_accuracy = []
        for i in range(preTrainBagMax):
            rand_index = np.random.choice(len(x_vals_train), size=batchSz)
            X = x_vals_train[rand_index]
            Y = np.transpose([y_vals_train[rand_index]])

            #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
            imgnp = X
            tanss = Y
            sess.run(train, feed_dict={img: imgnp, ans: tanss})            
            train_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_train, ans: np.transpose([y_vals_train])})
            train_accuracy.append(train_acc_temp)
            test_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            test_accuracy.append(test_acc_temp)

        #print("Times: %d Train Accuracy:%r" % (times, np.average(train_accuracy)))
        #print("Times: %d Test Accuracy:%r" % (times, np.average(test_accuracy)))
        train_avg_acc.append(np.average(train_accuracy))
        test_avg_acc.append(np.average(test_accuracy))
    print("Average Train Accuracy:%r" % (np.average(train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(test_avg_acc)))
        
def tensorSVMImagesBaggingPreTrain(images_path, timesMax, preTrainBagMax, vector_size=32):
    batchSz = 100
    
    # extract image features
    featuresW0, rowsW, colsW = extractFeatures(images_path) 
    featuresW = zca_whitening_matrix(featuresW0)
    train_avg_acc = []
    test_avg_acc = []
    loss_avg_acc = []
    for times in range(timesMax):
        #Split the training data and testing data.
        train_indices = np.random.choice(len(featuresW), round(len(featuresW)*0.8), replace=False)
        test_indices = np.array(list(set(range(len(featuresW))) - set(train_indices)))
        x_vals_train = featuresW[train_indices]
        x_vals_test = featuresW[test_indices]
        
        # mimic prediction
        y_anss = np.random.random(rowsW)
        anss = np.array([1 if y >0.5 else 0 for y in y_anss])
        y_vals_train = anss[train_indices]
        y_vals_test = anss[test_indices]

        #print('#1 Declare variables')
        W = tf.Variable(tf.random.normal ([colsW, 1], stddev = .1)) #torch.FloatTensor(featuresW)) #A
        B = tf.Variable(tf.random.normal ([1], stddev = .1))                                       #b
        
        #print('#2 Decalre placeholder')
        img = tf.compat.v1.placeholder(tf.float32, [None, colsW]) #x_data
        ans = tf.compat.v1.placeholder(tf.float32, [None, 1]) #y_target
        
        #Declare the model output.
        model_output = tf.subtract(tf.matmul(img, W), B) #x_data, A), b)
        #Declare the necessary components for the maximum margin loss.
        l2_norm = tf.reduce_sum(tf.square(W))
        alpha = tf.constant([0.1])
        classification_term = tf.reduce_mean(tf.maximum(0., tf.subtract(1.,tf.multiply(model_output, ans))))
        loss = tf.add(classification_term, tf.multiply(alpha, l2_norm))
        
        #Declare the prediction and accuracy functions.
        prediction = tf.sign(model_output)
        accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, ans),tf.float32))
        
        ## Create the epsilon and set 0.5.
        #epsilon = tf.constant([0.5])
        #loss = tf.reduce_mean(tf.maximum(0., tf.subtract(tf.abs(tf.subtract(model_output, y_target)), epsilon)))
        ##Declare the optimizer.
        #my_opt = tf.compat.v1.train.GradientDescentOptimizer(0.075)
        #train_step = my_opt.minimize(loss)
        #init = tf.initialize_all_variables()
        #sess.run(init)
        
        #Declare the optimizer.
        my_opt = tf.compat.v1.train.GradientDescentOptimizer(0.01)
        train = my_opt.minimize(loss)
        init = tf.compat.v1.global_variables_initializer()
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())

        sumacc = 0
        loss_vec = []
        train_accuracy = []
        test_accuracy = []
        for i in range(preTrainBagMax):
            rand_index = np.random.choice(len(x_vals_train), size=batchSz)
            X = x_vals_train[rand_index]
            Y = np.transpose([y_vals_train[rand_index]])

            #imgnp = np.vstack([np.expand_dims(x, 0) for x in featuresW[indexL:indexH]])
            imgnp = X
            tanss = Y
            sess.run(train, feed_dict={img: imgnp, ans: tanss})
            #acc = sess.run(accuracy, feed_dict={img: imgnp, ans: tanss})
            temp_loss = sess.run(loss, feed_dict={img: imgnp, ans: tanss})
            loss_vec.append(temp_loss)
            train_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_train, ans: np.transpose([y_vals_train])})
            train_accuracy.append(train_acc_temp)
            test_acc_temp = sess.run(accuracy, feed_dict={img: x_vals_test, ans: np.transpose([y_vals_test])})
            test_accuracy.append(test_acc_temp)

        #print("Times: %d Train Accuracy:%r" % (times, np.average(train_accuracy)))
        #print("Times: %d Train Accuracy:%r" % (times, np.average(test_accuracy)))
        #print("Times: %d Loss :%r" % (times, np.average(loss_vec)))
        train_avg_acc.append(np.average(train_accuracy))
        test_avg_acc.append(np.average(test_accuracy))
        loss_avg_acc.append(np.average(loss_vec))
    print("Average Train Accuracy:%r" % (np.average(train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(test_avg_acc)))
    print("Average Loss:%r" % (np.average(loss_avg_acc)))
        
def tensorFFNNSample():    
    batchSz = 100
    
    print('#1')
    colsW = 784
    rowsW = 200
    # Create two variables.
    W = tf.Variable(tf.random_normal([colsW, rowsW], stddev=0.35),
                          name="weights")
    B = tf.Variable(tf.random_normal([rowsW], stddev=0.35), name="biases")

    
    print('#2')
    img = tf.placeholder(tf.float32, [batchSz, colsW])
    ans = tf.placeholder(tf.float32, [batchSz, rowsW])
    
    print('#3')
    prbs = tf.nn.softmax(tf.matmul(img, W) + B)
    xEnt = tf.reduce_mean(-tf.reduce_sum(ans * tf.log(prbs), reduction_indices =[1]))
    
    print('#4')
    train = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(xEnt)
    numCorrect = tf.equal(tf.arg_max(prbs, 1), tf.arg_max(ans, 1))
    accuracy = tf.reduce_mean(tf.cast(numCorrect, tf.float32))

    print('#5')
    sess = tf.compat.v1.Session()
    sess.run(tf.compat.v1.global_variables_initializer())
    # Before starting, initialize the variables.  We will 'run' this first.
    #init = tf.initialize_all_variables()
    # Launch the graph.
    #sess = tf.compat.v1.Session()
    
    #sess.run(init)
    ignore, acc = sess.run([train, accuracy], feed_dict={img: img, ans: ans})
    print("Train Accuracy: %r" % (acc))
    #sumAcc = 0
    #sumAcc+= sess.run(accuracy, feed_dict={img: img, ans: ans})

"""
D^2 = (x-m)^T * C^-1 * (x-m)
where, 
 - D^2        is the square of the Mahalanobis distance. 
 - x          is the vector of the observation (row in a dataset), 
 - m          is the vector of mean values of independent variables (mean of each column), 
 - C^(-1)     is the inverse covariance matrix of independent variables. 
 """
def mahalanobis(x=None, data=None, cov=None):
    """Compute the Mahalanobis Distance between each row of x and the data  
    x    : vector or matrix of data with, say, p columns.
    data : ndarray of the distribution from which Mahalanobis distance of each observation of x is to be computed.
    cov  : covariance matrix (p x p) of the distribution. If None, will be computed from data.
    """
    x_minus_mu = x - np.mean(data)
    if not cov:
        cov = np.cov(np.transpose(data))
    inv_covmat = sp.linalg.inv(cov)
    left_term = np.dot(x_minus_mu, inv_covmat)
    mahal = np.dot(left_term, x_minus_mu.T)
    return mahal.diagonal()

"""
Mahalanobis distance can be used for classification problems.
Mahalanobis classifier
inputs:
    xtrain, ytrain, xtest, ytest=None
"""
class MahalanobisBinaryClassifier():
    def __init__(self, xtrain, ytrain):
        self.xtrain_pos = xtrain[ytrain == 1, :]
        self.xtrain_neg = xtrain[ytrain == 0, :]

    def predict_proba(self, xtest):
        pos_neg_dists = [(p,n) for p, n in zip(mahalanobis(xtest, self.xtrain_pos), mahalanobis(xtest, self.xtrain_neg))]
        return np.array([(1-n/(p+n), 1-p/(p+n)) for p,n in pos_neg_dists])

    def predict(self, xtest):
        return np.array([np.argmax(row) for row in self.predict_proba(xtest)])

def MahalanobisBinaryClassifierTraining(images_path, timesMax):
    batchSz = 100
    
    # extract image features
    featuresW0, rowsW, colsW = extractFeatures(images_path) 
    featuresW = zca_whitening_matrix(featuresW0)
    train_avg_acc = []
    test_avg_acc = []
    train_AUROC_avg=[]
    test_AUROC_avg=[]
    for times in range(timesMax):
        #Split the training data and testing data.
        train_indices = np.random.choice(len(featuresW), round(len(featuresW)*0.8), replace=False)
        test_indices = np.array(list(set(range(len(featuresW))) - set(train_indices)))
        xtrain = featuresW[train_indices]
        xtest = featuresW[test_indices]
        
        # mimic prediction
        y_anss = np.random.random(rowsW)
        anss = np.array([1 if y >0.5 else 0 for y in y_anss])
        ytrain = anss[train_indices]
        ytest = anss[test_indices]

        xtrain_pos = xtrain[ytrain == 1, :]
        xtrain_neg = xtrain[ytrain == 0, :]
        
        clf = MahalanobisBinaryClassifier(xtrain, ytrain)   
       
        test_pred_probs = clf.predict_proba(xtest)
        test_pred_class = clf.predict(xtest)
        
        # Pred and Truth
        test_pred_actuals = pd.DataFrame([(pred, act) for pred, act in zip(test_pred_class, ytest)], columns=['pred', 'true'])
        #print(test_pred_actuals[:5])
        
        test_truth = test_pred_actuals['true']
        test_pred = test_pred_actuals['pred']
        test_scores = np.array(test_pred_probs)[:, 1]
        #print('AUROC: ', sklearn.metrics.roc_auc_score(test_truth, test_scores))
        #print('\nConfusion Matrix: \n', sklearn.metrics.confusion_matrix(test_truth, test_pred))
        #print('\nAccuracy Score: ', sklearn.metrics.accuracy_score(test_truth, test_pred))
        #print('\nClassification Report: \n', sklearn.metrics.classification_report(test_truth, test_pred))
        test_AUROC_avg.append(sk.metrics.roc_auc_score(test_truth, test_scores))
        test_avg_acc.append(sk.metrics.accuracy_score(test_truth, test_pred))
        
        train_pred_probs = clf.predict_proba(xtrain)
        train_pred_class = clf.predict(xtrain)        
        
        # Pred and Truth
        train_pred_actuals = pd.DataFrame([(pred, act) for pred, act in zip(train_pred_class, ytrain)], columns=['pred', 'true'])
        #print(test_pred_actuals[:5])
        
        train_truth = train_pred_actuals['true']
        train_pred = train_pred_actuals['pred']
        train_scores = np.array(train_pred_probs)[:, 1]
        train_AUROC_avg.append(sk.metrics.roc_auc_score(train_truth, train_scores))
        train_avg_acc.append(sk.metrics.accuracy_score(train_truth, train_pred))
        
    print("Average Train Accuracy:%r" % (np.average(train_avg_acc)))
    print("Average Test Accuracy:%r" % (np.average(test_avg_acc)))
    print("Average Train AUROC:%r" % (np.average(train_AUROC_avg)))
    print("Average Test AUROC:%r" % (np.average(test_AUROC_avg)))
    
def run():
    #print(os.path.dirname(inspect.getfile(tensorflow)))
    images_path = './images/'    
 
    featurefilename = './MoMAPaintingQArtLearnMetrics_Todd_0628.xlsx'
    outfile = './MoMADecentArtistsAnalysis.txt'
    imagefile = 'W1siZiIsIjE0MDQ5NyJdLFsicCIsImNvbnZlcnQiLCItcmVzaXplIDMwMHgzMDBcdTAwM2UiXV0.png'
    # Debugging...
    #W1siZiIsIjc1MTUyIl0sWyJwIiwiY29udmVydCIsIi1yZXNpemUgMzAweDMwMFx1MDAzZSJdXQ.png'
    #image = cv2.imread(str.format('./images/%s' % imagefile), 0)
    #edges = cv2.Canny(image, 100, 100)
    #print(str.format("Edge features: %r" % len(edges.flatten())))
    #tensorFFNNSample()
    
    #tensorFFNNImages(images_path) # 0.42 only training data
    print('tensorFFNNImagesBaggingPreTrain')
    #tensorFFNNImagesBaggingPreTrain(images_path, 100, 500)
    
    print('tensorSVMImagesBaggingPreTrain')
    #tensorSVMImagesBaggingPreTrain(images_path, 100, 500)
    
    print('MahalanobisBinaryClassifierTraining')
    #MahalanobisBinaryClassifierTraining(images_path, 100)
    
    allfeatures = './MoMAPaintingQArtLearnDecentArtistsMetricsVector_0705.txt' #statistical features from Todd + Kaze features
    print('Finished')
    
run()