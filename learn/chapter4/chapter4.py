import pandas as pd
from scipy.interpolate import lagrange
from sklearn.decomposition import PCA

def chapter4_1():
    data = pd.read_excel('catering_sale.xls')
    # print( )
    data['销量'][(data['销量']<400)|(data['销量']>5000)] = None


    def ployinterp_column(s,n,k=5):
        y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))]
        y = y[y.notnull()]
        return lagrange(y.index,list(y))

    for i in data.columns:
        for j in range(len(data)):
            if (data[i].isnull())[j]:
                data[i][j] = ployinterp_column(data[i],j)

    print(data)


def chapter4_2():
    inputfile = 'principal_component.xls'
    outputfile = 'dimention_reducted.xls'

    data = pd.read_excel(inputfile,header= None)
    pca = PCA()
    pca.fit(data)
    print(pca.components_)
    print(pca.explained_variance_ratio_)

if __name__ == '__main__':
    # chapter4_1()
    chapter4_2()