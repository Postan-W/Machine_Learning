import pandas as pd
import sys
import os
import drawer
import numpy as np
#如果路径有中文，先获取文件再读取csv
file = open(r'C:\Users\Administrator\Desktop\MachineLearing\葡萄酒数据表格分析\wine_data.csv')
data = pd.read_csv(file,header=0,sep=',')
file.close()
data.columns = data.columns.str.replace(' ','_')
#几千行的数据太多，选取200行
data_smaller = data.loc[np.random.choice(data.index,replace=True,size=200),:]
drawer.draw_pie(data_smaller['fixed_acidity'],data_smaller['volatile_acidity'],'测试')