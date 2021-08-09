from fpdf import FPDF
import sys
import subprocess
def webtest_pdfmaker(filename):
    print("ssl print started")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=15)
    f = open('/home/kali/Desktop/Final_Year_Project/cache/'+filename+'_ssl_output.txt','r')
    pdf.cell(200,10,txt="WebTesting of "+filename,ln=1,align="C")
    pdf.set_font("Arial",size=8)
    #print(f.read())
    for x in f:
        #print(x)
        #if not x.startswith("|_"):
        pdf.set_text_color(r=255,g=0,b=0)
        pdf.cell(250,10,txt=x,ln=1)
        
        #print("----line break------")
    pdf.cell(250,10,txt="\n\n")
    f.close()
    print("gobuster print started")
    f = open('/home/kali/Desktop/Final_Year_Project/cache/'+filename+'_gobuster_report.txt','r')

    for x in f:
        #print(x)
        #if not x.startswith("|_"):
        pdf.set_text_color(r=255,g=0,b=0)
        pdf.cell(250,10,txt=x,ln=1)
        
        #print("----line break------")
    pdf.cell(250,10,txt="\n\n")
    f.close()
    print("nikto print started")
    pdf.set_text_color(r=0,g=0,b=0)
    pdf.cell(250,10,txt="NIKTO SCAN",ln=1)
    ipt = ".".join(filename.split(':'))
    try:
        temp = subprocess.Popen(['nikto','-host',ipt,'-o','/home/kali/Desktop/Final_Year_Project/cache/'+filename+'_nikto.txt'],stdout=subprocess.PIPE,universal_newlines=True)
        print(temp.stdout.read())
        #nikto -host 192.168.0.103 -o /home/kali/Desktop/Final_Year_Project/cache/192:168:0:103_nikto.txt
        f = open('/home/kali/Desktop/Final_Year_Project/cache/'+filename+'_nikto.txt','r')
        for x in f:
            pdf.set_text_color(r=0,g=0,b=0)
            pdf.cell(250,10,txt=x,ln=1)
        pdf.cell(250,10,txt="\n\n")
        f.close()
    except FileNotFoundError:
        print("Error in nikto scan")
        pass

    print(filename)
    pdf.output("/home/kali/Desktop/Final_Year_Project/results/"+"-".join(filename.split(":"))+"_webreport.pdf")
    pdf.close()
    return "-".join(filename.split(":"))+"_webreport.pdf"

if __name__ == "__main__":
    webtest_pdfmaker(sys.argv[1])