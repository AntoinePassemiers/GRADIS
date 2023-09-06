import os
import pickle

import numpy as np


ROOT = os.path.dirname(os.path.abspath(__file__))


for i in range(5):
	with open(f'size100_{i + 1}_data.pkl', 'rb') as f:
		data = pickle.load(f)

	arr = data[2].T

	net_folder = os.path.join(ROOT, f'net{i + 1}')
	if not os.path.isdir(net_folder):
		os.makedirs(net_folder)

	np.savetxt(os.path.join(net_folder, 'Expression.txt'), arr, delimiter='\t', fmt='%.8f')

	np.random.shuffle(arr)

	np.savetxt(os.path.join(net_folder, 'Expression-shuffled.txt'), arr, delimiter='\t', fmt='%.8f')

	arr = np.random.rand(*arr.shape)

	np.savetxt(os.path.join(net_folder, 'Expression-random.txt'), arr, delimiter='\t', fmt='%.8f')


with open('tmp.txt', 'w') as f:
	for i in range(100):
		f.write(f'G{i + 1}\n')
