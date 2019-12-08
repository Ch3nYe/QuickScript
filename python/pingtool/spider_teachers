from requests import request
from lxml import etree

response = request(url="https://scss.bupt.edu.cn/info/1063/1136.htm",method="GET")

response = response.content.decode('utf-8')
html = etree.HTML(response)

name = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[1]/td[2]/p/span/text()'))
click = ''.join(html.xpath('/html/body/div[3]/div[1]/div[2]/form/div[1]/i/script/text()')).split(',')[-1][:-1]
sex = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[2]/td[2]/p/span/text()'))
zhiwu = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[3]/td[2]/p/span/text()'))
xueshujianzhi = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[4]/td[2]/p/span/text()'))
laoshileixing = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[5]/td[2]/p/span/text()'))
suoshuzhongxin = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[6]/td[2]/p/span/text()'))
zhicheng = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[7]/td[2]/p/span/text()'))
chengdankecheng = ' '.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[8]/td[2]/p//span//text()'))
yanjiufangxiang = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[9]/td[2]/p/span/text()'))
gerenjieshao = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[10]/td[2]/p//text()'))
chengdanketi = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[11]/td[2]/p//span/text()'))
huojianghechengguo = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[12]/td[2]//p//text()'))
fabiaolunwen = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[13]/td[2]/p//span//text()'))
lianxidianhua = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[14]/td[2]//span//text()'))
gongzuodidian = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[15]/td[2]//span//text()'))
email = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[16]/td[2]//span//text()'))
beizhu = ''.join(html.xpath('//*[@id="vsb_content"]/div/div/table/tbody/tr[17]/td[2]//span//text()'))

print('姓名','----',name)
print('点击量','----',click)
print('性别','----',sex)
print('职务','----',zhiwu)
print('学术兼职','----',xueshujianzhi)
print('老师类型','----',laoshileixing)
print('所属中心','----',suoshuzhongxin)
print('职称','----',zhicheng)
print('承担课程','----',chengdankecheng)
print('研究方向','----',yanjiufangxiang)
print('个人介绍','----',gerenjieshao)
print('承担课题','----',chengdanketi)
print('获奖和成果','----',huojianghechengguo)
print('发表论文','----',fabiaolunwen)
print('联系电话','----',lianxidianhua)
print('工作地点','----',gongzuodidian)
print('email','----',email)
print('备注','----',beizhu)



