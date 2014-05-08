"""
===================
Plot different SVM 
===================

Comparison of different linear SVM classifiers on the iris dataset. It
will plot the decision surface for four different SVM classifiers.

"""

print(__doc__)

import numpy as np
import pylab as pl
from sklearn import svm, datasets, linear_model, datasets


INPUT_FILE = ['all_neat_n500']#, 'all_neat_n1000', 'all_neat_n1500', 'all_neat_n2000', 'all_neat_n5000', 'all_neat']



for net_type in INPUT_FILE:
  # import data
  #DATA_TRAIN = './data/' + net_type + '_test.data' 
  #data = np.loadtxt(DATA_TRAIN, delimiter = ',')

  #X = data[:,:4] 
  #Y = data[:,-1]

  iris = datasets.load_iris()
  X = iris.data[:, :2]  # we only take the first two features.
  Y = iris.target

  h = .02  # step size in the mesh

  # we create an instance of SVM and fit out data. We do not scale our
  # data since we want to plot the support vectors
  C = 1.0  # SVM regularization parameter
  svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
  rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, Y)
  poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, Y)
  lin_svc = svm.LinearSVC(C=C).fit(X, Y)

  # create a mesh to plot in
  x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
  y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
  xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                       np.arange(y_min, y_max, h))

  # title for the plots
  titles = ['SVC with linear kernel',
            'SVC with RBF kernel',
            'SVC with polynomial (degree 3) kernel',
            'LinearSVC (linear kernel)']


  for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
      # Plot the decision boundary. For that, we will assign a color to each
      # point in the mesh [x_min, m_max]x[y_min, y_max].
      pl.subplot(2, 2, i + 1)
      Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

      # Put the result into a color plot
      Z = Z.reshape(xx.shape)
      pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
      pl.axis('off')

      # Plot also the training points
      pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
      pl.title(titles[i])

  pl.show()
  #plt.savefig('svm_together' + net_type + '.png')
