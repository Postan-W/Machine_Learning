import os
import re
import requests
import sys
from lxml import etree
import pandas as pd
'''下面的URL是ajax加载的内容，用BeautifulSoup或Xpath直接获取从网站链接返回的HTML文件的数据的方式往往得不到，目前暂时机械的手动
复制链接'''
urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperience=-1&education=-1&companyTy'
        'pe=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&_v=0.75420128&x-zp-page-re'
        'quest-id=c9349f50d8134129828a3fd6cdebb33f-1542252095592-546632','https://fe-api.zhaopin.com/c/i/so'
        'u?start=60&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-'
        '1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&_v=0.99050332&x-zp-page-request-id=0d1e51287340'
        '4c338d4746efade3c24b-1542252174922-491324','https://fe-api.zhaopin.com/c/i/sou?start=120&pageSiz'
        'e=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1'
         '&kw=Java%E5%BC%80%E5%8F%91&kt=3&_v=0.21924522&x-zp-page-request-id=f65894d42394423e8f24bf38a0ae'
         'a0d8-1542252221835-965786','https://fe-api.zhaopin.com/c/i/sou?start=180&pageSize=60&cityId=530&w'
        'orkExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E'
        '5%8F%91&kt=3&_v=0.73648157&x-zp-page-request-id=43e9b772d1d3405dbace142103faeec0-1542252270832'
        '-101478','https://fe-api.zhaopin.com/c/i/sou?start=240&pageSize=60&cityId=530&workExperience=-1&ed'
        'ucation=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Java%E5%BC%80%E5%8F%91&kt=3&_v=0.'
        '74425705&x-zp-page-request-id=6ea6c55a416e4e4c9a30dcb24717bd87-1542252321797-561186']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
'''根据对json文本的分析，json对象的键’data‘的值中的results键的对应值是一个json数组，保存的是所有公司信息，每一个公司
是一个json对象。{'number': 'CC398107113J00040907712', 'jobType': {'items': [{'code': '160000', 'name': '软件/互联网
开发/系统集成'}, {'code': '44', 'name': '高级软件工程师'}], 'display': '软件/互联网开发/系统集成,高级软件工程师'}, 'comp
any': {'number': 'CZ398107110', 'url': 'https://company.zhaopin.com/CZ398107110.htm', 'name': '北京盛学成长科技有
限公司', 'size': {'code': '3', 'name': '100-499人'}, 'type': {'code': '5', 'name': '民营'}}, 'positionURL': 'htt
s://jobs.zhaopin.com/CC398107113J00040907712.htm', 'workingExp': {'code': '510', 'name': '5-10年'}, 'eduLevel':
 {'code': '4', 'name': '本科'}, 'salary': '15K-25K', 'emplType': '全职', 'jobName': '高级java开发工程师', 'industr
 y': '160000,210500,160400', 'recruitCount': 0, 'geo': {'lat': '39.961822', 'lon': '116.464077'}, 'city': {'ite
 s': [{'code': '530', 'name': '北京'}], 'display': '北京'}, 'applyType': '1', 'updateDate': '2018-11-14 19:27:49
 ', 'createDate': '2018-10-08 15:42:12', 'endDate': '2019-08-04 15:42:12', 'welfare': ['节日福利', '带薪年假', '补
 充医疗保险', '五险一金', '定期体检'], 'saleType': 0, 'feedbackRation': 0.5984, 'score': 607.3427, 'resumeCount': 7
 35, 'showLicence': 0, 'interview': 0, 'companyLogo': 'http://company.zhaopin.com/CompanyLogo/20171122/287207C86
 1B14BA4B277D8A863542FCB.jpg', 'tags': [], 'vipLevel': 1003, 'expandCount': 0, 'positionLabel': '{"qualificati
 ons":null,"role":null,"level":null,"jobLight":["节日福利","带薪年假","补充医疗保险","五险一金","定期体检","绩效奖金",
 "弹性工作","周末双休"],"companyTag":null,"skill":null,"refreshLevel":2,"chatWindow":20}', 'duplicated': False,
 'futureJob': False,
 'selected': False, 'applied': False, 'collected': False, 'isShow': False, 'timeState': '最新', 'rate': '59%'}
'''
#下面存储职位名称，职位链接，公司名称，公司链接，公司性质，公司规模，工作经验要求，学历要求，薪资，招聘人数，所在城市，福利,工作时间
#下面的列表用于创建DataFrame，最终要导出excel文件

