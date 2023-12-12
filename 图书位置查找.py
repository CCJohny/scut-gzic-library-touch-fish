import requests
from bs4 import BeautifulSoup

input_file = 'input.txt'
with open(input_file, 'r') as f:
    bkids = f.readlines()

url='http://202.38.247.161:8080/Graph.aspx'
s1='图书位置信息非实时更新，您要找的图书可能已被其他读者借阅，不在应有位置！如有不便，敬请谅解！条码为'
s2='的图书所在位置：'
s3='（导航提示：从大门进入，参照路线图提示方位。如需借阅国际校区密集书库图书，请咨询国际校区二楼服务台。）'

output_file = 'output.xls'
with open(output_file, 'w') as f:
    for bkid in bkids:
             param = { 'Bookid':bkid.strip() }
             response = requests.get(url=url,params=param)
             soup = BeautifulSoup(response.text, 'html.parser')
             table = soup.find('table')
             td = table.find('td')
             if(td):
                f.write(bkid.strip() + '\t' + td.text.replace(s1, '').replace(bkid.strip(), '').replace(s2, '').replace(s3, '') + '\n')
             else:
                f.write(bkid.strip() + '\t' + '系统无法对此条形码进行查询操作！' + '\n')