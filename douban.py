import requests
from lxml import etree
import time
with open('moviedata1.txt', 'w', encoding='utf-8') as f:
    for a in range(10):
        url = 'https://movie.douban.com/top250?start={}'.format(a*25)
        data = requests.get(url).text
        s = etree.HTML(data)

        file = s.xpath('//*[@id="content"]/div/div[1]/ol/li')

        for div in file:
            title = div.xpath("./div/div[2]/div[1]/a/span[1]/text()")[0]
            score = div.xpath("./div/div[2]/div[2]/div/span[2]/text()")[0]
            number = div.xpath("./div/div[2]/div[2]/div/span[4]/text()")[0]
            href = div.xpath("./div/div[2]/div[1]/a/@href")[0]
            dir = div.xpath("./div/div[2]/div[2]/p[1]/text()")[0]+div.xpath("./div/div[2]/div[2]/p[1]/text()")[1]
            say = div.xpath("./div/div[2]/div[2]/p[2]/span/text()")[0]
            f.write("{}　　　　　　　	   {}　　　　　　　	   {}　　　　　　　	   {}     {}\n {}\n\n\n".format(title, href, score, number, dir, say))
            time.sleep(0.05)

'''for i in name:
    i = ''.join(i.split())
    i = i.strip('/')
    print(i)
    print(score[p])
    if p <= 20 :
         p=p+1
//*[@id="content"]/div/div[1]/div[2]/table[1]/tr/td[2]/div/div/span[2]
//*[@id="content"]/div/div[1]/div[2]/table[1]/tr/td[2]/div/a
//*[@id="content"]/div/div[1]/div[2]
//*[@id="content"]/div/div[1]/div[2]/table[2]/tr/td[2]/div/a
//*[@id="content"]/div/div[1]/ol/li[1]
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[2]
//*[@id="content"]/div/div[1]/ol/li[1]
https://movie.douban.com/tag/top100?start=20&type=S
https://movie.douban.com/tag/top100?start=40&type=S
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/div/span[4]
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[1]/a/img
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[1]
//*[@id="content"]/div/div[1]/ol/li[1]/div/div[2]/div[2]/p[2]/span
//*[@id="ext-gen2801"]/td[4]/div
//*[@id="gridview-1215"]/table/tbody/tr[3]/td[4]/div
//*[@id="gridview-1215"]/table/tbody/tr[4]/td[4]/div
//*[@id="ext-gen2801"]/td[4]/div
//*[@id="ext-gen2807"]/td[4]/div
//*[@id="gridview-1215"]/table/tbody/tr[6]/td[4]/div
'''
