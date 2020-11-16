import sys
import nmap
import datetime
import os
def SCAN(ip):
    scanner = nmap.PortScanner() 
    timeNow  = datetime.datetime.now()
    fileName = ':'.join(ip.split('.'))+"_"+timeNow.strftime("%d_%m_%y_%H:%M:%S")+".txt"
    os.system("sudo nmap  -p- -O -A -oN "+ fileName+" -sV "+ ip)                                     
    scanner.scan(ip,"0-65535")                                              
    varFile = open(ip + '_' + str(datetime.datetime.now().strftime("%c")) + '.txt',"w")                                  
    varFile.write('Host : %s (%s) \n' % (ip, scanner[ip].hostname()))
    varFile.write('State : %s \n' % scanner[ip].state())
    osclass = scanner[ip]['osclass']
    varFile.write('OsClass.type : {0}\n'.format(osclass['type']))
    varFile.write('OsClass.vendor : {0}\n'.format(osclass['vendor']))
    varFile.write('OsClass.osfamily : {0}\n'.format(osclass['osfamily']))
    varFile.write('OsClass.osgen : {0}\n'.format(osclass['osgen']))
    varFile.write('OsClass.accuracy : {0}\n'.format(osclass['accuracy']))
    varFile.write('Protocol : tcp \n')
    proto = 'tcp'
    lport = list(scanner[ip][proto].keys())
    varFile.write('Port,State,Service,Version \n')
    for port in lport:
        varFile.write(port + "," + scanner[ip][proto][port]['state'] + "," + scanner[ip][proto][port]['service'] + "," + scanner[ip][proto][port]['version'] + "\n")
#print(dir(nmap))
SCAN(sys.argv[1])
