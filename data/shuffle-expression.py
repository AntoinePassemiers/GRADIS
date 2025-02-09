import numpy as np


X = np.genfromtxt('Expression-original.txt', delimiter='\t')

np.random.shuffle(X)

np.savetxt('Expression.txt', X, delimiter='\t', fmt='%.8f')
