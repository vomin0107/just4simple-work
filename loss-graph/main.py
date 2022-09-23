import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.interpolate import interp1d

# set file path
cwd = os.getcwd()
file_path = os.path.join(cwd, 'p3-2x-EfficientDetLite2-batchsize20-1459steps.txt')

# read 'color_range.txt' file and parsing it by id and value
df = pd.DataFrame() # blank DataFrame to store results

# open file
f = open(file_path)
val_loss_list = []

for line in f.readlines():
    # print(line)
    val_split = line.split('val_loss: ')
    if len(val_split)>1:
        loss = val_split[1][:6]
        # print(loss)
        val_loss_list.append(loss)

# print(val_loss_list)

df = pd.DataFrame({'val_loss': val_loss_list})
df = df.astype(float)

val_numpy_list = df.to_numpy().flatten()[:300]
index_list = np.arange(1, len(val_numpy_list)+1)[:300]
print(index_list)
print(val_numpy_list)

plt.figure(figsize=(40, 5))
poly = np.polyfit(index_list, val_numpy_list, 50)
poly_y = np.poly1d(poly)(index_list)
print(poly_y)
plt.plot(index_list,poly_y)
plt.plot(index_list,val_numpy_list)
plt.show()
