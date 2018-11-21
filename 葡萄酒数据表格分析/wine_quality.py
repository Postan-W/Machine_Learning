import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
'''matplotlib是最基础的可视化库
seaborn针对的点主要是数据挖掘和机器学习中的变量特征选取，sea
born可以用短小的代码去绘制描述更多维度数据的可视化效果图。（比如可以通过seaborn.heatmap画出各特征之间的相关度图，找出冗余特征）'''
#读取数据文件，sep是分隔符，header=0是指第一行作为列标题
wine = pd.read_csv('wine_data.csv',sep=',',header=0)
#将列标题单词之间的空格替换成'_'
wine.columns = wine.columns.str.replace(' ','-')
#print(wine.head(0))#head的参数为整数，表示表格的头n行数据
#print(wine.describe())#总体描述性统计量
'''
其结果将包括count，mean，std，min，max以及百分位数。默认情况下，百分位数分三档：25%，50%，75%，其中第50百分位数就是中位数。

count：计数，这一组数据中包含数据的个数
mean：平均值，这一组数据的平均值
std：标准差，这一组数据的标准差
min：最小值
max：最大值
百分位数：
第p百分位数是这样一个值，它使得至少有p%的数据项小于或等于这个值，且至少有(100-p)%的数据项大于或等于这个值。以身高为例，身高分布的第五百分位表示有5%的人的身高小于此测量值，95%的身高大于此测量值。

对象类型的数据（例如字符串或时间）
其结果包括count，unique，top，和freq。时间数据还包括first和last项目。

count：同上
unique：表示有多少种不同的值
top：数据中出现次数最高的值
freq：出现次数最高的那个值（top）的出现频率
'''
#找出质量的唯一值
#print(sorted(wine.quality.unique()))
#计算值的频率
#print(wine.quality.value_counts())
#按葡萄酒类型获取描述性统计量，并且只需要quality列的数据,unstack()表示分组值不是从上到下堆叠，参数无实义
#print(wine.groupby('type')[['quality']].describe().unstack('type'))
#按葡萄酒类型显示特定的分位数值
#print(wine.groupby('type')[['quality']].quantile([0.25,0.75]).unstack('type'))
#按葡萄酒的类型获取其质量的数据
red_wine = wine.loc[wine['type']== 'red','quality']
white_wine = wine.loc[wine['type']=='white','quality']
#sns.set_style('dark')
#sns.distplot(red_wine,norm_hist=True,kde=False,color='red',label='red wine')
#sns.distplot(white_wine,norm_hist=True,kde=False,color='white',label='red wine')
#sns.axlabel('Quality Score','Density')
#plt.title('Distribution of Quality by Wine Type')
#plt.legend()
#plt.show()
#检验两种葡萄酒平均质量
#print(wine.groupby('type')[['quality']].agg(['std']))#agg是个集成查询函数，这里是对两种葡萄酒质量的标准差进行查询
#基于标准差的t检验
#t_station,pvalue,df = sm.stats.ttest_ind(red_wine,white_wine)
#print('t_station:%.3f pvalue:%.3f'%(t_station,pvalue))


'''----------------------------------------------------------------------------------------------
质量、酒精含量和残余糖分三个变量两两间的散点图、回归直线和直方图，按葡萄酒类型分类
-------------------------------------------------------------------------------------------------'''
#corr可以计算出所有变量两两之间的线性相关性,，返回对象是dataframe，n行n列
#print(wine.corr())
#下面定义选取任意的200行的函数
def take_sample(data_frame,replace=False,n=200):
    return data_frame.loc[np.random.choice(data_frame.index,replace=replace,size=n)]
#上面的参数意义分别为列表或一个整数（如果是一个整数n，那么函数会把它转为列表np.arange(n)等差数列）、是否要重复值、元素个数
red_sample = take_sample(wine.loc[wine['type']=='red',:])
white_sample = take_sample(wine.loc[wine['type']=='white',:])
wine_sample  = pd.concat([red_sample,white_sample])#默认是对行进行拼接
#添加一个列用来保存被选取的行，被选取值为1，否则值为0
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index),1.,0.)
#print(pd.crosstab(wine.in_sample,wine.type,margins=True))
'''
上面的打印结果
type        red  white   All
in_sample
0.0        1399   4698  6097
1.0         200    200   400
All        1599   4898  6497
'''
#-------------------------------------------------------------------------------------------------------
#下面生成图形
sns.set_style('dark')
#pairplot可以创建一个统计图的矩阵，diag_kind参数指定主对角线上以直方图或密度图形式展示，其他按散点图展示
g = sns.pairplot(wine_sample,kind='reg',
hue='type',diag_kind='hist',diag_kws={'bins':10,'alpha':1.0},palette=dict(red='red',white='brown'),
markers=['o','s'],vars=['quality','alcohol','residual-sugar'])
plt.suptitle('Histograms and Scatter Plots of Quality,Alcohol and Residual_Sugar',fontsize=14,horizontalalignment=
             'center',verticalalignment='top',x=0.5,y=0.999)
plt.show()
#---------------------------------------------------------------------------------
'''相关系数和两两变量间的统计图有有助于对两个变量之间的关系进行量化和可视化，对于测量每个变量在其他变量不变时与因变量之间的关系
应该也是用线性回归
'''
