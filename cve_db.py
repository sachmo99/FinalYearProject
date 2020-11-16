import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
r = requests.get('https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html',headers=headers)
s = BeautifulSoup(r.text,'html.parser')
table_cve = s.find_all('table')[3].find_all('tr')
print(len(table_cve))
f = open('cve_db_output.json','w+')
f.write('{')
for x in table_cve:
    temp = x.find_all('td')
    print(temp[0].text.split(':')[1].strip(),temp[1].text.strip())
    f.write('"'+temp[0].text.split(':')[1].strip()+"\":\""+temp[1].text.strip()+'"')
    f.write(',')
f.write('}')
f.close()
