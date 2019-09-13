# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:20:08 2019

@author: qcheng1
"""

import pandas as pd
import scipy as sp
import numpy as np
import sklearn as sklearn
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
        self.xtrain_pos = xtrain.loc[ytrain == 1, :]
        self.xtrain_neg = xtrain.loc[ytrain == 0, :]

    def predict_proba(self, xtest):
        pos_neg_dists = [(p,n) for p, n in zip(mahalanobis(xtest, self.xtrain_pos), mahalanobis(xtest, self.xtrain_neg))]
        return np.array([(1-n/(p+n), 1-p/(p+n)) for p,n in pos_neg_dists])

    def predict(self, xtest):
        return np.array([np.argmax(row) for row in self.predict_proba(xtest)])

filepath = 'https://raw.githubusercontent.com/selva86/datasets/master/diamonds.csv'
df = pd.read_csv(filepath).iloc[:, [0,4,6]]
df.head()
df_x = df[['carat', 'depth', 'price']].head(500)
df_x['mahala'] = mahalanobis(x=df_x, data=df[['carat', 'depth', 'price']])
df_x.head()

# Critical values for two degrees of freedom
from scipy.stats import chi2
chi2.ppf((1-0.01), df=2)
#> 9.21
# Compute the P-Values
df_x['p_value'] = 1 - chi2.cdf(df_x['mahala'], 2)

# Extreme values with a significance level of 0.01
df_x.loc[df_x.p_value < 0.01].head(10)

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BreastCancer.csv', 
                 usecols=['Cl.thickness', 'Cell.size', 'Marg.adhesion', 
                          'Epith.c.size', 'Bare.nuclei', 'Bl.cromatin', 'Normal.nucleoli', 
                          'Mitoses', 'Class'])

df.dropna(inplace=True)  # drop missing values.
df.head()

xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(df.drop('Class', axis=1), df['Class'], test_size=.3, random_state=100)

# Split the training data as pos and neg
xtrain_pos = xtrain.loc[ytrain == 1, :]
xtrain_neg = xtrain.loc[ytrain == 0, :]

clf = MahalanobisBinaryClassifier(xtrain, ytrain)        
pred_probs = clf.predict_proba(xtest)
pred_class = clf.predict(xtest)

# Pred and Truth
pred_actuals = pd.DataFrame([(pred, act) for pred, act in zip(pred_class, ytest)], columns=['pred', 'true'])
print(pred_actuals[:5])

truth = pred_actuals.loc[:, 'true']
pred = pred_actuals.loc[:, 'pred']
scores = np.array(pred_probs)[:, 1]
print('AUROC: ', sklearn.metrics.roc_auc_score(truth, scores))
print('\nConfusion Matrix: \n', sklearn.metrics.confusion_matrix(truth, pred))
print('\nAccuracy Score: ', sklearn.metrics.accuracy_score(truth, pred))
print('\nClassification Report: \n', sklearn.metrics.classification_report(truth, pred))