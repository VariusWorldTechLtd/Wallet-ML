import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#def random_table_generator():

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))

#df1['randNumCol'] = np.random.randint(0,5, size=len(df1))

s = np.random.poisson(10,10000)

count, bins, ignored = plt.hist(s, 14, density=True)
plt.show()

#print(df)