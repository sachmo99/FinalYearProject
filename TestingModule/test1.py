
import xml.etree.ElementTree as et
import os
import json
import subprocess
import sys
def CVE_SCAN(ipaddress_file):
    with open('/home/kali/Desktop/Final_Year_Project/cve_db_output.json','r') as json_file:
        data_json = json.load(json_file)
    sys.stdout = open('/home/kali/Desktop/Final_Year_Project/cache/'+ipaddress_file+'.txt','w+')
    tree = et.parse('/home/kali/Desktop/Final_Year_Project/cache/'+ipaddress_file+'.xml')
    root = tree.getroot()
    # print(root)
    # print(root.getchildren())
    # print(root[4][4].getchildren())
    ports = root[3][3]
    service_list = []
    for port in root.iter('port'):
        service = port.find('service')
        attributes = service.attrib
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
    for x in service_list:
        if not x.startswith("unknown"):
            process = subprocess.Popen(['searchsploit','-j','-w',x],stdout=subprocess.PIPE,universal_newlines=True)
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
    return ipaddress_file

if  __name__ == "__main__":
    print(CVE_SCAN(sys.argv[1]))                   