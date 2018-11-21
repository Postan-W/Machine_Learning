from pyecharts import Bar,Line,Overlap,Pie

def draw_bar(x_axis,y_axis,title,vice_title):
    bar  = Bar(title,vice_title)
    bar.add('薪资占比',x_axis,y_axis)
    bar.use_theme('dark')
    bar.render()
def draw_pie(x_axis,y_axis,title):
    pie =Pie(title,title_pos='center',width=800,height=800)
    pie.add('玫瑰花图',x_axis,y_axis,center=[50,50],is_random=True,radius=[5,75],rosetype='area',
            is_legend_show=False,is_label_show=True)
    pie.render()
'''center为调整饼图圆心坐标（相对于Pie对象大小的百分比）
is_random为是否随即排列颜色列表（bool）
radius为半径(相对于Pie对象大小的百分比)，第一个为内圆半径,越小会使数据看起来更紧凑，第二个是标识线的长度，太大了会使文字超出图形而看不到
rosetype为是否展示成南丁格尔图
  'radius'
    圆心角，半径都展现数据大小
   'area'
    圆心角相同，为通过半径展现数据大小
is_label_show为是否显示标签（各个属性的数据信息） label_text_size为调整标签字体大小'''
