import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def chapter3_1():
    data = pd.read_excel('catering_sale.xls',index_col=u'日期')

    data.describe()

    plt.figure()
    p = data.boxplot(return_type='dict')
# print(p['fliers'])
    x = p['fliers'][0].get_xdata()
    y = p['fliers'][0].get_ydata()
    y.sort()
    plt.show()


def chapter3_2():
    data = pd.read_excel('catering_dish_profit.xls',index_col=u'菜品名')
    data = data['盈利'].copy()
    print(data)
    data.sort(ascending = False)

    plt.figure()
    data.plot(kind = 'bar')
    plt.ylabel('盈利（元）')
    p =1.0 * data.cumsum()/data.sum()
    p.plot(color = 'r',secondary_y = True,style = '-o',linewidth =2 )
    plt.annotate(format(p[6],'.4%'),xy=(6,p[6]))
    plt.ylabel('比例')
    plt.show()


def chapter3_3():
    data = pd.read_excel('catering_sale_all.xls',index_col='日期')
    # print(data.corr())

    # print(data.corr()['百合酱蒸凤爪'])

    # print(data['翡翠蒸香茜饺'].corr(data['百合酱蒸凤爪']))


if __name__ == '__main__':
    # print(data.describe())
    # chapter3_2()
    # chapter3_3()

    data = [1,2,3,4,5,6,7]
    data = np.array(data)
    print(data.cumsum())
    print(data.cumprod())