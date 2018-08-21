 # 将pandas.rpy.common导入为com
import pandas as pd
import pandas.rpy.common as com
 # filename =“weights.sav”
 # w = com.robj.r（'foreign :: read.spss（“％s”，to.data.frame = TRUE）'％filename）
 # w = com.convert_robj（w）
 # w.head（）
 # ID重量长度头饰教育学士学位
 # 1 L001 3.95 55.5 37.5女大专3名以上兄弟姐妹
 # 2 L003 4.63 57.0 38.5女性单身人士
 # 3 L004 4.75 56.0 38.5男年12兄弟姐妹
 # 4 L005 3.92 56.0 39.0男高级一兄弟
 # 5 L006 4.56 55.0 39.5男
 # 年10兄弟姐妹

filename = '20170913-2.sav'
w = com.robj.r('foreign :: read.spss（“％s”，to.data.frame = TRUE）'%filename)
w = com.convert_robj(w)
w.head()