# Import Packages
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()

# menampilkan data
print(digits.data)

# menetapkan target
digits.target

# bentuk data array
digits.images[0]

# memprediksi
# import svm
from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)

# memilih parameter
clf.fit(digits.data[:-1], digits.target[:-1])

# memprediksi nilai baru
clf.predict(digits.data[-1:])

# menggambarkan dataset dengan plt
from sklearn import datasets
import matplotlib.pyplot as plt
digits = datasets.load_digits()
# Display
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()


# Konvensi

#casting
import numpy as np
from sklearn import kernel_approximation

rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
X.dtype

transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
X_new.dtype

# Target regresi diberikan float64dan target klasifikasi dipertahankan:
from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)

list(clf.predict(iris.data[:3]))

clf.fit(iris.data, iris.target_names[iris.target])

list(clf.predict(iris.data[:3]))


# Parameter
# Memasang & memperbarui
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)
clf = SVC()
clf.set_params(kernel='linear').fit(X, y)
clf.predict(X[:5])
clf.set_params(kernel='rbf').fit(X, y)
clf.predict(X[:5])

# Multikelas
# Multilabel
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]
classif = OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X, y).predict(X)

# multikelas predict()
y = LabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)

# pengklasifikasi fit()
# representasi label biner 2d
from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)
