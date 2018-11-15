from pyecharts import Bar,Line,Overlap,Pie

def draw_bar(x_axis,y_axis,title,vice_title):
    bar  = Bar(title,vice_title)
    bar.add('薪资占比',x_axis,y_axis)
    bar.use_theme('dark')
    bar.render()
def draw_pie(x_axis,y_axis,title):
    pie =Pie(title,title_pos='center',width=1000)
    pie.add('玫瑰花图',x_axis,y_axis,center=[75,50],is_random=True,radius=[30,75],rosetype='area',
            is_legend_show=False,is_label_show=True)
    pie.render()
