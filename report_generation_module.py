from fpdf import FPDF
import sys
def pdfmaker(filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=15)
    f = open('/home/kali/Desktop/Final_Year_Project/cache/'+filename+'.txt','r')
    pdf.cell(200,10,txt="CVE LIST of "+filename,ln=1,align="C")
    pdf.set_font("Arial",size=8)
    #print(f.read())
    for x in f:
        #print(x)
        if not x.startswith("|_"):
            pdf.set_text_color(r=255,g=0,b=0)
            pdf.cell(250,10,txt=x,ln=1,align="C")
        else:
            pdf.set_text_color(r=-1,g=-1,b=255)
            pdf.cell(250 ,5 , txt=x,ln=1)
        #print("----line break------")
    pdf.output("/home/kali/Desktop/Final_Year_Project/results/"+filename+"_CVE_Scan.pdf")
    pdf.close()
    return filename+"_CVE_Scan.pdf"

if __name__ == "__main__":
    pdfmaker(sys.argv[1])