# -*- coding: utf-8 -*-
from numpy import *
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
trainX = iris.data
trainY = iris.target


clf = LogisticRegression(penalty='l2', dual=False, tol=1e-4, C=1.0,
                 fit_intercept=True, intercept_scaling=1, class_weight=None,
                 random_state=None, solver='liblinear', max_iter=100,
                 multi_class='ovr', verbose=0, warm_start=False, n_jobs=1)
'''
    @param penalty: 指定正则化策略
    @param dual:  是否求解对偶形式
    @param C:  惩罚项系数的倒数，越大，正则化项越小
    @param fit_intercept:  是否拟合截距
    @param intercept_scaling:  当solver='liblinear'、fit_intercept=True时，会制造出一个恒为1的特征，权重为b，为了降低这个人造特征对正则化的影响，可以将其设为1
    @param class_weight:  可以是一个字典或'balanced'。字典：可以指定每一个分类的权重；'balanced'：可以指定每个分类的权重与该分类在训练集中的频率成反比
    @param max_iter:  最大迭代次数
    @param random_state:  一个整数或一个RandomState对象或None
    @param solver:  指定求解最优化问题的算法：
    'newton-cg':牛顿法；
    'lbfgs':拟牛顿法；
    'liblinear':使用liblinear;(适用于小数据集)
    'sag':使用Stochastic Average Gradient Descent算法(适用于大数据集)
    @param tol:  指定迭代收敛与否的阈值
    @param multi_class: 
    'ovr': 采用one-vs-rest策略
    'multi_class': 采用多类分类Logistic回归
    @param verbose: 是否开启迭代过程中输出日志
    @param warm_start:  是否使用前一次的训练结果继续训练
    @param n_jobs: 任务并行时指定使用的CPU数，-1表示使用所有可用的CPU
    
    @attribute coef_: 权重向量
    @attribute intercept_: 截距b
    @attribute n_iter_: 实际迭代次数
    
    @method fit(X,y[,sample_weight]): 训练模型
    @method predict(X): 预测
    @method predict_log_proba(X): 返回X预测为各类别的概率的对数
    @method predict_proba(X): 返回X预测为各类别的概率
    @method score(X,y[,sample_weight]): 计算在(X,y)上的预测的准确率
'''

clf.fit(trainX, trainY)

print ("权值："+str(clf.coef_))
print ("截距："+str(clf.intercept_))
print ("分数："+str(clf.score(trainX, trainY)))
print (clf.predict(trainX))
print (trainY)
'''
C:\Anaconda2\lib\site-packages\sklearn\datasets
权值：[[ 0.41498833  1.46129739 -2.26214118 -1.0290951 ]
 [ 0.41663969 -1.60083319  0.57765763 -1.38553843]
 [-1.70752515 -1.53426834  2.47097168  2.55538211]]
截距：[ 0.26560617  1.08542374 -1.21471458]
分数：0.96
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1 1 1 2 1 1 1
1 1 1 1 1 1 1 1 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
2]
'''
