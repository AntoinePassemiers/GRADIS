import numpy as np
import pandas as pd


PERMUTATION = 'all'
assert PERMUTATION in {'row', 'col', 'all'}


ws = pd.read_excel('Network-original.xlsx', header=None, names=['tf', 'tg', 'regulation'])

print(ws)

labels = np.array(ws['regulation'])
tfs = list(np.asarray(ws['tf'], dtype=str))
tgs = list(np.asarray(ws['tg'], dtype=str))

tf_names = list(set(tfs))
tg_names = list(set(tgs))
tf_dict = {gene_name: i for i, gene_name in enumerate(tf_names)}
tg_dict = {gene_name: i for i, gene_name in enumerate(tg_names)}

arr = np.full((len(tf_names), len(tg_names)), -1, dtype=np.int8)
for k in range(len(tfs)):
    i = tf_dict[tfs[k]]
    j = tg_dict[tgs[k]]
    arr[i, j] = int(labels[k])

if PERMUTATION == 'col':
    for i in range(len(arr)):
        mask = (arr[i, :] >= 0)
        row = arr[i, mask]
        np.random.shuffle(row)
        arr[i, mask] = row
elif PERMUTATION == 'row':
    for j in range(len(arr)):
        mask = (arr[:, j] >= 0)
        col = arr[mask, j]
        np.random.shuffle(col)
        arr[mask, j] = col
else:
    mask = (arr >= 0)
    elements = arr[mask]
    assert len(elements.shape) == 1
    np.random.shuffle(elements)
    arr[mask] = elements

for k, (tf_name, tg_name) in enumerate(zip(tfs, tgs)):
    i = tf_dict[tf_name]
    j = tg_dict[tg_name]
    labels[k] = int(arr[i, j])

with open('tmp.txt', 'w') as f:
    for k in labels:
        f.write(f'{k}\n')

ws['regulation'] = np.asarray(labels, dtype=int)

ws.to_excel('Network.xlsx', header=False, index=False)
