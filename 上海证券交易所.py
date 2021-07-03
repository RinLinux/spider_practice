import requests
import json

headers = {
    'Referer': 'http://www.sse.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}
res = requests.get(url='http://query.sse.com.cn/security/stock/queryCompanyBulletin.do?jsonCallBack=jsonpCallback57548&isPagination=true&productId=&securityType=0101%2C120100%2C020100%2C020200%2C120200&reportType2=DQBG&reportType=QUATER1&beginDate=2021-04-03&endDate=2021-07-03&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1625312697779'
                       ,headers=headers)
json_data = json.loads(res.text[19:-1])
for i in json_data['pageHelp']['data']:
    pdf_url = 'http://www.sse.com.cn' + i['URL']
    filename = i['TITLE'] + '.pdf'
#     print(pdf_url,i['TITLE'])
    resource = requests.get(pdf_url,stream=True)
    with open(filename,'wb') as f:
        for chunk in resource.iter_content(1024):
            f.write(chunk)
        print(filename)
