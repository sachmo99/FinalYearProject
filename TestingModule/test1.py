
import xml.etree.ElementTree as et
import os
import json
import subprocess
import sys
with open('../cve_db_output.json','r') as json_file:
    data_json = json.load(json_file)
sys.stdout = open('output.txt','w+')
tree = et.parse('result.xml')
root = tree.getroot()
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# print(root.tag)
# print(root.attrib)
ports = root[3][3]
# for x in ports:
#     for y in x:
#         print(y)
service_list = []
for port in root.iter('port'):
    service = port.find('service')
    attributes = service.attrib
    # service_list.append(attributes['product'] + " "+attributes['version'])
    temp = ""
    flag  = 0
    if "product" in attributes.keys():
        temp += attributes['product'] + " "
    elif "name" in attributes.keys():
        temp+= attributes['name']+" "
    if "version" in attributes.keys():
        temp += attributes['version']
        flag = 1
    if len(temp) == 0:
        #service_list.append(attributes['name'])
        pass
    elif flag == 1:
        service_list.append(temp)
    else:
        service_list.append(temp)
        #pass
#print(service_list)

# stream = os.popen('searchsploit -j ' + service_list[0])
# output = stream.read()
# print(help(json))
for x in service_list:
    if not x.startswith("unknown"):
        process = subprocess.Popen(['searchsploit','-j','-w',x],stdout=subprocess.PIPE,universal_newlines=True)
        # while process.poll() is None:
        #     #do nothing
        #     #print("Searching DB for",x," ....")
        #     pass
        output = process.stdout.read()
        sample_op = json.loads(output)
        if len(sample_op['RESULTS_EXPLOIT'])!= 0:
            print(x,sample_op['SEARCH'],":", "CRITICAL EXPOSURE")
            for y in sample_op['RESULTS_EXPLOIT']:
                edb_id = y['URL'].split('/')[-1]
                if edb_id in data_json.keys():
                    print("|_",y['Title'],"CVE_ID:",data_json[edb_id])
                    print("|___|_","URL:",y['URL'])
                else:
                    print("|_",y['Title'],"URL:",y['URL'])
                #r = requests.get(y['URL'])
                # r = requests.get(y['URL'],headers=headers)
                # s = BeautifulSoup(r.text,'html.parser')
                # ans = s.find_all('h6')
                # for z in ans:
                #     print("Possible CVE ID:",z.text.strip())
                

                
            #print()