import os
import pickle

import numpy as np


ROOT = os.path.dirname(os.path.abspath(__file__))


for i in [1, 4]:
	arr = np.loadtxt(f'net{i}_expression_data.tsv', delimiter='\t')
		
	arr = arr.T

	with open(f'tmp{i}.txt', 'w') as f:
		for k in range(arr.shape[0]):
			f.write(f'G{k + 1}\n')

	net_folder = os.path.join(ROOT, f'net{i}')
	if not os.path.isdir(net_folder):
		os.makedirs(net_folder)

	np.savetxt(os.path.join(net_folder, 'Expression.txt'), arr, delimiter='\t', fmt='%.8f')

	np.random.shuffle(arr)

	np.savetxt(os.path.join(net_folder, 'Expression-shuffled.txt'), arr, delimiter='\t', fmt='%.8f')

	arr = np.random.rand(*arr.shape)

	np.savetxt(os.path.join(net_folder, 'Expression-random.txt'), arr, delimiter='\t', fmt='%.8f')


