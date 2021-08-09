import json
import subprocess
import os
import sys

def gobuster_test(ip_address,username="",password=""):
    command_output = subprocess.Popen(['gobuster','dir','-u',ip_address,'-w','//usr//share//wordlists//dirb//common.txt','-U',username,'-P',password,'-q','-e','-b 403,404','-r'],stdout=subprocess.PIPE,universal_newlines=True).stdout.read()
    #print(command_output.stdout.read())
    #gobuster dir -u http://192.168.0.102 -w /usr/share/wordlists/dirb/common.txt -U admin -P password -q -e -b 403,404 -r
    command_output = command_output.split("\n")
    for x in range(len(command_output)):
        command_output[x] = command_output[x].split("(")
    print(command_output)
    ip_out = ":".join(ip_address.split("."))
    f = open('/home/kali/Desktop/Final_Year_Project/cache/'+ip_out+"_gobuster_report.txt","w")
    f.write("The following URLs are accessible by bruteforcing. Please check their security. \n")
    f.write("GOBUSTER SCAN \n")
    for x in command_output:
        if x[0] != '':
            f.write(x[0]+" : "+x[1][:-1] + "\n")
    f.close()
    return ip_out+"_gobuster_report.txt"


if __name__ == "__main__":
    if len(sys.argv) > 2:
        gobuster_test(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        gobuster_test(sys.argv[1])