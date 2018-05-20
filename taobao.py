import requests

from lxml import etree
with open('taobaopaper.txt', 'w', encoding='utf-8') as paper:
    for i in range(10):
        url = 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&clk1=5eceeacc5efaaa564368c049f1f0be57&keyword=%E5%8D%AB%E7%94%9F%E7%BA%B8&page={}'.format(i)
        data = requests.get(url).text
        s = etree.HTML(data)
        lenth = s.xpath('//*[@id="ItemWrapper"]/div/a/div[2]/span/text()')
        for i in range(len(lenth)):
            news = s.xpath('//*[@id="ItemWrapper"]/div/a/div[2]/span/text()')[i]
            price = s.xpath('//*[@id="ItemWrapper"]/div/a/div[2]/p[1]/span[1]/strong/text()')[i]
            '''print('{}'.format(news))
            print(price.strip())'''
            paper.write('{}                                                      {}'.format(news,price.strip()))














'''//*[@id="ItemWrapper"]/div[1]/a/div[2]/span
//*[@id="ItemWrapper"]/div[1]/a/div[2]/p[1]/span[1]
//*[@id="ItemWrapper"]/div[2]/a/div[2]/span
//*[@id="ItemWrapper"]/div[2]/a/div[2]/p[1]/span[1]
//*[@id="ItemWrapper"]/div[7]/a/div[2]/span
//*[@id="ItemWrapper"]/div[1]/a/div[2]/p[1]/span[1]
//*[@id="ItemWrapper"]/div[2]/a/div[2]/p[1]/span[1]
//*[@id="ItemWrapper"]/div[7]/a/div[2]/p[1]/span
//*[@id="ItemWrapper"]/div[3]/a/div[2]/p[1]/span[1]
//*[@id="ItemWrapper"]/div[4]/a/div[2]/p[1]/span
//*[@id="ItemWrapper"]/div[1]/a/div[2]
//*[@id="ItemWrapper"]/div[1]/a/div[2]/span
//*[@id="ItemWrapper"]/div[1]/a/div[2]/span
//*[@id="ItemWrapper"]/div[2]/a/div[2]/span
//*[@id="ItemWrapper"]/div[2]/a/div[2]/p[1]/span[1]/strong
//*[@id="ItemWrapper"]/div[100]/a/div[2]/p[1]/span[1]/strong'''