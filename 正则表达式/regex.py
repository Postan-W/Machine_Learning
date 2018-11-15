import re

pattern5 = re.compile('\d')
print(pattern5.sub('-','one1two2three3four'))
print(re.sub('\d','-','one1two2three3four'))
pattern6 = re.compile('(\w+) (\d+)')
#group(0)相当于group（）
for i in pattern6.finditer('pretty 123,good 456'):
    print(i.group(0))
    print(i.group(1))
    print(i.group(2))

#分组之间的替换
print(pattern6.sub(r'\2 \1','pretty 123,good 456'))
print(re.sub('(\w+) (\d+)',r'\2 \1','pretty 123,good 456'))
#电话号码部分遮盖
pattern7 = re.compile('(\d{3})(\d{4})(\d{4})')
print(pattern7.sub(r'\1****\3','15216802238and15216802239'))

#贪婪模式与非贪婪模式
#贪婪模式
str = 'aaa<p>hello<p>hello<p>addfa<p>'
print(re.compile('<p>.*<p>').findall(str))
#非贪婪模式
print(re.compile('<p>.*?<p>').findall(str))
#中文的匹配
print(re.findall('[\u4e00-\u9fa5]+','你好，hi，朋友'))
#match只成功匹配一次，不在向后匹配,若果开头没能匹配则返回none
pattern8 = re.compile('\d+')
print(pattern8.match('123def456').group())
#search值成功匹配一次，但与match相比不必限定在开头
pattern8 = re.compile('\d+')
print(pattern8.search('abc123def456').group())