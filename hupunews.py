import requests

from lxml import etree
with open('hupunews.txt', 'w', encoding='utf-8') as f:
    for a in range(10):
        url = 'https://voice.hupu.com/nba/{}.html'.format(2270998+a)
        data = requests.get(url).text
        s = etree.HTML(data)
        news = s.xpath('/html/body/div[4]/div[1]/div[2]/div/div[2]')

        for div in news:
            lenStory = div.xpath('./p/text()')
            title = div.xpath('/html/body/div[4]/div[1]/div[1]/h1/text()')[0]
            """print(title)"""
            f.write("{}\n\n\n".format(title))
            for i in range(len(lenStory)):
                story = div.xpath('./p/text()')[i]
                f.write("{}\n\n\n".format(story))





'''''//*[@id="gridview-1098"]/table/tbody/tr[5]/td[4]/div
//*[@id="gridview-1098"]/table/tbody/tr[6]/td[4]/div
//*[@id="gridview-1098"]/table/tbody/tr[7]/td[4]/div
//*[@id="ext-gen2412"]/td[4]/div
//*[@id="sports"]/div[2]/div[1]/ul/li[1]
//*[@id="sports"]/div[2]/div[1]/ul/li[2]/a
//*[@id="sports"]/div[2]/div[1]/ul/li[3]/a
//*[@id="sports"]/div[2]/div[1]
//*[@id="sports"]/div[2]/div[1]/div[2]/h3/a
/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/a
/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a
/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/ul
/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/ul/li[7]/a
/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/ul/li[6]/a
/html/body/div[4]/div[1]/div[2]/div/div[2]/p[1]
/html/body/div[4]/div[1]/div[2]/div/div[2]/p[2]
/html/body/div[4]/div[1]/div[2]/div/div[2]/p[1]
/html/body/div[4]/div[1]/div[1]/h1'''