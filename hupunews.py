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





