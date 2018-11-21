import numpy as nup #专门用来创建列表的库
import pandas as pd#数据表格
nup.array([1,2,3])#创建矩阵
matrix1 = nup.zeros((2,3,3))#0填充矩阵
matrix2 = nup.ones((2,2))#1填充矩阵
matrix3 = nup.arange(1,9,2)#等差数列，（初始值，终值，步长）
matrix4 = nup.linspace(1,10,10)#等差数列，（初始值，终值，袁术个数）
matrix5 = nup.logspace(0,3,2)#等比数列，（初始值，终值，个数）
matrix6 = nup.random.random((3,3))#0-1间的随机数，（（行数，列数））
matrix7 = nup.random.randint(10,100,size=(3,3))#随机整数（初始值，终值，size=（行数，列数））
matrix8 = nup.random.randn(3,3)#正态分布，（行数，列数）
matrix9 = nup.random.rand(5)#0-1之间的随机数，（个数）
matrix10 = nup.random.randint(1,10,size=(2,3))
matrix11 = nup.ones((3,3))
matrix12 = nup.array([[2,2,2],[2,2,2],[2,2,2]])
#print(matrix7.shape)#形状
#print(matrix7.ndim)#维度
#print(matrix7.size)#个数
#print(matrix7.dtype)#数据类型
#print(matrix7.itemsize)#元素大小
#print(matrix7.astype(float))#更改元素数据类型
#print(matrix11.dot(matrix12))
#前面用三维矩阵演示索引和切片
matrix13 = nup.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
#print(matrix13[0,1,2])#期望值是5，参数是（第一维，第二维，第三维）
#print(matrix13[0,:,1])#期望值，[2,5,8]
#print(matrix13[:,:,1])#期望值，[[2,5,8],[11,14,17]
'''花式索引，每一层中括号中的数表示上一层对下一层的选取,比如下面的表示选取0和1两个二维里面的0和1两个二维的0和0元素'''
#print(matrix13[[0,1],[0,1],[0,0]])#期望值是[1,13]
#索引器
'''下面的结果是[[[ 1  2][ 4  5]],[[10 11][13 14]]]]，与花式索引的区别是花式索引时是层层筛选，而索引器是层层叠加'''

#print(matrix13[nup.ix_([0,1],[0,1],[0,1])])
#print(matrix10.transpose())#矩阵转置
#print(matrix10.T)#矩阵转置
#print(nup.where([[True,False],[True,False]],[[1,2],[3,4]],[[5,6],[7,8]]))#选择函数
#条件选择
matrix14 = nup.array([1,2,3])
matrix15 = nup.array([4,5,6])
#print([m14 if compare else m15 for(m14,m15,compare) in zip(matrix14,matrix15,matrix14 < matrix15)])
#------------------------------------------------------------------------------------------#
'''Series形式像字典，是带索引的数据集合；通过列表创建的索引默认从0开始增加；还可以通过字典创建'''
series1 = pd.Series(nup.array([1,2,3,4]))
series2 = pd.Series({'a':1,'b':2})
series3 = pd.Series(data=[1,2,3],index=['k','j','l'])
#print(series3[series3 > 1])
#---------------------------------------------------------------------------------------------#
#DataFrame表格
frame1 = pd.DataFrame([['Ann','Steve','Sam'],[90,91,92],['class1','class2','class3']],index=['name','goal','class'],
columns=['c1','c2','c3'])
frame2 = pd.DataFrame({'class':['c1','c2','c3'],'goal':[93,94,95]},index=['Ann','Steve','Sam'])
print(frame2.goal)
#添加列
#frame2['address'] = ['p1','p2','p3']
#删除列
#frame2.pop('class')
#print(frame2)
#print(frame2['goal'])
#取值
#print(frame2.loc['Ann','goal'])#取Ann行的goal列
#print(frame2.loc['Ann'])#取一行的信息
#---------------------------------------------------------------------------------------
#用pandas读取文件
#csv = pd.read_csv('testData.csv')
#txt = pd.read_csv('testData.txt',sep = ';')
#print(csv)
#print(txt)
#excel = pd.read_excel('testData.xlsx')
#print(excel)