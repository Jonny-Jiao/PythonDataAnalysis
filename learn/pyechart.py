from pyecharts import Bar
import pandas as pd
from functools import *
import math
import numpy as np
# import moviepy.editor
from scipy.optimize import fsolve
from scipy import integrate

def bar():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar("柱状图数据堆叠示例")
    bar.add("商家A", attr, v1, is_stack=True)
    bar.add("商家B", attr, v2, is_stack=True)
    bar.render(path='../templates/learn/pye_bar.html')


def test_reduce():
    print(reduce( lambda x,y:x*y,range(1,5)))


def numpy_test():
    b = np.array([[1,2,3],[5,7,9]])
    print(b*b)


def scipy_fsolve_test():
    def f(x):
        x1 = x[0]
        x2 = x[1]
        return [2*x1-x2**2-1,x1**2-x2-2]
    result = fsolve(f,[0,0])
    print(result)


def scipy_integrate_test():
    def g(x):
        return (1-x**2)**0.5

    pi_2,err = integrate.quad(g,-1,1)
    print(pi_2 * 2)

if __name__ == '__main__':
    # bar()
    # test_reduce()
    # print(math.sin(1))

    # print(np.array([2,0,1,5]))
    # numpy_test()

    # scipy_test()
    scipy_integrate_test()