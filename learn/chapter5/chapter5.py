import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from learn.chapter5.cm_plot import cm_plot
# from apriori import *
# import apriori

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

def chapter5_3_apriori():
    # 自定义连接函数，用于实现L_{k-1}到C_k的连接
    def connect_string(x, ms):
        x = list(map(lambda i: sorted(i.split(ms)), x))
        l = len(x[0])
        r = []
        for i in range(len(x)):
            for j in range(i, len(x)):
                if x[i][:l - 1] == x[j][:l - 1] and x[i][l - 1] != x[j][l - 1]:
                    r.append(x[i][:l - 1] + sorted([x[j][l - 1], x[i][l - 1]]))
        return r

    # 寻找关联规则的函数
    def find_rule(d, support, confidence, ms=u'--'):
        result = pd.DataFrame(index=['support', 'confidence'])  # 定义输出结果

        support_series = 1.0 * d.sum() / len(d)  # 支持度序列
        column = list(support_series[support_series > support].index)  # 初步根据支持度筛选
        k = 0

        while len(column) > 1:
            k = k + 1
            print(u'\n正在进行第%s次搜索...' % k)
            column = connect_string(column, ms)
            print(u'数目：%s...' % len(column))
            sf = lambda i: d[i].prod(axis=1, numeric_only=True)  # 新一批支持度的计算函数

            # 创建连接数据，这一步耗时、耗内存最严重。当数据集较大时，可以考虑并行运算优化。
            d_2 = pd.DataFrame(list(map(sf, column)), index=[ms.join(i) for i in column]).T

            support_series_2 = 1.0 * d_2[[ms.join(i) for i in column]].sum() / len(d)  # 计算连接后的支持度
            column = list(support_series_2[support_series_2 > support].index)  # 新一轮支持度筛选
            support_series = support_series.append(support_series_2)
            column2 = []

            for i in column:  # 遍历可能的推理，如{A,B,C}究竟是A+B-->C还是B+C-->A还是C+A-->B？
                i = i.split(ms)
                for j in range(len(i)):
                    column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

            cofidence_series = pd.Series(index=[ms.join(i) for i in column2])  # 定义置信度序列

            for i in column2:  # 计算置信度序列
                cofidence_series[ms.join(i)] = support_series[ms.join(sorted(i))] / support_series[
                    ms.join(i[:len(i) - 1])]

            for i in cofidence_series[cofidence_series > confidence].index:  # 置信度筛选
                result[i] = 0.0
                result[i]['confidence'] = cofidence_series[i]
                result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]

        result = result.T.sort(['confidence', 'support'], ascending=False)  # 结果整理，输出
        print(u'\n结果为：')
        print(result)

        return result

    inputfile = 'menu_orders.xls'
    outputfile = 'apriori_rule.xls'
    data = pd.read_excel(inputfile,header = None)

    print(data)
    print('\n转换原始矩阵到0-1矩阵')
    ct = lambda x:pd.Series(1,index=x[pd.notnull(x)])
    b = map(ct,data.as_matrix())
    # print('data.as_matrix()',data.as_matrix())
    # print('b',b)
    data = pd.DataFrame(list(b)).fillna(0)
    # print(data)
    print('\n转换完成')

    support = 0.2 #最小支持度
    confidence = 0.5 #最小置信区间
    ms = '----'
    result = find_rule(data,support,confidence,ms)
    # print(result)


if __name__ == '__main__':
    # chapter5_1()
    # chapter5_2()
    chapter5_3_apriori()
    pass