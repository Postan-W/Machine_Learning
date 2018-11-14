import cv2
import aircv
def match_result(background,target):
    #第一个参数表示背景图像的路径，第二个参数表示要匹配的那部分内容的图片的路径;函数返回的是匹配部分的中心坐标
    t = aircv.imread(target)
    b = aircv.imread(background)
    result = aircv.find_template(b,t)
    return result['result']
#用cv2画图形
def draw_circle(background,pos,radius,color,line_width):
    #参数分别是背景图、位置，半径，颜色，线宽
    cv2.circle(background,pos,radius,color,line_width)
    cv2.imshow('match',background)
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__=='__main__':
    radius = 50
    color = (0,255,0)
    line_width = 5
    center = (int(match_result('background.jpg','target.jpg')[0]),int(match_result('background.jpg','target.jpg')[1]))
    draw_circle(aircv.imread('background.jpg'),center,radius,color,line_width)