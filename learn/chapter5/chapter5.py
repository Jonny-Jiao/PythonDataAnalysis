import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from learn.chapter5.cm_plot import cm_plot


def chapter5_1():
    data = pd.read_excel('sales_data.xls',index_col='序号')
    data[data == '好'] = 1
    data[data == '高'] = 1
    data[data == '是'] = 1
    data[data != 1] = 0
    # print(data)
    x = data.iloc[:,:3].as_matrix().astype(int)
    y = data.iloc[:, 3].as_matrix().astype(int)

    model = Sequential()
    model.add(Dense(3, 10))
    model.add(Activation('relu'))
    model.add(Dense(10, 1))
    model.add(Activation('sigmoid'))

    model.compile(loss = 'binary_crossentropy',optimizer = 'adam',class_mode = 'binary')

    model.fit(x,y,nb_epoch=1000,batch_size=10)
    yp = model.predict_classes(x).reshape(len(y))

    cm_plot(y,yp).show()


def chapter5_2():
    inputfile = 'consumption_data.xls'
    outerfile = 'data_type.xls'
    k = 3
    iteration = 500
    data = pd.read_excel(inputfile,index_col= 'Id')
    data_zs = 1.0 *(data-data.mean())/data.std()
    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=k,n_jobs=4,max_iter=iteration)
    model.fit(data_zs)
    r1 = pd.Series(model.labels_).value_counts()
    r2 = pd.DataFrame(model.cluster_centers_)
    r = pd.concat([r2,r1],axis=1)
    r.columns = list(data.columns) + ['类别数目']
    print(r)
    r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis = 1)
    r.columns = list(data.columns) + ['聚类类别']
    # r.to_excel(outerfile)
    print(r)


def density_plot(data,title):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure()
    for i in range(len(data.iloc[0])):
        (data.iloc[:,i]).plot(kind = 'kde',label = data.columns[i],linewidth = 2)
    plt.ylabel('密度')
    plt.xlabel('人数')
    plt.title('聚类类别%s各属性的密度曲线',title)
    plt.legend()
    return plt

if __name__ == '__main__':
    # chapter5_1()
    chapter5_2()