position = []
name_of_company = []
scale_of_company = []
number_required = []
category_of_company = []
experience = []
education = []
salary =[]
city = []
welfare = []
link_of_company = []
link_of_job = []
working_time = []
#下面对所有五个页面的招聘信息进行收集
for url in urls:
 response =requests.get(url,headers=headers)
 data = response.json()
 companies = data['data']['results']
 for company in companies:
    name_of_company.append(company['company']['name'])
    link_of_company.append(company['company']['url'])
    scale_of_company.append(company['company']['size']['name'])
    category_of_company.append(company['company']['type']['name'])
    link_of_job.append(company['positionURL'])
    experience.append(company['workingExp']['name'])
    education.append(company['eduLevel']['name'])
    salary.append(company['salary'])
    working_time.append(company['emplType'])
    position.append(company['jobName'])
    city.append(company['city']['display'])
    welfare.append(company['welfare'])
#直接利用列表数据制作词云，免去了中文分词的步骤
 import word_cloud
 word_cloud.generate_wordcloud(' '.join(salary))
 word_cloud.generate_wordcloud(' '.join(experience))
 word_cloud.generate_wordcloud(' '.join(education))
'''使用pyecharts库对薪水和学历要求进行可视化展示，因为薪水是’3K-11K‘这样的形式，需要
设定几个区间然后统计范围内的频率，学历的几种类型也要得到器出现的频率，所以下面先对数据进行整理
'''
salary_str = ''.join(salary)
#匹配的几个区间为3000-6000，6000-12000，12000-24000，24000-30000,30000-40000
salary1 = re.compile('[3456]K-[3456]K').findall(salary_str)
salary2 = re.compile('[6789]K-[6789]K|[6789]K-1[0-2]K|1[012]K-1[012]K').findall(salary_str)
salary3 = re.compile('1[2-9]K-1[2-9]K|1[2-9]K-2[0-4]K|2[0-4]K-2[0-4]K').findall(salary_str)
salary4 = re.compile('2[4-9]K-2[4-9]K|2[4-9]K-30K').findall(salary_str)
salary5 = re.compile('3[0-9]K-3[0-9]K|3[0-9]K-40K').findall(salary_str)
#下面计算比重
rate = []
rate1 = len(salary1)/len(salary)
rate2 = len(salary2)/len(salary)
rate3 = len(salary3)/len(salary)
rate4 = len(salary4)/len(salary)
rate5 = len(salary5)/len(salary)
rate.append(rate1)
rate.append(rate2)
rate.append(rate3)
rate.append(rate4)
rate.append(rate5)
import sys
#将上层目录路径添加到库搜索路径中
sys.path.append('..')
import drawer
drawer.draw_bar(['3K-6K','6K-12K','12K-24K','24K-30K','30K-40K'],rate,'智联招聘Java岗位薪资统计','共'+str(len(salary))+'家公司')
drawer.draw_pie(['3K-6K','6K-12K','12K-24K','24K-30K','30K-40K'],rate,'薪资占比玫瑰图')



frame = pd.DataFrame({'公司名称':name_of_company,'公司链接':link_of_company,'公司规模':scale_of_company,'所在城市':city,
                      '企业类型':category_of_company,'岗位名称':position,'岗位链接':link_of_job,
                      '工作经验':experience,'学历起点':education,'薪水':salary,'工作类型':working_time,
                      '福利':welfare})
frame.to_excel('智联北京Java岗位招聘信息.xlsx',sheet_name='第1页',header='北京Java岗位招聘信息',na_rep='NULL')













