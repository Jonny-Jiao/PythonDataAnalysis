import pandas as pd
import numpy as np

if __name__ == '__main__':

    a = 1
    pd.notnull(a)
    # print(pd.notnull(a))

    d = [1,2,3,4,5,5,5]

    D = pd.unique(d)
    # print(D)

    # print(np.random.rand(3,2))

    a = '[{"measure":"248","place":"245","shape":"83","time":""}]'

    print(a.replace("248" ,"1111").replace('245','222'))