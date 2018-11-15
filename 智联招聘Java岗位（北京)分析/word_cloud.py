from wordcloud import WordCloud, ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
#上面添加的是词云生成工具和中文分词工具
#定义用于分词的函数
def cut_text(filePath):
    with open(filePath,mode='r',encoding='utf-8') as file:
        my_text = file.read()
        cut_text = ' '.join(jieba.lcut(my_text))
        return cut_text
#将字符串转为词云，这里提供薪资、学历、工作经验三个字符串
def generate_wordcloud(str):
    #获取背景图片
    background = plt.imread('background.jpg')
    #建立词云对象
    cloud = WordCloud(
        background_color='white',  # 设置背景颜色
        mask=background,  # 背景图片
        font_path='C:\Windows\Fonts\STZHONGS.TTF',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
        max_words=200,  # 设置最大显示的字数
        stopwords='面议',  # 设置停用词
        max_font_size=75,  # 设置字体最大值
        random_state=50  # 设置有多少种随机形态，即多少种配色方案
    )
    cloud.generate_from_text(str)

    # 改变字体颜色
    img_colors = ImageColorGenerator(background)
    # 字体颜色为背景图片的颜色
    cloud.recolor(color_func=img_colors)
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()