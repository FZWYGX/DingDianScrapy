import requests
from scrapy import Selector
import re

url = 'https://www.23us.so/'
# url = 'https://www.23us.so/xiaoshuo/14786.html'
# url = 'https://www.23us.so/files/article/html/14/14786/index.html'
# url = 'https://www.23us.so/files/article/html/23/23684/11537118.html'

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
# }
#
# resp = requests.get(url, headers=headers)
# response = Selector(text=resp.content.decode())
#
# urls = response.xpath('//a/@href').extract()
# for url in urls:
#     print(url)

# index_url = response.xpath("//p[@class='btnlinks']/a/@href").extract_first()

# style = response.xpath("//div[@class='bdsub']/dl/dt/a//text()").extract()
# style = style[1]
# print(style)
# name = response.xpath("//div[@class='bdsub']/dl/dd[1]/h1/text()").extract_first().replace("最新章节", "")
# print(name)
# author = response.xpath("//div[@class='bdsub']/dl/dd[2]/h3/text()").extract_first().replace("作者：", "")
# print(author)
# chapters = response.xpath("//table[@id='at']//text()").extract()
# chaptersUrl = response.xpath("//table[@id='at']//a/@href").extract()
#
# xsChapter = {chapters[i]: chaptersUrl[i] for i in range(len(chapters))}
# print(xsChapter)


# print(url)
# name = response.xpath("//div[@class='bdsub']/dl/dt/a//text()").extract()
# name = name[-1]
# print(name)
# chapter = response.xpath("//h1/text()").extract_first().strip()
# print(chapter)
#
# content = response.xpath("//dd[@id='contents']//text()").extract()
# content = "\n".join(i.strip() for i in content if len(i.strip()) > 0)
# print(content)

sss = re.findall(r'https://www\.23us\.so/xiaoshuo/\d+\.html', 'https://www.23us.so/xiaoshuo/13317.html')
print(sss)




'https://www.23us.so/xiaoshuo/15536.html'
'https://www.23us.so/xiaoshuo/14823.html'
'https://www.23us.so/xiaoshuo/3475.html'
'https://www.23us.so/xiaoshuo/12817.html'
'https://www.23us.so/xiaoshuo/23302.html'
'https://www.23us.so/xiaoshuo/15729.html'
'https://www.23us.so/xiaoshuo/23686.html'

'https://www.23us.so/files/article/html/1/1961/index.html'
'https://www.23us.so/files/article/html/21/21694/index.html'
'https://www.23us.so/xiaoshuo/21867.html'


