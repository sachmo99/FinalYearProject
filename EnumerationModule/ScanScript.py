import subprocess
import json
import sys
def SCAN(ip):
    filename = ip.split('.')
    filename = ":".join(filename)
    nmap_scan = subprocess.Popen(["sudo /usr/bin/nmap -sV -sT -p- -O -oX ~/Desktop/Final_Year_Project/cache/"+filename+".xml " +ip],shell=True,
                        stdout=subprocess.PIPE)
    print(nmap_scan)
    output = nmap_scan.stdout.read()
    print(output)
    return filename
#print(dir(nmap))
if __name__ == '__main__':
    print(SCAN(sys.argv[1]))
