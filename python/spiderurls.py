from requests import request
from lxml import etree
urls = []

for i in range(1,11):
    url = "https://scss.bupt.edu.cn/szdw/jsml/%s.htm" % (str(i))
    response = request(url=url, method='GET')
    response = response.content.decode('utf-8')
    html = etree.HTML(response)

    gets = html.xpath('/html/body/div[3]/div[2]/div[2]/div/ul//li/div/a/@href')
    # print("\n".join(gets))
    urls+=gets

# 第一页
response = request(url="https://scss.bupt.edu.cn/szdw/jsml.htm", method='GET')
response = response.content.decode('utf-8')
html = etree.HTML(response)
gets = html.xpath('/html/body/div[3]/div[2]/div[2]/div/ul//li/div/a/@href')
# print("\n".join(gets))
urls+=gets

print('总计：',len(urls))
print("\n".join(urls))
