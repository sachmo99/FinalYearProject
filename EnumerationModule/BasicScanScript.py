import sys
import nmap
import datetime
import os
import subprocess
def SCAN(ip):
    scanner = nmap.PortScanner() 
    timeNow  = datetime.datetime.now()
    fileName = ':'.join(ip.split('.'))+".txt"
    # os.system("nmap  -p0-65535 -A -oN "+ fileName+" -sV "+ ip)                                     
    scanner.scan(ip,"0-65535",arguments='-sC -A')                                              
    varFile = open("copy_"+fileName,"w")                                  
    varFile.write('Host : %s (%s) \n' % (ip, scanner[ip].hostname()))
    varFile.write('State : %s \n' % scanner[ip].state())
    print(scanner[ip])
    for output in scanner[ip]['hostscript']:
        if output['id'] == 'smb-os-discovery':
            varFile.write('OS Data : {0}\n'.format(output['output']))
    varFile.write('Protocol : tcp \n')
    proto = 'tcp'
    lport = list(scanner[ip][proto].keys())
    varFile.write('Port,State,Service,Product\n')
    for port in lport:
        varFile.write(str(port) + "," + scanner[ip][proto][port]['state'] + "," + scanner[ip][proto][port]['name'] + "," + scanner[ip][proto][port]['product'] + "\n")
    return filename


#print(dir(nmap))
if __name__ == '__main__':
    print(SCAN(sys.argv[1]))
